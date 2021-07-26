from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment import views

router = DefaultRouter()
router.register('entry', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]