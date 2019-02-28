from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name





class Image(models.Model):
    image_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    # photo = models.ImageField(upoad_to='images/')
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)

    @classmethod
    def get_photos(cls):
        return cls.objects.all()

    @classmethod
    def search_by_category(cls,category):
        images = Category.objects.filter(name__icontains=category)
        return images


