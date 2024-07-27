from django.urls import path
from . import views
from .views import SignUpView


# app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/review/', views.add_review, name='add_review'),
    path('order/', views.create_order, name='create_order'),
    path('order/success/', views.order_success, name='order_success'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    # path('accounts/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]
#
# urlpatterns += [
#     path('signup/', SignUpView.as_view(), name='signup'),
# ]
