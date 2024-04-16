from rest_framework import viewsets
from .models import Task, AppUser
from .serializers import TaskSerializer, AppUserSerializer

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class AppUserView(viewsets.ModelViewSet):
    serializer_class = AppUserSerializer
    queryset = AppUser.objects.all()