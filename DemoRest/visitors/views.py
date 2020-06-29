from rest_framework import generics, viewsets
from .serializers import *
from .models import *
from .permission import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .mixins import LikedMixin

class VisitorCreateView(generics.CreateAPIView):
    serializer_class = VisitorDetailSerializer
    permission_classes = (IsAuthenticated, )

class VisitorsListView(generics.ListAPIView):
    serializer_class = VisitorsListSerializer
    queryset = Visitor.objects.all()
    permission_classes = (IsAuthenticated, )

class VisitorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VisitorDetailSerializer
    queryset = Visitor.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


class VisitorViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

