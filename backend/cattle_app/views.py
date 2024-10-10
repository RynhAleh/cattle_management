from .models import Cattle
from .serializers import CattleSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.response import Response


class CattleViewSet(viewsets.ModelViewSet):
    queryset = Cattle.objects.all()
    serializer_class = CattleSerializer


class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        users = User.objects.all()
        user_data = [{'id': user.id, 'username': user.username} for user in users]
        return Response(user_data)
