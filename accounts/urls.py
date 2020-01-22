from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    url(r'^logout/$', LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^profile/$', views.view_profile, name = 'view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name = 'view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
    url(r'^change-password/$', views.change_password, name = 'change_password'),
    #url(r'^reset-password/$', PasswordResetView.as_view(template_name = 'accounts/reset-password.html'), 
    #name = 'reset_password'),
    #url(r'^reset-password/done$', PasswordResetDoneView.as_view(template_name = 'accounts/reset-password-done.html'), 
    #name = 'reset_password_done')
]
