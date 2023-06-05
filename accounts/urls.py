from django.urls import path
from . import views
from knox import views as knox_views
from .views import ShopperCreateAPIView, LoginAPIView, PasswordResetAPIView, PasswordResetConfirmAPIView,DeleteShopperView

urlpatterns = [
    path('register/', ShopperCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('password_reset/', PasswordResetAPIView.as_view()),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view()),
    path('<int:pk>/delete/', DeleteShopperView.as_view(), name='delete_shopper'),
    path('',views.ListShopperView.as_view(), name='shopper'),
]