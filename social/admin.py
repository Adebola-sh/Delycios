from django.contrib import admin
from .models import FakeWallet, Txn

# Register your models here.
admin.site.register(FakeWallet)
admin.site.register(Txn)