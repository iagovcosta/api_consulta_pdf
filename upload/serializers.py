from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField, ModelSerializer
from .models import File
import textract

class FileSerializer(serializers.ModelSerializer):

    text = SerializerMethodField('get_text')

    class Meta:
        model = File
        fields = '__all__'

    def get_text(self, obj):
        text = textract.process('api/media/testando.pdf')
        return text




