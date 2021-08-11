from django.contrib import admin
from .models import *

# Register your models here.
class scoreAdmin(admin.ModelAdmin):
    list_display = ["name", "leader_board"]

admin.site.register(score, scoreAdmin)
admin.site.register(leaderBoard)
