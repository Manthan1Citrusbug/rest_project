from django.urls import path
from .views import student_insert, student_update, student_delete


urlpatterns = [
    path('student-insert/',student_insert,name="insert"),
    path('student-update/',student_update,name="update"),
    path('student-delete/',student_delete,name="delete")
]