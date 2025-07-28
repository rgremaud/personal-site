from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testemail@example.com",
            password="testpass1234"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testemail@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperemail@example.com",
            password="testpass1234"
        )
        self.assertEqual(user.username, "testsuperuser")
        self.assertEqual(user.email, "testsuperemail@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
