from django.db import models

class ExtractSign(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    file = models.FileField()
    scanned_file = models.FileField(null=True)

    def __str__(self):
        return f'{self.id} {self.file}'