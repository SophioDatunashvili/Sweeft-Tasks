from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = URL
        fields = '__all__'

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/url/{obj.short_name}/')