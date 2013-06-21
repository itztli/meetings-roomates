'''
Created on Jun 16, 2013

@author: vdelaluz
'''

from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

#admin.site.register(Poll)



class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)

