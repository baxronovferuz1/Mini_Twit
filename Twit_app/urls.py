
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, LikeViewSet, FollowViewSet, UserProfileView, CommentViewSet, RelatedAPIView
from . import views


router = SimpleRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('likes', LikeViewSet, basename='likes')
router.register('follows', FollowViewSet, basename='follows')
router.register('Comments',CommentViewSet, basename='comments')


urlpatterns = [
    path('me/', UserProfileView.as_view()),
    path('', include(router.urls)),
    path('page/', RelatedAPIView.as_view, name="page")
    #path('password/change/', views.password_change, name='password_change'),
    #path('password/get/', views.get_password, name='get_password'), """
]
