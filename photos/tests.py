from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTestClass():
    def setup(self):
        self.new_category = Category(name='test')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,category))



class ImageTestClass(TestCase):
    def setup(self):
        self.nairobi = Location(location_name='Nairobi')
        self.nairobi.save_location()

        # Creating a new category and saving it
        self.new_category = category(name='test')
        self.new_category.save_category()

        self.new_image = Image(name='test image', description='this is a test description',location=self.nairobi)
        self.new_image.save()

        self.new_image.category.add(self.new_category)

    def tearDown(self):
        Location.objects.all().delete()
        category.objects.all().delete()
        Image.objects.all().delete()



