from django.urls import path
from crud import views

urlpatterns = [
    path('studentapi/', views.student_api, name='student_api'),
    path('studentapi/<int:id>/', views.student_api, name='student_api'),
]
