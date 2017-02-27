from django.contrib import admin

# Register your models here.
from .models import Restaurant, Address

class AddressAdmin(admin.ModelAdmin):
      list_display = ('business_name','address','latitude','longitude','latlng','timestamp')
      search_fields = ('business_name','address','latitude','longitude','latlng','timestamp')
      list_per_page = 50 # No of records per page


admin.site.register(Restaurant)
admin.site.register(Address,AddressAdmin)