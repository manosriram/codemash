from rest_framework import serializers

from app.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    created = serializers.DateTimeField()
    score = serializers.FloatField()
    image_url = serializers.URLField()
    author = serializers.CharField()

    class Meta:
        model = Snippet
        fields = "__all__"

#  class RandomSnippetSerializer(serializers.ModelSerializer):
    #  code = serializers.CharField()
