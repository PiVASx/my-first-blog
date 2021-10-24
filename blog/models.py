from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Ссылка на другую модель.
    title = models.CharField(max_length=200)  # Текст с ограничением по симвалам 200
    text = models.TextField()  # Текст без ограничения
    created_date = models.DateTimeField(default=timezone.now)  # Дата время
    published_date = models.DateTimeField(blank=True, null=True)  # Дата время

    # ц
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title