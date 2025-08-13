from django.contrib import admin
from .models import Booking, MenuItem

admin.site.site_header = "Little Lemon Admin"
admin.site.site_title = "Little Lemon Admin Portal"
admin.site.index_title = "Welcome to Little Lemon Restaurant Portal"
# Register your models here.



admin.site.register(Booking)
admin.site.register(MenuItem)
