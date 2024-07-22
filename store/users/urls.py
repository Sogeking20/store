from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('password-resete', PasswordResetView.as_view(template_name = "users/password_reset_form.html"), name ='password_reset'),
    path('password-resete/done/', PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name ='password_reset_done'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/del/<int:basket_id>/', views.delete_basket, name='delete_basket'),
]