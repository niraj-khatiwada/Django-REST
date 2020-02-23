from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('hello-world-api-viewset', views.HelloWorldViewset, basename = 'helloworld_apiviewset')

from . import views

urlpatterns = [
    path('hello-world/', views.HelloWorldAPIView.as_view(), name="Hello_World"),
    path('', include(router.urls))
]
