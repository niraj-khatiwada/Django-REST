from django.urls import path, include

from .views import HelloAPIView

urlpatterns = [
    path('', HelloAPIView.as_view(), name = 'HelloAPI')
]
