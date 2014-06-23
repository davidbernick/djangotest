from django.contrib import admin
from .models import Task,Category
from guardian.admin import GuardedModelAdmin

class TaskAdmin(GuardedModelAdmin):
    pass

class CategoryAdmin(GuardedModelAdmin):
    pass

admin.site.register(Task,TaskAdmin)
admin.site.register(Category,CategoryAdmin)
# Register your models here.
