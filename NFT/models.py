from django.db import models
from django.contrib.auth import get_user_model

# Register your models here.

user = get_user_model()
    
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
    owner = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class Price(models.Model):
    IRL = models.DecimalField(max_digits=6, decimal_places=2)
    USD = models.DecimalField(max_digits=6, decimal_places=2)