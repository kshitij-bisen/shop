
from django.contrib import admin
from django.urls import path
from e_app import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .form import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm


urlpatterns = [
    # path('', views.index),
    path('', views.HomeView.as_view()),
    # path('product-detail/', views.product_detail),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view()),
    path('add-to-cart/', views.add_to_cart),
    path('buy-now/', views.buy_now),
    path('checkout/', views.checkout),
    path('orders/', views.orders),
    path('mobile/', views.mobile),
    path('mobile/<slug:data>', views.mobile,name='mobiledata'),            # slug because string
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    # path('changepassword/', views.change_password, name='changepassword'),
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='e_app/login.html',authentication_form=''), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='e_app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='e_app/passwordchangedone.html'), name='passwordchangedone'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='e_app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='e_app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='e_app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='e_app/password_reset_complete.html'), name='password_reset_complete'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
