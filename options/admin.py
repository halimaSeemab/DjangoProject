from django.contrib import admin
from .models import list
from .models import LM

from .models import WH



class listAdmin(admin.ModelAdmin):
  list_display = ("book", "writer",)
  
admin.site.register(list,listAdmin)

admin.site.register(LM, listAdmin)
admin.site.register(WH, listAdmin)
