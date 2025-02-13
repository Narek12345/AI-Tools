import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


from .base import FunctionalTest



class NewVisitorTest(FunctionalTest):
    """Тест нового посетителя."""


    def test_telegram_platform(self):
        """Тест: пользователь хочет прочитать больше о автоматизации в Telegram."""

        # Нарек решает открыть главную страницу сайта.
        self.browser.get(self.live_server_url)

        # Проверяет, что заголовок содержит "AI-Tools".
        self.assertIn('AI-Tools', self.browser.title)

        # Проверяет, что в шапке есть "AI-Tools":
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("AI-Tools", header_text)

        # Находит ссылку "Telegram" и кликает по ней.
        telegram_link = self.browser.find_element(By.LINK_TEXT, "Telegram")
        ActionChains(self.browser).move_to_element(telegram_link).click()

        # Проверяет, что URL изменился на страницу Telegram.
        self.assertIn("/telegram", self.browser.current_url)

        # Проверяет, что на странице Telegram есть заголовок с названием платформы.
        header_text = self.browser.find_element(By.TAG_NAME, "h2").text
        
        # Нарек нажимает на кнопку "Подключить бота" для автоматизации.
        self.browser.find_element(By.LINK_TEXT, 'Подключить бота').click()

        # Появляется форма для ввода данных для подключения Telegram бота. Нарек вводит в форму свой Telegram bot token и нажимает Enter.
        inputbox = self.browser.find_element(By.ID, "id_telegram_bot_token")
        inputbox.send_keys("8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg")
        intupbox.send_keys(Keys.ENTER)

        # Открывается страница с его ботом. Он видит кнопку "Запустить" рядом с его созданным Telegram ботом.
        self.browser.fail("Нажимает на кнопку 'Запустить'.")
