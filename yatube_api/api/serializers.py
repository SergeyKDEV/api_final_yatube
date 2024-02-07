from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


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

    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Метакласс сериализатора Comment."""
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Comment.

    Атрибуты:
    user : SlugRelatedField
        поле для вывода имени подписчика из модели User по полю 'username'
    following : SlugRelatedField
        поле для вывода имени автора из модели User по полю 'username'
    """

    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        required=False
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        required=True
    )

    class Meta:
        """Метакласс сериализатора Follow."""
        fields = 'user', 'following'
        model = Follow

    def validate(self, data):
        """Проверка на самоподписку и дубликаты."""
        user = self.context['request'].user
        following = data.get('following')

        if user == following:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя!')
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                f'Вы уже подписаны на автора {following}!')

        return data
