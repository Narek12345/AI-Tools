import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from .base import FunctionalTest, wait



class NewVisitorTest(FunctionalTest):
    """Тест нового посетителя."""


    @wait
    def test_telegram_platform(self):
        """Тест: пользователь хочет прочитать больше о автоматизации в Telegram."""

        # Пользователь решает открыть главную страницу сайта.
        self.browser.get(self.live_server_url)

        # Проверяет, что заголовок содержит "AI-Tools".
        self.assertIn('AI-Tools', self.browser.title)

        # Проверяет, что в шапке есть "AI-Tools":
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("AI-Tools", header_text)

        # Находит ссылку "Telegram" и кликает по ней.
        telegram_link = self.browser.find_element(By.LINK_TEXT, "Telegram")
        self.browser.execute_script("arguments[0].click();", telegram_link)

        # Проверяет, что URL изменился на страницу Telegram.
        self.assertIn("/telegram", self.browser.current_url)

        # Проверяет, что на странице Telegram есть заголовок с названием платформы.
        header_text = self.browser.find_element(By.TAG_NAME, "h2").text
        
        # Пользователь нажимает на кнопку "Подключить бота" для автоматизации.
        self.browser.find_element(By.LINK_TEXT, 'Подключить бота').click()

        # Появляется форма для ввода данных для подключения Telegram бота. Пользователь вводит в форму название боту и свой Telegram bot token и нажимает Enter.
        bot_name_field = self.browser.find_element(By.NAME, "name")
        bot_name_field.send_keys("Telegram bot")
        bot_token_field = self.browser.find_element(By.NAME, "token")
        bot_token_field.send_keys("8083179427:AAF5z0kDDygySnBfzLAkYe9RFYcfcuC9pTg")
        bot_token_field.send_keys(Keys.ENTER)

        # Открывается страница с добавленным только что ботом. Пользователь видит кнопку "Запустить" рядом с его созданным Telegram ботом. Пользователь нажимает на кнопку "Запустить".
        header_text = self.browser.find_element(By.TAG_NAME, "h2").text
        self.assertIn(header_text, "Telegram bot")
        run_button = self.browser.find_element(By.XPATH, '//button[text()="Запустить"]')
        self.assertIsNotNone(run_button)
        run_button.click()

        self.fail("Нажимает на кнопку 'Запустить'.")
