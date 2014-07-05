from django.contrib import admin
from dblog.models import *

class PostAdmin(admin.ModelAdmin):
    change_form_template = 'dblog/admin/change_form.html'

admin.site.register(dblog_Post, PostAdmin)
admin.site.register(dblog_Tag)
admin.site.register(dblog_Author)