from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from .models import File

# Create your views here.
class FileUploadView(APIView):

    parser_classes = (JSONParser, MultiPartParser)

    class Meta:
        model = File

    def post(self, request):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():

            file_serializer.save()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

