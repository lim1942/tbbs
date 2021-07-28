from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register('manage', views.UserViewSet)

app_name = 'users'
urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('', include(router.urls)),

]