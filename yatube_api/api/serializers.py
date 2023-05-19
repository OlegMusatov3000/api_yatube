from rest_framework import serializers

from posts.models import Group, Post, Comment, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('post',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date', 'author', 'image', 'group',
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')
