from selenium.webdriver.common.by import By

from .base import FunctionalTest



class NewVisitorTest(FunctionalTest):


	def test_whatsapp_platform(self):
		"""Тест: пользователь хочет прочитать больше о автоматизации в WhatsApp."""

		# Пользователь решает открыть главную страницу сайта.
		self.browser.get(self.live_server_url)

		# Проверяет, что заголовок содержит "AI-Tools".
		self.assertIn("AI-Tools", self.browser.title)

		# Проверяет, что в шапке есть "AI-Tools".
		header_text = self.browser.find_element(By.TAG_NAME, "h1").text
		self.assertIn("AI-Tools", header_text)

		# Находит ссылку "WhatsApp" и кликает по ней.
		whatsapp_link = self.browser.find_element(By.LINK_TEXT, "WhatsApp")
		self.browser.execute_script("arguments[0].click();", whatsapp_link)

		# Открылась страница "Нет функциональности".
		header_text = self.browser.find_element(By.TAG_NAME, "h2").text
		self.assertIn("Функциональность в разработке!", header_text)
