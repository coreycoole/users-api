from django.db import models

class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    last_login = models.DateTimeField()
    login_count = models.IntegerField()
    project_count = models.IntegerField()

    def get_users(self):
        return self.id

    def __str__(self):
        return self.id
