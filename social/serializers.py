from rest_framework import serializers
from .models import Post, Comment


class ViewCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ['text', 'author', 'created_on']

class feedSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'body', 'author', 'created_on']
class getPostSerializer(serializers.ModelSerializer):
    def get_comment(self,obj):

        cidt = str(obj)
        cid = cidt.split('(')[1].split(')')[0]
        c = Comment.objects.filter(post_id=int(cid))
        return ViewCommentSerializer(c, many=True).data
    author = serializers.ReadOnlyField(source='author.username')
    comment = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'body', 'author', 'created_on', 'comment']
        # fields = ['id','url','body','author','created_on']


class postPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['body']


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