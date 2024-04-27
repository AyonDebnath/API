from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view())
]