from rest_framework.serializers import  ModelSerializer, PrimaryKeyRelatedField

from .models import Posts, Comments, Type


class TypesSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class PostSerializer(ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    type = TypesSerializer(read_only=True)
    type_id = PrimaryKeyRelatedField(queryset=Type.objects.all(), source='type', write_only = True)
    class Meta:
        model = Posts
        fields = '__all__'



