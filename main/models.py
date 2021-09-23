from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        verbose_name = "User information"
        verbose_name_plural = "User information"

class To_doLists(models.Model):
    title = models.CharField(max_length=200)
    to_do = models.TextField()
    date = models.DateField(auto_now_add=True)
    user_name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Todo list"
        verbose_name_plural = "Todo lists"