from django.urls import path, include

from . import views

from rest_framework import  routers

router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile-viewset', views.ProfileViewSet)
router.register('login', views.LoginViewset, basename= 'login')


urlpatterns = [
    path('hello-api/', views.HelloAPIView.as_view(), name = 'HelloAPI'),
    path('', include(router.urls))
]
