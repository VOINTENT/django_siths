from django.contrib import admin

from .models import Recruit, Planet, Test_h_s, Question, Answer, Sith


class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )


class SithAdmin(admin.ModelAdmin):
    list_display = ('name', 'planet', 'count_h_s', )
    list_display_links = ('name', )
    search_fields = ('name', )

class Test_h_sAdmin(admin.ModelAdmin):
    list_display = ('code', )
    list_display_links = ('code', )
    search_fields = ('code', )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'code', )
    list_display_links = ('text', )
    search_fields = ('text', )

# class RecruitAdmin(admin.ModelAdmin):
#     list_display = ('name', 'planet', 'age', 'email', 'is_passed', 'is_h_s', )
#     list_display_links = ('name', )
#     search_fields = ('name', )
#
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer', 'recruit', )
#     list_display_links = ('question', 'answer', )
#     search_fields = ('question', 'answer', )


admin.site.register(Planet, PlanetAdmin)
admin.site.register(Sith, SithAdmin)
admin.site.register(Test_h_s, Test_h_sAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Recruit, RecruitAdmin)
# admin.site.register(Answer, AnswerAdmin)
