from django.contrib import admin
from .models import Album, Label, Artist, Image

admin.site.register(Album)
admin.site.register(Label)
admin.site.register(Artist)
admin.site.register(Image)
