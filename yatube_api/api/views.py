from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Group, Post


class PostViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Post.

    Доступные HTTP методы:

    - GET;
    - POST;
    - PUT;
    - PATCH;
    - DELETE.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создает пост с автором из запроса."""
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для работы с моделью Group.

    Доступные HTTP методы:

    - GET;
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Comment.

    Доступные HTTP методы:

    - GET;
    - POST;
    - PUT;
    - PATCH;
    - DELETE.
    """

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)

    def get_post(self):
        """Получает объект поста с комментарием."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Возвращает комментарии к посту."""
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """Создает комментарий к посту, записывает пользователя в авторы."""
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(ModelViewSet):
    """
    ViewSet для работы с моделью Follow.

    Доступные HTTP методы:

    - GET;
    - POST;
    - PUT;
    - PATCH;
    - DELETE.
    """

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Возвращает комментарии к посту."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Создает подписку, возвращает ошибку если дубль или самоподписка."""
        serializer.save(user=self.request.user)
