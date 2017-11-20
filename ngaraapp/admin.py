from django.contrib import admin
from ngaraapp.models import Index
from ngaraapp.models import About
from ngaraapp.models import Service
from ngaraapp.models import Contact
# from ngaraapp.models import Form

# Register your models here.

admin.site.register(Index)
admin.site.register(About)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

# @admin.register(Login)
# class LoginAdmin(admin.ModelAdmin):
#     pass
# Register the admin class with the associated model
# admin.site.register(Contact, ContactAdmin)
