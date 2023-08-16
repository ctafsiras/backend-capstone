from django.test import TestCase

from .models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item= Menu.objects.create(title='menu 2',price=12.0,inventory=100)
        itemstr=item.get_item()

        self.assertEqual(itemstr,'menu 2 : 12.0')