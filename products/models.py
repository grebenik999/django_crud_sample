from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(
        upload_to='images/', default='defaul.jpg')
    icon = models.ImageField(
        upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
