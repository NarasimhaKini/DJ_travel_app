from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Place
from django.core.serializers import serialize

def map_view(request):
    # Server-rendered page including map; JS will fetch /api/places/
    return render(request, 'places/map.html')

def places_api(request):
    # Return places with minimal fields and photo counts + thumbnails (first photo)
    places = Place.objects.all().prefetch_related('photos')
    data = []
    for p in places:
        first_photo = p.photos.first()
        data.append({
            'id': p.id,
            'name': p.name,
            'slug': p.slug,
            'lat': float(p.latitude),
            'lng': float(p.longitude),
            'description': p.description[:200],
            'photo_count': p.photos.count(),
            'thumbnail': first_photo.image.url if first_photo else None,
            'detail_url': p.get_absolute_url(),
        })
    return JsonResponse(data, safe=False)

def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)
    photos = place.photos.all()
    return render(request, 'places/place_detail.html', {
        'place': place,
        'photos': photos
    })
