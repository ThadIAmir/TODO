from django.test import SimpleTestCase
from django.urls import reverse, resolve

from base.views import CustomLoginView, RegisterView, TaskDelete


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_task_delete_url_resolves(self):
        url = reverse('task-delete', args=['sth'])
        self.assertEqual(resolve(url).func.view_class, TaskDelete)
