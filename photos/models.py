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

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.get(id = self.id).delete()

    def update_image(self,val):
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):
        return cls.objects.get(id = image_id)

    @classmethod
    def copy_image(image_url):
        find_image = Image.get_image_by_id(image_id)
        return pyperclip.copy(find_image.image_url)

    @classmethod
    def show_image(cls,category):
        images = cls.objects.filter(category__name=category)
        return images

        
    @classmethod
    def get_photos(cls):
        return cls.objects.all()


    @classmethod
    def search_by_category(cls,category):
        photo = Category.objects.filter(name__icontains = category)[0]
        return  cls.objects.filter(category__id = photo.id)

    @classmethod
    def filter_by_location(cls,location):
        the_location = Location.objects.get(name = location)
        return cls.objects.filter(location__id = the_location.id)

    def __str__(self):
        return self.name