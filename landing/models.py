from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    passwordMatch = models.CharField(max_length=256)

    def __str__(self):
        return "%s %s %s" % (self.id, self.name, self.email)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'