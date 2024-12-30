from django.contrib import admin

from .models import Profile,Category,Item

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')  

admin.site.register(Profile, ProfileAdmin)
# Registering the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryname', 'description', 'created_at', 'updated_at')  
    search_fields = ('categoryname',)  
    list_filter = ('created_at',) 
    ordering = ('-created_at',) 

# Registering the Item model
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemname', 'category', 'quantity', 'price', 'sku', 'status', 'created_at')
    search_fields = ('itemname', 'sku') 
    list_filter = ('category', 'status', 'created_at') 
    ordering = ('-created_at',)  