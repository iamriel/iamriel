from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import (
    Company,
    Experience,
    Skill,
    UserProfile,
    UserSkill,
)


class SkillInline(admin.TabularInline):
    model = UserSkill
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'profile'


class CustomUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
        ExperienceInline,
    ]


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    inlines = [
        SkillInline,
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserSkill)
