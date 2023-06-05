from django.urls import path
from . import views
# from knox import views as knox_views

urlpatterns = [
    path('',views.ListProductView.as_view(), name='product'),
    path('add_product/',views.CreateProductView.as_view(), name='create_product'),
    path('<pk>/update_product/',views.UpdateProductView.as_view(), name='product_update'),
    path('<pk>/delete_product/',views.DeleteProductView.as_view(), name='product_delete'),
    path('order/',views.ListOrderView.as_view(), name='order'),
    path('add_order/',views.CreateOrderView.as_view(), name='create_order'),
    path('<pk>/update_order/',views.UpdateOrderView.as_view(), name='order_update'),
    path('<pk>/delete_order/',views.DeleteOrderView.as_view(), name='order_delete'),
    path('panier/ajouter/<int:produit_id>/', views.ajouter_au_panier),
    path('panier/supprimer/<int:produit_id>/', views.supprimer_du_panier),
    path('cart/', views.afficher_panier),
    # path('cart/add/<int:product_id>', views.add_to_cart, name='add-to-cart'),
    # path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    # path('cart/view/', views.view_cart, name='view-cart'),
    # path('login/',views.login_api, name='login'),
    # path('user/',views.get_user_data, name='user'),
    # path('register/',views.register_api, name='register'),
    # path('logout/',knox_views.LogoutView.as_view(), name='logout'),
   









]
