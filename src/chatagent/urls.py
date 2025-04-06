from django.urls import path
from . import views

urlpatterns = [
    path('create_session/', views.create_session, name='create_session'),
    path('chat/<int:session_id>/', views.view_chat, name='view_chat'),
    path('chat/<int:session_id>/post_message/', views.post_message, name='post_message'),
]
