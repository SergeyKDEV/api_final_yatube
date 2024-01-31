from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Group, Post

from .permissions import IsAuthorOrReadOnly
from .serializers import GroupSerializer, PostSerializer


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
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = (LimitOffsetPagination,)

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

    queryset = None


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

    queryset = None
