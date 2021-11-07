from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from home import views
from dashboard import views as dashboard_view
from sign_up import views as signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_login, name="login"),
    path('signup/', signup_view.signup_site, name="signup"),
    path('dashboard/', dashboard_view.dashboard, name="dashboard"),
    path('info_register/', dashboard_view.patients_register, name="info_register"),
    path('file_converter/', dashboard_view.file_converter, name="file_converter"),
    path('file_converter/<int:pk>/', dashboard_view.delete_profile, name="delete_profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
