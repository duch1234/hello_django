from django.contrib import admin
from .models import Wygrzewanie



class WygrzewanieAdmin(admin.ModelAdmin):
    list_display=('title','titleClass','author','type_stb','test_Status')
    list_filter=('type_stb','test_Status')
admin.site.register(Wygrzewanie,WygrzewanieAdmin)
# Register your models here.
