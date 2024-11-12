from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from ..models import Task

class TaskAPITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.url = '/api/tasks/'

    def test_create_task(self):
        """
            Test creating a task.
        """
        data = {
            'title': 'Test Task',
            'completed': False,
            'description': 'This is a test task',
            'created_at': '2024-11-11T10:00:00Z'
        }
        response = self.client.post(self.url, data, format='json')
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Task')
        self.assertEqual(response.data['completed'], False)

    def test_get_task(self):
        """
            Test retrieving a task.
        """
        task = Task.objects.create(
            title='Test Task',
            completed=False,
            description='Test task description',
            created_at='2024-11-11T10:00:00Z'
        )
        response = self.client.get(f'{self.url}{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        """
            Test updating a task.
        """
        task = Task.objects.create(
            title='Test Task',
            completed=False,
            description='Test task description',
            created_at='2024-11-11T10:00:00Z'
        )
        updated_data = {
            'title': 'Updated Task',
            'completed': True,
            'description': 'Updated task description',
            'created_at': '2024-11-11T10:00:00Z'
        }
        response = self.client.put(f'{self.url}{task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')
        self.assertEqual(response.data['completed'], True)

    def test_delete_task(self):
        """
            Test deleting a task.
        """
        task = Task.objects.create(
            title='Test Task',
            completed=False,
            description='Test task description',
            created_at='2024-11-11T10:00:00Z'
        )
        response = self.client.delete(f'{self.url}{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the task is deleted
        self.assertEqual(Task.objects.count(), 0)

    def test_get_tasks_without_authentication(self):
        """
            Test retrieving tasks without authentication (should fail).
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + "not a token")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_without_authentication(self):
        """
            Test creating a task without authentication (should fail).
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + "not a token")
        data = {
            'title': 'Test Task',
            'completed': False,
            'description': 'This is a test task',
            'created_at': '2024-11-11T10:00:00Z'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
