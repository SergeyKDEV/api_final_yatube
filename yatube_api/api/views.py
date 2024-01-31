from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


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

    queryset = None


class GroupViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для работы с моделью Group.

    Доступные HTTP методы:

    - GET;
    """

    queryset = None


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
