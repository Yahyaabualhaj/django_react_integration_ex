from django.db import models
from django.contrib.auth.models import User


class Vacation(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)

    date_from = models.DateField()
    date_to = models.DateField()
    comments = models.CharField(max_length=200)
    status = models.CharField(null=True, blank=True, max_length=200, )

    def __str__(self):
        return '  |From : ' + \
               str(self.date_from) + ' |To: ' + \
               str(self.date_to)