from django.contrib import admin

# Register your models here.
from first_app.models import Name,Topic,WebPage

admin.site.register(Name)
admin.site.register(Topic)
admin.site.register(WebPage)
