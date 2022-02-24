from django.db import models
from django.contrib.auth.models import User

class Crypto(models.Model):
    crypto_ticker = models.CharField(max_length=8)
    sell_price = ...
    buy_price = ...
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coins', null=True, blank=True)  # request.user inside views is the user
    # request.user.crypto_set.all() all coins user is interested in
    # request.user.coins.all()
    def __str__(self):
        return self.crypto_ticker
# Create your models here.
