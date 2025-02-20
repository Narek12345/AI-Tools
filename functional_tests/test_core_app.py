import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base import FunctionalTest


TEST_TELEGRAM_BOT_TOKEN = os.getenv("TEST_TELEGRAM_BOT_TOKEN")



class test_back_button(FunctionalTest):


    def test_simple_back_button(self):
        """Тест: пользователь видит кнопку 'Назад' и хочет протестировать его."""

        # Пользователь открывает главную страницу.
        self.browser.get(self.live_server_url)

        # Решает перейти в приложение Telegram.
        telegram_link = self.browser.find_element(By.LINK_TEXT, 'Telegram')
        self.browser.execute_script("arguments[0].click();", telegram_link)

        # Дальше пользователь нажимает на кнопку "Подключить бота", заполнив поля. После создания бота идет автоматическое перенаправление на страницу с ботом.
        self.browser.find_element(By.LINK_TEXT, 'Подключить бота').click()
        bot_name_field = self.browser.find_element(By.NAME, "name")
        bot_name_field.send_keys("Telegram bot")
        bot_token_field = self.browser.find_element(By.NAME, "token")
        bot_token_field.send_keys(TEST_TELEGRAM_BOT_TOKEN)
        bot_token_field.send_keys(Keys.ENTER)

        # Затем пользователь решает нажать на кнопку "Назад". Он переходит на страницу с кнопкой "Подключить бота".
        self.browser.find_element(By.ID, "btn-back").click()
        header_text = self.browser.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Telegram", header_text)

        # Затем пользователь еще раз нажимает на кнопку "Назад". Теперь пользователь на главной странице сайта.
        self.browser.find_element(By.ID, "btn-back").click()
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("AI-Tools", header_text)



class TestInDevelopmentPage(FunctionalTest):


    def test_subscribe_to_telegram_channel(self):
        """Тест: проверяет переход пользователя на Telegram-канал после нажатия на кнопку подписки."""

        # Открываем страницу "Функциональность в разработке"
        self.browser.get(f"{self.live_server_url}/in_development")

        # Запоминаем текущую вкладку
        original_window = self.browser.current_window_handle

        # Находим и кликаем по кнопке "Подписаться на канал"
        self.browser.find_element(By.LINK_TEXT, "Подписаться на канал").click()

        # Ожидаем появления новой вкладки
        WebDriverWait(self.browser, 10).until(lambda d: len(d.window_handles) > 1)

        # Переключаемся на новую вкладку
        new_window = [window for window in self.browser.window_handles if window != original_window][0]
        self.browser.switch_to.window(new_window)

        # Ожидаем загрузки страницы Telegram
        WebDriverWait(self.browser, 10).until(EC.url_contains("t.me"))

        # Проверяем, что пользователь перешел на нужный канал
        expected_url = "https://t.me/ai_tools_channel"
        self.assertTrue(self.browser.current_url.startswith(expected_url))
