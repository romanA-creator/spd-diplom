"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
from django.conf.urls.static import static
from django.conf import settings static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from posts.views import PostViewSet, LikeViewSet, CommentViewSet, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/',  RegisterView.as_view(), name='register'),
    path('api/posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('api/posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
    path('api/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    #path('api/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
    path('api/likes/', LikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='like-list'),
    #path('api/likes/<int:pk>/', LikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='like-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
