from django.db import models

class Location(models.Model):
   name = models.CharField(max_length = 30)

   def save_location(self):
       self.save()

   def delete(self):
       self.delete()

   def update(self,field,val):
       Location.objects.get(id = self.id).update(field = val)

   def __str__(self):
       return self.name

class Category(models.Model):
   name = models.CharField(max_length = 30)
   def save_category(self):
       self.save()

   def delete(self):
       Category.objects.get(id = self.id).delete()

   def update(self,field,val):
       Category.objects.get(id = self.id).update(field = val)

   def __str__(self):
       return self.name




class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    image_url = models.ImageField(upload_to = 'articles/')

    @classmethod
    def get_photos(cls):
        return cls.objects.all()

    @classmethod
    def search_by_category(cls,category):
        images = Category.objects.filter(name__icontains=category)
        return images


