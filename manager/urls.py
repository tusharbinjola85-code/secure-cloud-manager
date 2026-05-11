from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('register/', views.register_view, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('delete/<int:file_id>/', views.delete_file),

    path('logout/', views.logout_view),

]