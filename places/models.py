from django.db import models
from django.urls import reverse

class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('places:detail', args=[self.slug])

    def __str__(self):
        return self.name

class Photo(models.Model):
    place = models.ForeignKey(Place, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='places/%Y/%m/%d/')
    caption = models.TextField(blank=True)
    taken_at = models.DateField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title or 'Photo'} - {self.place.name}"
