from django.contrib import admin
from .models import Box, Activity, RFID, Item, User

admin.site.register(Box)
admin.site.register(RFID)
admin.site.register(Activity)
admin.site.register(Item)
admin.site.register(User)
