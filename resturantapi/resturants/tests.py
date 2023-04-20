import pytest

from django.test import TestCase, RequestFactory

from mixer.backend.django import mixer

from django.urls import reverse, resolve


class TestUrls(TestCase):
    def test_create_resturant_url(self):
        path = reverse('resturants:create_resturant')
        assert resolve(path).view_name == 'resturants:create_resturant'

    def test_read_resturant_url(self):
        path = reverse('resturants:read_resturant', kwargs={'resturant_id': 1})
        assert resolve(path).namespace == 'resturants'

    def test_vote_reset_url(self):
        path = reverse('resturants:reset_votes')
        assert resolve(path).app_name == 'resturants'


@pytest.mark.django_db
class TestModels(TestCase):
    def test_resturant_has_votes(self):
        resturant = mixer.blend('resturants.Resturant', votes=1)
        assert resturant.has_votes == True

    def test_resturant_has_no_votes(self):
        resturant = mixer.blend('resturants.Resturant', votes=0)
        assert resturant.has_votes == False


@pytest.mark.django_db
class TestViews(TestCase):
    def test_index(self):
        mixer.blend('resturants.Resturant')
        mixer.blend('resturants.Menu')
        path = reverse('resturants:index')
        response = self.client.get(path)
        assert response.status_code == 200

    def test_vote(self):
        mixer.blend('resturants.Resturant', resturant_id=1)
        path = reverse('resturants:vote', kwargs={'resturant_id': 1})
        response = self.client.get(path)
        assert response.status_code == 302
