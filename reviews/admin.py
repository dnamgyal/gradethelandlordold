from django.contrib import admin

from .models import Landlord, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('landlord', 'rating', 'user_name', 'comment','communication', 'rent_again', 'address', 'apt_condition', 'maintenance_eff', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Landlord)
admin.site.register(Review, ReviewAdmin)
