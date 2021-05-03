from django.contrib import admin

from .models import Education, Resume, Skill, WorkExperience

# Register your models here.


class SkillInline(admin.TabularInline):
    model = Skill

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class EducationInline(admin.StackedInline):
    model = Education

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
        WorkExperienceInline,
        EducationInline,
    ]
