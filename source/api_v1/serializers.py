from rest_framework import serializers
from webapp.models import Quote


class UserQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'author', 'email', 'text', ]
        read_only_fields = ['is_moderated']


class AdminQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'is_moderated', ]
        read_only_fields = ['id', 'author', 'email', 'rating', ]
