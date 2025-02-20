import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from datetime import datetime, timedelta

from .base import FunctionalTest, wait


TEST_TELEGRAM_BOT_TOKEN = os.getenv("TEST_TELEGRAM_BOT_TOKEN")
TEST_TELEGRAM_BOT_NAME = "Telegram bot"



class NewVisitorTest(FunctionalTest):
    """Тест нового посетителя."""


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
        bot_name_field.send_keys(TEST_TELEGRAM_BOT_NAME)
        bot_token_field = self.browser.find_element(By.NAME, "token")
        bot_token_field.send_keys(TEST_TELEGRAM_BOT_TOKEN)
        bot_token_field.send_keys(Keys.ENTER)
        now_time = datetime.now()

        # Открывается страница с добавленным только что ботом. Пользователь видит на страницу информацию о боте: name, is_running, created_at, updated_at. Также на странице есть кнопка "Запустить".
        header_text = self.browser.find_element(By.TAG_NAME, "h2").text
        self.assertEqual(header_text, TEST_TELEGRAM_BOT_NAME)
        is_running_status = self.browser.find_element(By.TAG_NAME, "is_running_status").text
        self.assertFalse(is_running_status)
        created_at = self.browser.find_element(By.TAG_NAME, "created_at").text
        self.assertAlmostEqual(now_time, created_at, delta=timedelta(seconds=1))
        updated_at = self.browser.find_element(By.TAG_NAME, "updated_at").text
        self.assertEqual(created_at, updated_at)

        # Пользователь нажимает на кнопку "Запустить".
        start_bot = self.browser.find_element(By.ID, "start-bot-btn").click()

        self.fail("Нажал на кнопку 'Запустить'.")
