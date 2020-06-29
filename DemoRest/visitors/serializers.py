from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class VisitorDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Visitor
        fields = (
            'id',
            'user',
            'post_title',
            'post_body'
        )

class VisitorsListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Visitor
        fields = (
            'id',
            'user',
            'post_title',
            'post_body',
            'total_likes',
            'total_dislikes',
            'date_join',
            'update_on'
        )


class VisitorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Visitor
        fields = (
            'id',
            'user',
            'total_likes',
            'total_dislikes',
        )

User = get_user_model()

class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )
    def get_full_name(self, obj):
        return obj.get_full_name()