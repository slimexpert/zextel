from django.contrib import admin
# Register your models here.
from .models import new, job, document

class NewsAdmin(admin.ModelAdmin):
	list_display = ('new_title', 'new_title_text', 'pub_date', 'pub_main', 'new_like',)

class JobsAdmin(admin.ModelAdmin):
	list_display = ('job_title', 'job_show',)

class DocumentsAdmin(admin.ModelAdmin):
	list_display = ('doc_title', 'doc_path', 'doc_pub', 'doc_show',)


admin.site.register(new, NewsAdmin)
admin.site.register(job, JobsAdmin)
admin.site.register(document, DocumentsAdmin)
