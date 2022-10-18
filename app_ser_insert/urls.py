from django.urls import path
from .views import student_insert, student_update


urlpatterns = [
    path('student-insert/',student_insert,name="insert"),
    path('student-update/',student_update,name="update")
]