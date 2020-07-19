from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from .models import Collection, User, Word


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    repassword = serializers.CharField(write_only=True)

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        else:
            raise ValidationError("Email already exists.")

    def validate_password(self, password):
        min_length = settings.MIN_LENGTH_PASSWORD
        if min_length > len(password):
            raise ValidationError(_("Password should be longer"))
        else:
            return password

    def validate(self, data):
        if data["password"] != data["repassword"]:
            raise ValidationError(_("The two password fields did not match."))
        return data

    def save(self, request):
        user = User(email=request.data["email"])
        user.set_password(request.data['password'])
        user.save()
        return user


class PasswordChangeSeializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    re_password = serializers.CharField()

    def validate(self, attrs):
        self.user = self.context['request'].user
        if not self.user or not self.user.check_password(attrs['old_password']):
            raise ValidationError(_('Old password is incorrect'))
        elif attrs['new_password'] != attrs['re_password']:
            raise ValidationError(_('New passwords are not the same'))
        else:
            self.set_new_password = attrs['new_password']
        return attrs
    
    def save(self):
        self.user.set_password(self.set_new_password)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except ObjectDoesNotExist:
            raise ValidationError(_('Account with the email does not exist'))
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField()
    re_new_password = serializers.CharField()

    def validate(self, attrs):
        if attrs['new_password'] != attrs['re_new_password']:
            raise ValidationError(_('New passwords are not the same'))
        return attrs

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ("key",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "collections", "words", "is_confirmed")
        read_only_fields = ("email", "collections", "words")


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ("id", "user", "title", "created_at", "words")
        read_only_fields = ('words',)


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = (
            "id",
            "user",
            "title",
            "translation",
            "progress",
            "collection",
        )


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("title",)
