import time

from selenium.webdriver.common.by import By

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
		self.browser.find_element(By.LINK_TEXT, "Telegram").click()

		# Проверяет, что URL изменился на страницу Telegram.
		self.assertIn("/telegram", self.browser.current_url)

		# Проверяет, что на странице Telegram есть заголовок с названием платформы.
		header_text = self.browser.find_element(By.TAG_NAME, "h2").text
		
		# Нарек нажимает на кнопку "Подключить бота" для автоматизации.
		self.browser.find_element(By.LINK_TEXT, 'Подключить бота').click()
