from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from base.models import Task


class TaskViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        self.test_task = Task.objects.create(user=self.user, title="Test Task", description="Test Description")

        self.task_list_url = reverse('tasks')
        self.task_create_url = reverse('task-create')
        self.task_detail_url = reverse('task-detail', args=[f'{self.test_task.id}'])

    def test_task_list_GET(self):
        response = self.client.get(self.task_list_url)
        self.assertTemplateUsed(response=response, template_name='base/task_list.html')

    def test_task_create_GET(self):
        response = self.client.get(self.task_create_url)
        self.assertTemplateUsed(response=response, template_name='base/task_create.html')

    def test_task_detail_GET(self):
        response = self.client.get(self.task_detail_url)
        self.assertTemplateUsed(response=response, template_name='base/task_detail.html')

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import Task


class TaskDeleteView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', password='password456')
        self.client.login(username='testuser', password='password123')

        self.user_task = Task.objects.create(user=self.user, title="User Task", description="User Description")
        self.other_task = Task.objects.create(user=self.other_user, title="Other Task", description="Other Description")

        self.task_delete_url = reverse('task-delete', args=[self.user_task.id])
        self.other_task_delete_url = reverse('task-delete', args=[self.other_task.id])

    def test_task_delete_view_access_GET(self):
        """
        Ensure the delete confirmation page is displayed for the owner of the task.
        """
        response = self.client.get(self.task_delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task_delete.html')

    def test_task_delete_view_access_GET_other_user(self):
        """
        Ensure that another user cannot access the delete view of a task they do not own.
        """
        response = self.client.get(self.other_task_delete_url)
        self.assertEqual(response.status_code, 404)

    def test_task_delete_POST_success(self):
        """
        Ensure that the task is deleted successfully when the owner confirms deletion.
        """
        response = self.client.post(self.task_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks'))
        self.assertFalse(Task.objects.filter(id=self.user_task.id).exists())

    def test_task_delete_POST_other_user(self):
        """
        Ensure that another user cannot delete a task they do not own.
        """
        response = self.client.post(self.other_task_delete_url)
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Task.objects.filter(id=self.other_task.id).exists())

    def test_task_delete_GET_not_authenticated(self):
        """
        Ensure that unauthenticated users cannot access the delete view.
        """
        self.client.logout()
        response = self.client.get(self.task_delete_url)
        self.assertEqual(response.status_code, 302)

    def test_task_delete_not_authenticated(self):
        """
        Ensure that unauthenticated users cannot access or delete a task.
        """
        self.client.logout()

        # Test GET request
        response_get = self.client.get(self.task_delete_url)
        self.assertEqual(response_get.status_code, 302)
        self.assertRedirects(response_get, f"{reverse('login')}?next={self.task_delete_url}")

        # Test POST request
        response_post = self.client.post(self.task_delete_url)
        self.assertEqual(response_post.status_code, 302)
        self.assertRedirects(response_post, f"{reverse('login')}?next={self.task_delete_url}")

        self.assertTrue(Task.objects.filter(id=self.user_task.id).exists())
