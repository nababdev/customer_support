from django.urls import path
from .views import MessageDetail, MessageList

urlpatterns = [
    path("messages/", MessageList.as_view(), name="messages"),
    path("messages/<int:pk>", MessageDetail.as_view(), name="messages_detail"),
]