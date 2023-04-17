from django.contrib import admin
from .models import AddpostModel , add_question
 
# @admin.register(AddpostModel)
@admin.register(add_question)
class ClientPost(admin.ModelAdmin):
   pass

