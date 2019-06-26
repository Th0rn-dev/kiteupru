from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

USER_NAME = 'test'
USER_EMAIL = '1@r.ru'
PASSWORD = '123'

class LoginVewsTest(TestCase):
    """Тест представления login()"""

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username=USER_NAME,
            password=PASSWORD)

    def test_uses_login_template(self):
        """тест: раздел Войти (kiteup.ru/accounts/login)использует
        шаблон login.html"""
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_login_ok(self):
        """тест: успешный логин"""
        login_ok = self.client.login(username='test', password='123')
        self.assertTrue(login_ok)

    def test_login_fake(self):
        """тест: фейк логин"""
        login_fake = self.client.login(username='test', password='fake')
        self.assertFalse(login_fake)


class DashboardViewsTest(TestCase):
    """Тест представления dashboard()"""

    def test_uses_dashboard_template(self):
        """тест: раздел 'Личный кабинет' использует шаблон dashboard.html"""
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'dashboard.html')

