from django.contrib import admin
from .models import Data,FormUser
# Register your models here.


class DataAdmin(admin.ModelAdmin):

    list_display = [
        "user",
        "temperature",
        "noise",
        "light",
        "date",


    ]
    list_display_links = [
        "user"
    ]

    class Meta:
        model = Data


class FormAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "content",
        "datetime",
    ]

    class Meta:
        model = FormUser


admin.site.register(Data,DataAdmin)
admin.site.register(FormUser,FormAdmin)


