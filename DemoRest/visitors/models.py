from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    date_join_like = models.DateTimeField(auto_now_add=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Dislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dislikes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    date_join_dislike = models.DateTimeField(auto_now_add=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Visitor(models.Model):
    post_title = models.TextField(verbose_name='Title')
    post_body = models.TextField(verbose_name='Post_body')
    date_join = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)
    dislikes = GenericRelation(Dislike)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_dislikes(self):
        return self.dislikes.count()
