from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import (
    Company,
    Education,
    Email,
    Experience,
    School,
    Skill,
    Testimonial,
    UserProfile,
    UserSkill,
)


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


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class SkillInline(admin.TabularInline):
    model = UserSkill
    extra = 1


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    inlines = [
        EducationInline,
        SkillInline,
        TestimonialInline,
    ]


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Company)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(School)
admin.site.register(Skill)
admin.site.register(Testimonial)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserSkill)
