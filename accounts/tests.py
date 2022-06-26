from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="tester",
            email="tester@tests.com",
            password="testpwd"
        )
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.email, 'tester@tests.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testadmin",
            email="testadmin@tests.com",
            password="testadminpwd"
        )
        self.assertEqual(admin_user.username, 'testadmin')
        self.assertEqual(admin_user.email, 'testadmin@tests.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
