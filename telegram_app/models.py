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

        if self.id:
            prev_instance = TelegramBot.objects.get(id=self.id)
            if prev_instance.is_running != self.is_running:
                TelegramBotStatus.objects.create(bot=self, is_running=self.is_running)

        super().save(*args, **kwargs)



class TelegramBotStatus(models.Model):
    bot = models.ForeignKey(TelegramBot, on_delete=models.CASCADE)
    is_running = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
