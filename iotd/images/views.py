from django.shortcuts import render
from images.models import FeaturedImage
from django.conf import settings

def home(request):
    image = FeaturedImage.objects.latest('uploaded') 
    print(settings.STATIC_ROOT)
    context = {
        'image': image
    }
    return render(request, 'images/home.html',
                              context)
