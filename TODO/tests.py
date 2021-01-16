from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Todo

# Create your tests here.

class TodoTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.todo = Todo.objects.create(
            title='Read more on CSS',
            description='Your CSS skills is lacking',
            deadline='2021-1-19 22:30:35'
        )

    def test_string_representation(self):
        todo = Todo(title='A sample Todo')
        self.assertEqual(str(todo), todo.title)

    def test_todo_content(self):
        self.assertEqual(f'{self.todo.title}', 'Read more on CSS')
        self.assertEqual(f'{self.todo.description}', 'Your CSS skills is lacking')
        self.assertEqual(f'{self.todo.deadline}', '2021-1-19 22:30:35')

    def test_todo_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Read more on CSS')
        self.assertTemplateUsed(response, 'home.html')

    def test_todo_detail_view(self):
        response = self.client.get('/todo/1')
        no_response = self.client.get('/todo/1000000000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Read more on CSS')
        self.assertTemplateUsed(response, 'todo_detail.html')
