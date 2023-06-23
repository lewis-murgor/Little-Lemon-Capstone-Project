from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):

    def setUp(self):
        self.menu = Menu(title="IceCream", price=80, inventory=100)

    def test_instance(self):
        self.assertTrue(isinstance(self.menu, Menu))

    def test_save_menu(self):
        self.menu.save_menu()
        menu_item = Menu.objects.all()
        self.assertTrue(len(menu_item) > 0)
    
    def test_delete_menu(self):
        self.menu.save_menu()
        self.menu.delete_menu()
        menu_item = Menu.objects.all()
        self.assertTrue(len(menu_item) == 0)
