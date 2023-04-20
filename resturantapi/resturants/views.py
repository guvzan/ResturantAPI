from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ResturantForm, MenuForm
from .models import Resturant, Menu


def index(request):
    resturants = Resturant.objects.all().order_by('-votes')
    menus = Menu.objects.filter(resturant=resturants[0])
    context = {
        'resturants': resturants,
        'menus': menus,
        'winner': resturants[0]
    }
    return render(request, 'resturants/index.html', context)


@login_required
def vote(request, resturant_id):
    if request.method == "POST":
        resturant = Resturant.objects.get(id=resturant_id)
        resturant.votes += 1
        resturant.save()
    return redirect('resturants:index')


@login_required
def reset_votes(request):
    resturants = Resturant.objects.all()
    for resturant in resturants:
        resturant.votes = 0
        resturant.save()
    return redirect('resturants:index')


class ResturantCRUD:

    def create(self, request):
        if request.method == 'POST':
            form = ResturantForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('resturants:index')
        else:
            form = ResturantForm()
        context = {
            'form': form
        }
        return render(request, 'resturants/create_resturant.html', context)

    def read(self, request, resturant_id):
        resturant = Resturant.objects.get(id=resturant_id)
        menus = Menu.objects.filter(resturant=resturant)
        context = {
            'resturant': resturant,
            'menus': menus
        }
        return render(request, 'resturants/resturant_profile.html', context)

    def update(self, request, resturant_id):
        resturant = Resturant.objects.get(id=resturant_id)
        if request.method == 'POST':
            form = ResturantForm(instance=resturant, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('resturants:index')
        else:
            form = ResturantForm(instance=resturant)
        context = {
            'form': form,
            'resturant': resturant
        }
        return render(request, 'resturants/edit_resturant.html', context)

    def delete(self, request):
        pass


class MenuCRUD:
    def create(self, request):
        if request.method == 'POST':
            form = MenuForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('resturants:index')
        else:
            form = MenuForm()
        context = {
            'form': form
        }
        return render(request, 'resturants/create_menu.html', context)

    def read(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        context = {
            'menu': menu
        }
        return render(request, 'resturants/menu_info.html', context)

    def update(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        if request.method == 'POST':
            form = MenuForm(instance=menu, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('resturants:index')
        else:
            form = MenuForm(instance=menu)
        context = {
            'form': form,
            'menu': menu
        }
        return render(request, 'resturants/edit_menu.html', context)

    def delete(self, request):
        pass
