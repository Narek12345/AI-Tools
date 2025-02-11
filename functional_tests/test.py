from selenium.webdriver.common.by import By

from .base import FunctionalTest



class NewVisitorTest(FunctionalTest):
	"""Тест нового посетителя."""


	def test_telegram_platform(self):
		"""Тест: пользователь хочет прочитать больше о автоматизации в Telegram."""

		# Нарек решает открыть главную страницу сайта.
		self.browser.get(self.live_server_url)

		# Он видит, что заголовок и шапка страницы состоят из "AI-Tools".
		self.assertIn('AI-Tools', self.browser.title)
		header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
		self.assertIn('AI-Tools', header_text)

		# Дальше он листает вниз и находит информацию о платформах и решает перейти на платформу Telegram.
		self.browser.find_element(By.LINK_TEXT, 'Telegram').click()

		# Он видит информацию о платформе Telegram.
