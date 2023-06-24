from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from user_auth.models import UserProfile, UserLocation
from payment_management.models import Wallet
# Create your models here.

class FakeWallet(models.Model):
    password = models.CharField(max_length=30)
    person = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='fwallet')
    history = models.TextField(null=True, blank=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=1000.00)

class Txn(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sender = models.ForeignKey(FakeWallet, on_delete=models.CASCADE, related_name='txn')
    recipient = models.ForeignKey(FakeWallet, on_delete=models.CASCADE, related_name='pay')

user = UserProfile
@receiver(post_save, sender = user)
def creation_handling(sender, instance, created, *args, **kwargs):
    if created:
        print('A new User')
        newWallet = FakeWallet.objects.create(password = instance.password, person= instance )
        newWallet.save()
    else:
        print('Nothing special')

# @receiver(pre_save, sender=Txn)
# def fwallet_presave(sender, instance,*args, **kwargs):
#     if instance.sender is None:
#         instance.sender = 
#     bal = FakeWallet.objects.get(person=instance.sender)
#     if instance.amount< bal:
        
#         bal -= instance.amount
#         bal.save()
#     else:
#         print('Insufficient balance')