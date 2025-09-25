from django.test import TestCase
from restaurant.models import MenuItem
from decimal import Decimal

# Create your tests here.

class MenuItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Use Decimal for price to match the model's DecimalField and follow PEP 8 for variable names
        cls.menu_item = MenuItem.objects.create(title="Pizza", price=Decimal('10.99'), inventory=5)

    def test_fields(self):
        """Test that the model fields have the correct types."""
        menu_item = self.menu_item
        self.assertIsInstance(menu_item, MenuItem)
        self.assertIsInstance(menu_item.title, str)
        # Price should be an instance of Decimal, not float
        self.assertIsInstance(menu_item.price, Decimal)
        self.assertIsInstance(menu_item.inventory, int)

    def test_values(self):
        """Test that the model instance has the correct values."""
        menu_item = self.menu_item
        self.assertEqual(menu_item.title, "Pizza")
        self.assertEqual(menu_item.price, Decimal('10.99'))
        self.assertEqual(menu_item.inventory, 5)

    def test_str_representation(self):
        """Test the string representation of the model."""
        menu_item = self.menu_item
        self.assertEqual(str(menu_item), "Pizza")
        
    def test_get_item(self):
        menu_item = self.menu_item
        self.assertEqual(str(menu_item), "Pizza : 10.99")
        
