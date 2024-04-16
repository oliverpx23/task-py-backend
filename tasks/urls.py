from django.urls import path, include
from rest_framework import routers
from tasks import views

# api versioning
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')
router.register(r'users', views.AppUserView, 'users')

urlpatterns = [
    path('v1/', include(router.urls)),
]
