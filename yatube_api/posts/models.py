from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для сообществ."""

    title = models.TextField(
        max_length=200,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        """Дополнительная информация о модели Group."""
        verbose_name = 'группы'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        """Возвращает все поля сообщества."""
        return (
            f'{self.title[:20]} | '
            f'{self.slug} | '
            f'{self.description};'
        )


class Post(models.Model):
    """Модель для постов."""

    text = models.TextField(
        blank=False,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Группа'
    )

    class Meta:
        """Дополнительная информация о модели Post."""
        ordering = ('pub_date',)
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        """Возвращает значение всех полей поста, кроме изображения."""
        return (
            f'{self.text[:20]} | '
            f'{self.pub_date} | '
            f'{self.author};'
        )


class Comment(models.Model):
    """Модель для комментариев."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Связанный пост'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        """Дополнительная информация о модели Comment."""
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        """Возвращает значение всех полей комментария."""
        return (
            f'{self.author} | '
            f'{self.post} | '
            f'{self.text[:20]} | '
            f'{self.created};')


class Follow(models.Model):
    """Модель для подписок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        null=True,
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        null=True,
        verbose_name='Автор'
    )

    class Meta:
        """Дополнительная информация о модели Follow."""
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_prevent_to_self_follow',
                check=~models.Q(user=models.F('following')),
            ),
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='%(app_label)s_%(class)s_prevent_to_exists_follow',
            ),
        ]
        verbose_name = 'подписки'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        """Возвращает все поля подписки."""
        return (
            f'{self.user} -> '
            f'{self.following};'
        )
