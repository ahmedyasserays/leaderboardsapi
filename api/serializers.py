from rest_framework import serializers 
from renderer.models import score, leaderBoard

class boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = leaderBoard
        fields = "__all__"


class scoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = score
        fields = "__all__"
