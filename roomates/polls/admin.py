'''
Created on Jun 16, 2013

@author: vdelaluz
'''

from django.contrib import admin
from polls.models import Poll

admin.site.register(Poll)