from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auction(models.Model):

    title = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Competitor(models.Model):

    auction = models.ForeignKey(Auction)
    bid = models.PositiveIntegerField()
    bid_owner = models.ForeignKey(User)
    bid_comment = models.CharField(max_length=75)
    bid_ip = models.GenericIPAddressField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bid)

