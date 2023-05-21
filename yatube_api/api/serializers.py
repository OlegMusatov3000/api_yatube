from rest_framework import serializers

from posts.models import Group, Post, Comment, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('post',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')
