from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet, UserViewSet

app_name = 'api'

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view(
            {'get': 'retrieve',
             'put': 'update',
             'patch': 'update',
             'delete': 'destroy'})
    ),
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view(
        {'get': 'list', 'post': 'create'})
    ),
    path('api-token-auth/', views.obtain_auth_token)

]
