from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(name='Breakfast', price=20, description='A selection of breakfast items')

        self.assertEqual(str(menu), 'Breakfast : A selection of breakfast items')

        self.assertEqual(menu.name, 'Breakfast')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.description, 'A selection of breakfast items')

        self.assertEqual(menu.calculate_total_cost(), 30)