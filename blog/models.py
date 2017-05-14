from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class CardType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    card_type = models.ForeignKey('CardType')
    image = models.ImageField(upload_to='images/')
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Checkbox(models.Model):
    title = models.CharField(max_length=50)
    card = models.ForeignKey('Card')
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ProjectCard(models.Model):
    title = models.CharField(max_length=110)
    project = models.ForeignKey('Project')
    card = models.ForeignKey('Card')
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class CardLink(models.Model):
    title = models.CharField(max_length=110)
    card_before = models.ForeignKey('Card',related_name='cards_before')
    card_after = models.ForeignKey('Card',related_name='cards_after')
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ProjectResource(models.Model):
    title = models.CharField(max_length=110)
    project = models.ForeignKey('Project')
    resource_card = models.ForeignKey('Card')
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ProjectResult(models.Model):
    title = models.CharField(max_length=110)
    project = models.ForeignKey('Project')
    result_card = models.ForeignKey('Card')
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class ProjectStep(models.Model):
    title = models.CharField(max_length=110)
    project = models.ForeignKey('Project')
    step_card = models.ForeignKey('Card')
    step_num = models.IntegerField()
    created_by = models.ForeignKey('auth.User')
    created_ts = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

