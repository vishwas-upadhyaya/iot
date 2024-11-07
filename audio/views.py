from django.shortcuts import render

# Create your views here.

# audio/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
# from mlsubtopic.speechtotext import transcribe_audio
# views.py
import os
from django.conf import settings
from django.shortcuts import render
from .forms import ImageUploadForm
from mlsubtopic.ImageToText import convert


# from mlsubtopic.res_gen import get_text

@csrf_exempt  # Use this only for testing purposes, ideally use CSRF protection in production
def upload_image(request):
    # uploaded_file_url = None
    str1 = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            title = form.cleaned_data['title']
            # Define the path where the file will be saved
            image_file.name = "testing4.png"
            file_path = os.path.join(settings.UPLOAD_FOLDER, image_file.name)
            # Save the file manually
            with open(file_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
            # Generate the URL for displaying the image
            str1 = convert(file_path)

            # print(str)
            # uploaded_file_url = f'/media/{image_file.name}'
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form, 'audio': str1})

