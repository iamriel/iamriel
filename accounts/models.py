from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    title = models.CharField(max_length=100, blank=True)
    information = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    google_plus_url = models.URLField(blank=True)
    linked_in_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, through='UserSkill')

    def __str__(self):
        return self.user.get_full_name()

    @property
    def top_skills(self):
        return self.userskill_set.order_by('-percent')[:3]

    @property
    def other_skills(self):
        return self.skills.exclude(id__in=self.top_skills.values_list('skill', flat=True))


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    website_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Experience(models.Model):
    user = models.ForeignKey(User, related_name='experiences')
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return '{} - {}'.format(self.user, self.company)


class UserSkill(models.Model):
    LEVEL_ADVANCED = 'advanced'
    LEVEL_EXPERT = 'expert'
    LEVEL_INTERMEDIATE = 'intermediate'

    LEVEL_CHOICES = (
        (LEVEL_ADVANCED, 'Advanced'),
        (LEVEL_EXPERT, 'Expert'),
        (LEVEL_INTERMEDIATE, 'Intermediate'),
    )

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(help_text='Number of years.', blank=True, null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default=LEVEL_INTERMEDIATE)
    percent = models.FloatField(default=0.0)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('profile', 'skill', )

    def __str__(self):
        return '{} - {}'.format(self.profile, self.skill)

    @property
    def title(self):
        return self.skill.title
