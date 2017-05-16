from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100, blank=True)
    information = models.TextField(blank=True)
    linked_in_url = models.URLField(blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.user, self.company)


class Skill(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TopSkill(models.Model):
    LEVEL_ADVANCED = 'advanced'
    LEVEL_EXPERT = 'expert'
    LEVEL_INTERMEDIATE = 'intermediate'

    LEVEL_CHOICES = (
        (LEVEL_ADVANCED, 'Advanced'),
        (LEVEL_EXPERT, 'Expert'),
        (LEVEL_INTERMEDIATE, 'Intermediate'),
    )

    user = models.ForeignKey(User)
    skill = models.ForeignKey(Skill)
    duration = models.PositiveIntegerField(help_text='Number of years.')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default=LEVEL_INTERMEDIATE)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'skill', )

    def __str__(self):
        return '{} - {}'.format(self.user, self.skill)
