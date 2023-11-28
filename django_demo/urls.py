from django.urls import path
from .views import login_view, logout_view, register_view, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login_view, name='template/login.html'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('', index, name='index'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
