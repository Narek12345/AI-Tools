from django.contrib.staticfiles.testing import StaticLiveServerTestCase



class FunctionalTest(StaticLiveServerTestCase):
	"""Методы и атрибуты для работы с функциональными тестами."""


	def setUp(self):
		"""Создание сеанса браузера для работы функциональных тестов."""
		self.browser = webdriver.Chrome()


	def tearDown(self):
		"""Выключение сеанса браузера."""
		self.browser.quit()
