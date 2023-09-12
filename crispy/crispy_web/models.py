from django.db import models

class Tray(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    bar_code = models.TextField(max_length=48)

    def __str__(self):
        return(f"{self.bar_code}")