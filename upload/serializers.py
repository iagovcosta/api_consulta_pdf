from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField, ModelSerializer
from .models import File
import textract

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'title')


class pdf_text(ModelSerializer):

    text = SerializerMethodField()

    class Meta:
        model = File

    def get_text(self, obj):
        textract.process('api/media/testando.pdf')
        return str(obj.text.text)
