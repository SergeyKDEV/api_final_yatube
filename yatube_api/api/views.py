from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class PostViewSet(ModelViewSet):
    queryset = None


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = None


class CommentViewSet(ModelViewSet):
    queryset = None


class FollowViewSet(ModelViewSet):
    queryset = None
