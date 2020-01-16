from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model


class krazTests(TestCase):
    def test_string_representation(self):
        user = get_user_model().objects.create_user(username='testuser', email='test@test.com', password='secret')
        Post.objects.create(title='Test', body='Test Has Passed', author=user)
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'Test')

# Create your tests here.
