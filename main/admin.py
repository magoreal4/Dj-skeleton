from django.contrib import admin

from solo.admin import SingletonModelAdmin
from main.models import SiteConfiguration, Alcance


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Alcance)


