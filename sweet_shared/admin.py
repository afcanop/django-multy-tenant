from django.contrib import admin

# Register your models here.
from sweet_shared.models import SweetType

@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)