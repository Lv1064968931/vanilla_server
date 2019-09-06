from rest_framework import serializers
from .models import User, vocabulary, Sentence, Userdata, Strangeword, Clockingdata
from .models import PhoneVerifyRecord


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerifyRecord
        fields = "__all__"


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = vocabulary
        fields = "__all__"


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = "__all__"

class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = "__all__"

class StrangewordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strangeword
        fields = "__all__"

class ClockingdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clockingdata
        fields = "__all__"