from django.contrib import admin

# Register your models here.
from . models import Property, propertyImage, Place, Category, PropertyReview, PropertyBook
admin.site.register(Property)
admin.site.register(propertyImage)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)