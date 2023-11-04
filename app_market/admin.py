from django.contrib import admin
from .models import Client,Trade

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_id','name','brokerage','date']
    
@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ['client_id','name','exchange','symbol','rate','netrate','qty','amount','date','status']

    

