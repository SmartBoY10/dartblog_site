from django.test import TestCase

from blog.models import Category

class CategoryrModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(title='Sport', slug='sport')

    def test_title_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Названия категории')

    def test_title_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(category.get_absolute_url(), '/blog/category/1')