
from rest_framework import serializers
from qrcode4e.models import UserImg

class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImg
        fields = "__all__"