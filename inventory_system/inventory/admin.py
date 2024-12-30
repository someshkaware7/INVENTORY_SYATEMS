from django.contrib import admin

from .models import Profile 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')  

admin.site.register(Profile, ProfileAdmin)
