from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('hello-world-api-viewset', views.HelloWorldViewset, basename = 'helloworld_apiviewset')
router.register('profile', views.ProfileViewset)
router.register('login', views.LoginViewset, basename='login')
router.register('feed', views.ProfileFeedViewset)

from . import views

urlpatterns = [
    path('hello-world/', views.HelloWorldAPIView.as_view(), name="Hello_World"),
    path('', include(router.urls))
]
