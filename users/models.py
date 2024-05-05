from django.db import models

class UserModel(models.Model):
    full_name = models.CharField(max_length=128)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=13)

    email = models.EmailField()
    region = models.CharField(max_length=20)
    certificate = models.FileField(upload_to="media/certificates", null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'