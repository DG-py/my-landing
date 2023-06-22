from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):


# ЖИЛ РАСУЛ
# РАСУЛ ИЗУЧАЕТ ПРОГРАМИРОВАНИЕ И РАБОТАЕТ МЕНЕДЖЕРОМ
# ОДНАЖДЫ РАСУЛ РЕШИЛ ПРОКАЧАТЬСЯ В АЙТИ
# РАСУЛ ЗАШЕЛ В ГУГЛ ВВЕЛ ЗАПРОС (СОЗДАНИЕ ЛАНДИНГА ) И КЛИКНУЛ ПО ОДНОЙ ИЗ ССЫЛОК

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В БРАУЗЕРЕ РАСУЛА ОТКРЫЛСЯ САЙТ (ПО АДРЕСУ http://127.0.0.1:8000)
        # В ЗОГОЛОВКЕ САЙТА РАСУЛ ПРОЧИТАЛ (САЙТ ПОРТФОЛИО РАСУЛА СУЛЕЙМАНОВА)
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('САЙТ ПОРТФОЛИО РАСУЛА СУЛЕЙМАНОВА', self.browser.title)
        #self.fail('Finish the test!')

    def test_home_page_header(self):
        # В ШАПКЕ САЙТА НАПИССАНО ( РАСУЛ СУЛЕЙМАНОВ)
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Rasul Suleymanov', header.text)

    def test_home_page_blog_foto(self):
        # ПОД ШАПКОЙ ПРОФИЛЯ (О БОМНЕ)
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # ПОД СТАТЬЕЙ ОБО МНЕ (МОИ СКИЛЫ)
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element_by_class_name('article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)


if __name__ == '__main__':
    unittest.main()








# ПОД СТАТЬЕЙ ОБО МНЕ (МОИ СКИЛЫ)

# ПРИ КЛИКЕ ПО ОДНОМУ ИЗ ЗАГОЛОВКОВ РАСУЛ ПЕРЕХОДИТ К ЭТОМУ ПУНКТУ

# ОЗНАКОМИВШИСЬ С ПОРТФОЛИО РАСУЛ КЛИКНУЛ ПО ТЕКСТУ РАСУЛ СУЛЕЙМАНОВ
# ПОПАЛ ОБРАТНО НА ГЛАВГУЮ СТРАНИЦУ
