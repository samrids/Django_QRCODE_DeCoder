from qrcode4e.models import UserImg
from django.shortcuts import render
from qrcode4e.serializers import UserImgSerializer
from rest_framework import status
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
import json

from qrcode4e.forms import ImageForm

from PIL import Image
from pyzbar import pyzbar
import requests

class ImageViewSet(ListAPIView):
    queryset = UserImg.objects.all()
    serializer_class = UserImgSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = UserImg.objects.create(image=file)
        url = '{0}{1}'.format('http://127.0.0.1:8000',image)
        
        img = Image.open(requests.get(url, stream=True).raw)
        output = pyzbar.decode(img)
        image.decode_text = str(output[0].data.decode('UTF-8'))
        image.save()
        
        return HttpResponse(json.dumps({'text': str(output[0].data.decode('UTF-8'))}), status=status.HTTP_200_OK)


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'GET':
        form = ImageForm()
    return render(request, 'index.html', {'form': form})