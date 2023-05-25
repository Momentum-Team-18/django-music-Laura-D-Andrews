from django.contrib import admin
from .models import Album, Label, Artist

admin.site.register(Album)
admin.site.register(Label)
admin.site.register(Artist)