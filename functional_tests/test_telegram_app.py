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

        # Появляется форма для ввода данных для подключения Telegram бота. Пользователь вводит в форму название бота и свой Telegram bot token и нажимает Enter.
        bot_name_field = self.browser.find_element(By.NAME, "name")
        bot_name_field.send_keys(TEST_TELEGRAM_BOT_NAME)
        bot_token_field = self.browser.find_element(By.NAME, "token")
        bot_token_field.send_keys(TEST_TELEGRAM_BOT_TOKEN)
        bot_token_field.send_keys(Keys.ENTER)
        now_time = datetime.now().replace(second=0, microsecond=0)

        # Открывается страница с добавленным только что ботом.
        # Пользователь видит название бота.
        header_text = self.browser.find_element(By.TAG_NAME, "h2").text
        self.assertEqual(header_text, TEST_TELEGRAM_BOT_NAME)

        # Пользователь видит статус бота.
        is_running_status = self.browser.find_element(By.ID, "is-running-status").text
        self.assertTrue(is_running_status == 'False')

        # Пользователь видит дату обновления статуса бота.
        bot_status_update_at = self.browser.find_element(By.ID, "bot-status-update-at").text
        bot_status_update_at = bot_status_update_at.replace("p.m.", "PM").replace("a.m.", "AM")
        bot_status_update_at = datetime.strptime(bot_status_update_at, "%b. %d, %Y, %I:%M %p")
        self.assertAlmostEqual(now_time, bot_status_update_at, delta=timedelta(seconds=3))

        # Пользователь видит время создания бота.
        created_at = self.browser.find_element(By.ID, "created-at").text
        created_at = created_at.replace("p.m.", "PM").replace("a.m.", "AM")
        created_at = datetime.strptime(created_at, "%b. %d, %Y, %I:%M %p")
        self.assertAlmostEqual(now_time, created_at, delta=timedelta(seconds=3))

        # Пользователь видит время обновления бота.
        updated_at = self.browser.find_element(By.ID, "updated-at").text
        updated_at = updated_at.replace("p.m.", "PM").replace("a.m.", "AM")
        updated_at = datetime.strptime(updated_at, "%b. %d, %Y, %I:%M %p")
        self.assertEqual(created_at, updated_at)

        # Пользователь нажимает на кнопку "Запустить".
        start_bot = self.browser.find_element(By.ID, "start-bot-btn").click()
