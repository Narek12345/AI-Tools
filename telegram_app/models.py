from django.db import models



class TelegramBot(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	token = models.CharField(max_length=100, unique=True, blank=False, null=False)
	is_running = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	class Meta:
		db_table = 'telegram_bot'


	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)
