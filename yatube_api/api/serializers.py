from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Метакласс сериализатора Post."""
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        """Метакласс сериализатора Group."""
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Comment.

    Атрибуты:
    author : SlugRelatedField
        поле для вывода имени автора из модели User по полю 'username'.
    """

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Метакласс сериализатора Comment."""
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Comment.

    Атрибуты:
    user : SlugRelatedField
        поле для вывода имени подписчика из модели User по полю 'username'
    following : SlugRelatedField
        поле для вывода имени автора из модели User по полю 'username'
    """

    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Метакласс сериализатора Follow."""
        fields = '__all__'
        model = Follow
