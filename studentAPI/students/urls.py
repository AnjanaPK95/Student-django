from django.urls import path
from .views import StudentCreate

urlpatterns = [
    path('students/', StudentCreate.as_view(), name='student-create'),
]
