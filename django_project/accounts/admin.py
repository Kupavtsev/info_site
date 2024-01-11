from django.contrib import admin
from .models import Account


class AccountAdmin( admin.ModelAdmin ):
    list_display        = ( 'username', 'email', 'last_login', 'date_joined' )
    list_display_links  = ( 'username', 'email', 'date_joined' )
    search_fields       = ( 'username', 'email' )

admin.site.register( Account, AccountAdmin )