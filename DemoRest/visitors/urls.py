from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'visitor/likedislike', VisitorViewSet)

app_name = 'visitors'
urlpatterns = router.urls+[
    path('visitor/create/', VisitorCreateView.as_view()),
    path('visitor/all/', VisitorsListView.as_view()),
    path('visitor/detail/<int:pk>/', VisitorDetailView.as_view()),

]