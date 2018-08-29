from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    #as_view in quanto si tratta di una class based view
    path('users/', views.UserList.as_view(), name='user_list'),
    path('user/<username>/', views.userProfileView, name='user_profile'),
    path('cerca/', views.cerca, name='funzione_cerca')
]
