from unicodedata import name
from django.db import models
from enum import Enum

class TypeNFT(Enum):
    Picture, Voice, Gif = 1, 2, 3
    
class NFT(models.Model):
    name = models.CharField(max_length=100)
    IpfsAddress = models.CharField(unique=True, max_length=100)
    UpdatedAt = models.DateTimeField()
    CreatedAt = models.DateTimeField()
    LastPrice = models.IntegerField()

class Price(models.Model):
    IRL = models.FloatField(max_length=100)
    USD = models.FloatField(max_length=100)