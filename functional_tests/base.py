import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from django.contrib.staticfiles.testing import StaticLiveServerTestCase


MAX_WAIT = 5


def wait(fn):
	def modified_fn(*args, **kwargs):
		start_time = time.time()
		while True:
			try:
				return fn(*args, **kwargs)
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)
	return modified_fn



class FunctionalTest(StaticLiveServerTestCase):
	"""Методы и атрибуты для работы с функциональными тестами."""


	def setUp(self):
		"""Создание сеанса браузера для работы функциональных тестов."""
		self.browser = webdriver.Chrome()


	def tearDown(self):
		"""Выключение сеанса браузера."""
		self.browser.quit()
