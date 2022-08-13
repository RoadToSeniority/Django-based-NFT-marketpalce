from unicodedata import name
from django.db import models
from enum import Enum
    
class NFT(models.Model):

    class NFTType(models.TextChoices):
        Picture = 'Picture'
        Voice = 'Voice'
        Gif = 'Gif'
        
    name = models.CharField(max_length=100)
    IpfsAddress = models.CharField(unique=True, max_length=100)
    NftType = models.CharField(max_length=100, choices=NFTType.choices)
    UpdatedAt = models.DateTimeField(auto_now=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    LastPrice = models.DecimalField(max_digits=6, decimal_places=2)

class Price(models.Model):
    IRL = models.DecimalField(max_digits=6, decimal_places=2)
    USD = models.DecimalField(max_digits=6, decimal_places=2)