import os

import jwt
from django.contrib.auth import user_logged_in
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler

from .models import User
from .serializers import UserSerializer

from dotenv import load_dotenv

load_dotenv()


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Actually works with data, doesn't render anything.
        Receives data from request, validates and saves it.
        :returns Response()
        """
        user = request.POST
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @api_view(['POST'])
    def authenticate_user(self, request):
        """
         Actually works with data, doesn't render anything.
         Tries to authenticate user and generates JWT-token for them.
        :returns Response()
        """
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.get(email=email, password=password)
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, os.environ.get('SECRET_KEY'))
                    user_details = {}
                    user_details['name'] = "%s %s" % (
                        user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)
                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)

    def register_user(self, request):
        """
        Renders user_register template if request.method == GET,
        creates row in database with data from html form if request.method == POST
        """
        if request.method == 'POST':
            response = self.post(request)
            if response.status_code == 201:
                return redirect('users:main')
        else:
            return render(request, 'users/user_registration.html')

    def show_profile(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        context = {
            'user': user
        }
        return render(request, 'users/user_profile.html', context)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
