from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.budget_list,
        name='budget_list'
    ),

    path(
        'add/',
        views.add_budget,
        name='add_budget'
    ),

    path(
        'edit/<int:pk>/',
        views.edit_budget,
        name='edit_budget'
    ),

    path(
        'delete/<int:pk>/',
        views.delete_budget,
        name='delete_budget'
    ),

]