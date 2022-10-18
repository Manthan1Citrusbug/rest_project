from django.urls import path
from .views import student_detail


urlpatterns = [
    path('student-detail/',student_detail,name="detail")
]