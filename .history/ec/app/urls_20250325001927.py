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
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangeddone'),name='passwordchange'),
    path('passwordchangeddone/',auth_view.PasswordChangedDoneView.as_view(template_name='app/passwordchanged.html'),name='passwordchangeddone')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)