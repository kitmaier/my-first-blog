from django.contrib import admin
from .models import Post, Card, Checkbox, CardType, Project, ProjectCard, CardLink, ProjectResource, ProjectResult, ProjectStep

admin.site.register(Post)
admin.site.register(Card)
admin.site.register(Checkbox)
admin.site.register(CardType)
admin.site.register(Project)
admin.site.register(ProjectCard)
admin.site.register(CardLink)
admin.site.register(ProjectResource)
admin.site.register(ProjectResult)
admin.site.register(ProjectStep)