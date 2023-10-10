from django.contrib import admin

from core.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['question_text', 'answer_text', 'id']
    list_filter = ['create_date', 'save_date']
