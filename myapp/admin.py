from django.contrib import admin
from .models import QuestionTian as Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_txt']}),
        ('Date information',{'fields':['pub_data'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_txt','pub_data')
    list_filter = ['pub_data']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)

# Register your models here.
