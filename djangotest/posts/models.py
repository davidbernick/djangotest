from django.db import models
from django.contrib.auth.models import User,Group
from guardian.shortcuts import assign_perm,remove_perm

class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        permissions = (
            ('view_category', 'View Category'),
        )

    def __unicode__(self):
        return self.name

class Task(models.Model):
    summary = models.CharField(max_length=32)
    content = models.TextField()
    reported_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category,related_name='category',blank=True,null=True)

    def __unicode__(self):
        return "%s (%s)" % (self.summary,self.created_at)


    class Meta:
        permissions = (
            ('view_task', 'View task'),
            ('curate_category','Curate category'),
        )
# Create your models here.
