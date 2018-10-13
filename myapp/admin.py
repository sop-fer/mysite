from django.contrib import admin
from myapp.models import student
# Register your models here.

class studentadmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return 'girl'
        else:
            return 'boy'
    list_display = ['sname','sage',gender,'scontent']
    list_filter = ['sgender']
    

admin.site.register(student, studentadmin)