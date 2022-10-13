from rest_framework import serializers
from .models import Pengguna
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class MinimizedPenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = ["id", "display_name", "username"]


class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
        fields = [
            "id",
            "email",
            "username",
            "display_name",
            "phone",
        ]
