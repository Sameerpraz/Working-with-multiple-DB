from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import *

router = routers.DefaultRouter()
router.register("faculty",FacultyView)


urlpatterns = [
    
]+router.urls