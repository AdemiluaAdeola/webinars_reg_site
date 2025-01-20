from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Webinar)
admin.site.register(Registration)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(Blog)