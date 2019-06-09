import datetime
from django.test import TestCase
from news.models import ItemNews


# Create your tests here.

class NewsViewTest(TestCase):
    """тест представления новостей, раздел сайта 'Новости':
    kiteup.ru/club-news/"""
    def test_uses_news_template(self):
        """тест: раздел Новости (kiteup.ru/club-news/1)использует
        шаблон news.html"""
        news = ItemNews.objects.create(title_news='Новость 1')
        response = self.client.get(f'/club-news/{news.id}')
        self.assertTemplateUsed(response, 'news.html')

    def test_display_only_item_news(self):
        """тест: отображать определенную новость по id"""
        # создаем 2 разные новости
        correct_news = ItemNews.objects.create(title_news='Новость 1')
        news2 = ItemNews.objects.create(title_news='Новость 2')
        # делаем запрос на отображение корректной новости
        response = self.client.get(f'/club-news/{correct_news.id}')

        self.assertContains(response, 'Новость 1')
        self.assertNotContains(response, 'Новость 2')

    def test_view_date_dispalay(self):
        """тест: отображать дату создания новости"""
        date = datetime.datetime.now()
        news = ItemNews.objects.create(title_news='Новость 1')
        response = self.client.get(f'/club-news/{news.id}')
        self.assertContains(response, date.strftime('%d.%m.%Y'))

    def test_display_news_content(self):
        """тест: содержимое новости"""
        news = ItemNews.objects.create(
            title_news='Новость 1',
            content = 'Lorem ipsum'
        )
        self.assertEqual('Lorem ipsum', news.content)

    # 1)Использовать тестовый клиент Django,
    # 2) Проверить используемый шаблон и каждый элемент в контексте шаблона.
    # 3) Проверить, чтобы все обьекты били правильными либо наборы queryset имели правильные элементы.
    # 4) Проверить, чтобы все формы имели правильный класс.
    # 5) ПОдумать о тестировании логики шаблона: любой оператор for или if может заслужить минимального теста.
    # 6) В отношении представлений, которые обрабатывают POST-запросы, удостовериться, что тестируються оба случая: допустимый и недопустимый.
    # 7) Факультативно проверить на исправность, что форма выведена в качестве HTMLи ее ошибки визуально отображаются
