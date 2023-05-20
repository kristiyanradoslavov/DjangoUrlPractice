from django.urls import path
from djangoProjectUrlPractice.departments import views

urlpatterns = [
    path("", views.index, name="index view"),
    path("<slug:department_id>/", views.departments, name='different deps')
]
