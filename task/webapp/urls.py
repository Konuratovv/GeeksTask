from django.urls import path

from webapp.views import *

urlpatterns = [
    path('v1/tasks', TaskAPIView.as_view()),
    path('v1/tasks/<int:pk>', TaskAPIRetrieveUpdateDeleteView.as_view())
]
