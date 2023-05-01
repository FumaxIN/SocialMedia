from rest_framework import serializers
from .models import Post, Comment, UserProfile, Like
from django.contrib.auth.models import User


class ViewCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['text', 'author', 'created_on']


class feedSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()
    # liked_by_current_user = serializers.SerializerMethodField()
    class Meta:
        model = Post
        # fields = ['id', 'body', 'author', 'media', 'likes_count', 'liked_by_current_user', 'created_on']
        fields = ['id', 'body', 'author', 'media', 'likes_count', 'created_on']
    def get_likes_count(self, obj):
        return obj.like_set.count()

    # def get_liked_by_current_user(self, obj):
    #     request = self.context['request'] # Get request object from context
    #     user = request.user # Get current user from request
    #     if user.is_authenticated:
    #         try:
    #             like = Like.objects.get(user=user.userprofile, post=obj)
    #             return True
    #         except Like.DoesNotExist:
    #             return False
    #     return False


class getPostSerializer(serializers.ModelSerializer):
    def get_comment(self, obj):
        print("&&&&&&&&&&&&&&")
        print(obj)
        cidt = str(obj)
        cid = cidt.split('(')[1].split(')')[0]
        print(cid)
        c = Comment.objects.filter(post_id=int(cid))
        return ViewCommentSerializer(c, many=True).data

    author = serializers.ReadOnlyField(source='author.username')
    comment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'body', 'media', 'author', 'created_on', 'comment']


class postPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['body', 'media']


class CommentSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     instance = super().create(validated_data)
    #     instance.post = Post.objects.get(id=self.initial_data['post'])
    #     instance.save()
    #     return  instance

    class Meta:
        model = Comment
        fields = ['text']


class ViewCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['text', 'author', 'created_on']


class UserDetailsSerializer(serializers.ModelSerializer):
    # def get_posts(self, obj):
    #     user = self.context['request'].user.username
    #     posts = Post.objects.get(author=user)
    #     return feedSerializer(posts, many=True)
    bio_s = serializers.ReadOnlyField(source='userprofile.bio')
    dp = serializers.ImageField(source='userprofile.profile_image')
    # posts_by_user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'dp', 'first_name', 'last_name', 'bio_s']


class UpdateProfileSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'bio']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.userprofile.bio = validated_data.get('bio', instance.userprofile.bio)
        instance.save()
        instance.userprofile.save()
        return instance

# class postAction

class UserLikedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user']


