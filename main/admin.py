from django.contrib import admin
from .models import Question
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "choice1",
                    "choice2", "choice3", "choice4", "answer")

    list_filter = ["domain"]

    search_fields = ["question"]


admin.site.register(Question, QuestionAdmin)
