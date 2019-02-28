from django.contrib import admin
from .models import Location,Image,Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Location)
admin.site.register(Image,ImageAdmin)
admin.site.register(Category)
