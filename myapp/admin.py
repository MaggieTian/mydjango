from django.contrib import admin
from .models import Question,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_txt']}),
        ('Date information',{'fields':['pub_data'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question,QuestionAdmin)

# Register your models here.
