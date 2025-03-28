from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import MyPasswordResetForm,LoginForm,MyPasswordChangeForm

urlpatterns = [
    path("",views.home),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name='category-title'),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail"),
    path("profile/",views.ProfileView.as_view(),name="profile"), 
    path("address/",views.Address,name="address"),
    path("updateAddress/<int:pk>/",views.updateAddress.as_view(), name='updateAddress'),





    #login authentication
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path("accounts/login",auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('logout/', views.custom_logout, name='logout'),

    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html',form_class=MyPasswordResetForm),name='password_reset_done'),
    path('password-reset-confirm/<uidb64><token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MyPasswordResetForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html',form_class=MyPasswordResetForm),name='password_reset_complete'),
    



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)