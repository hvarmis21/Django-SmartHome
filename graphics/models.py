from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Data(models.Model):
    temperature = models.IntegerField(verbose_name="Temperature")
    noise = models.IntegerField(verbose_name="Noise")
    light = models.IntegerField(verbose_name="Light")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = "Data"


class FormUser(models.Model):
    title = models.CharField(verbose_name="Title", max_length=140)
    content = models.TextField(verbose_name="Content")
    datetime = models.DateTimeField(verbose_name="Publishing Date", auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} {} {} {}".format(self.user, self.title, self.content, self.datetime)

    class Meta:
        verbose_name = "FormUser"
