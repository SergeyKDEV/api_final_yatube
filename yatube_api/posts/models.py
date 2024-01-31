from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Модель для постов."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self) -> str:
        """Возвращает значение всех полей поста, кроме изображения."""
        return (
            f'{self.text[:20]}, '
            f'{self.pub_date}, '
            f'{self.author}.'
        )


class Comment(models.Model):
    """Модель для комментариев."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        """Возвращает значение всех полей комментария."""
        return (
            f'{self.author}, '
            f'{self.post}, '
            f'{self.text[:20]}, '
            f'{self.created}.'
        )


class Group(models.Model):
    """Модель для сообществ."""

    title = models.TextField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        """Возвращает все поля сообщества."""
        return (
            f'{self.title[:20]}, '
            f'{self.slug}, '
            f'{self.description}.'
        )


class Follow(models.Model):
    """Модель для подписок."""

    pass
