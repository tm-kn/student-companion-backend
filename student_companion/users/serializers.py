from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            },
            'password': {
                'write_only': True
            }
        }

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)

        user.set_password(validated_data['password'])

        user.save()

        return user


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'first_name': {
                'read_only': True
            },
            'last_name': {
                'read_only': True
            }
        }
