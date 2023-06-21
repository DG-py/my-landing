from selenium import webdriver
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
        browser = self.browser.get('http://127.0.0.1:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('РАСУЛ СУЛЕЙМАНОВ', header)


if __name__ == '__main__':
    unittest.main()






# ПОД ШАПКОЙ ПРОФИЛЯ (О БОМНЕ)

# ПОД СТАТЬЕЙ ОБО МНЕ (МОИ СКИЛЫ)

# ПРИ КЛИКЕ ПО ОДНОМУ ИЗ ЗАГОЛОВКОВ РАСУЛ ПЕРЕХОДИТ К ЭТОМУ ПУНКТУ

# ОЗНАКОМИВШИСЬ С ПОРТФОЛИО РАСУЛ КЛИКНУЛ ПО ТЕКСТУ РАСУЛ СУЛЕЙМАНОВ
# ПОПАЛ ОБРАТНО НА ГЛАВГУЮ СТРАНИЦУ
