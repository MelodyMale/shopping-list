from django.urls import path

from core import views

urlpatterns = [
    path("item/", views.ItemList.as_view()),
    path("item/<int:pk>/", views.ItemDetail.as_view()),
]
