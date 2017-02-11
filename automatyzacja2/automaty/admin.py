from django.contrib import admin
from .models import Wygrzewanie
from .models import Konta_Testowe


class WygrzewanieAdmin(admin.ModelAdmin):
    list_display=('title','titleClass','author','type_stb','test_Status')
    list_filter=('type_stb','test_Status')
    search_field=('title','titleClass','author','type_stb','test_Status')
admin.site.register(Wygrzewanie,WygrzewanieAdmin)
# Register your models here.

class Konta_TestoweAdmin(admin.ModelAdmin):
    list_display=('accountNumber','terminalNumbers','technology','accountStatus')
    list_filter=('terminalNumbers','technology','accountStatus')
admin.site.register(Konta_Testowe,Konta_TestoweAdmin)