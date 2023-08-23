from rest_framework import serializers
from .models import User, Property, Compound, PassType, PassRequest, Payment, Notification, PropertyOwnerVerification, NationalIDVerification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class CompoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compound
        fields = '__all__'

class PassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassType
        fields = '__all__'

class PassRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassRequest
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class PropertyOwnerVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyOwnerVerification
        fields = '__all__'

class NationalIDVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalIDVerification
        fields = '__all__'
