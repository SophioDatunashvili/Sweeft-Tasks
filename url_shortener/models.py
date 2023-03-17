import random
import string
from django.db import models


class URL(models.Model):
    url = models.URLField(max_length=250)
    short_name = models.CharField(max_length=20, unique=True, blank=True)
    is_premium_client = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Generate a random short_name if not provided
        if not self.short_name:
            short_name_length = 10  # You can set the desired length
            self.short_name = ''.join(random.choices(string.ascii_letters + string.digits, k=short_name_length))

            # Ensure the generated short_name is unique
            while URL.objects.filter(short_name=self.short_name).exists():
                self.short_name = ''.join(random.choices(string.ascii_letters + string.digits, k=short_name_length))

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.url} -> {self.short_name}'
