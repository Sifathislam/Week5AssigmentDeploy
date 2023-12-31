from django.contrib import admin
from . models import Book,review,Purcehase_history

# Register your models here.
admin.site.register(Book)
admin.site.register(review)
admin.site.register(Purcehase_history)