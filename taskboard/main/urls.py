"""Файл с инструкциями для роутинга приложения"""
from django.urls import path
from rest_framework.routers import SimpleRouter
import main.views as views

app_name = 'main'

router = SimpleRouter()
router.register("entity", views.EntityViewSet)
router.register("comments", views.EntityCommentsViewSet)
router.register('L3', views.L3CommentViewSet)
router.register("bio", views.BIOView)
router.register("passport", views.PassportView)

urlpatterns = [
    path('changeStatus/<int:id>/', views.ChangeEntityStatusView.as_view()),
    path('entities/status/<int:status>/', views.EntitiesByStatusView.as_view()),
] + router.urls
