from django.urls import path

from . import views

resturant_crud = views.ResturantCRUD()
menu_crud = views.MenuCRUD()

urlpatterns = [
    path('', views.index, name='index'),
    path('create/resturant', resturant_crud.create, name='create_resturant'),
    path('<int:resturant_id>', resturant_crud.read, name='read_resturant'),
    path('create/menu', menu_crud.create, name='create_menu'),
    path('menu/<int:menu_id>', menu_crud.read, name='read_menu'),
    path('edit/menu/<int:menu_id>', menu_crud.update, name='edit_menu'),
    path('edit/resturant/<int:resturant_id>', resturant_crud.update, name='edit_resturant'),
    path('vote/<int:resturant_id>', views.vote, name='vote'),
    path('vote/reset', views.reset_votes, name='reset_votes'),

]