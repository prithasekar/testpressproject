from django.contrib import admin
from .models import Question
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['question','option1','option2','option3','option4','crtanswer']
admin.site.register(Question)
