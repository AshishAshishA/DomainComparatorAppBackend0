from django.contrib import admin
from .models import DomainSuffix, DomainDetail, WebsiteName,SearchedName

# Register your models here.
admin.site.register(DomainSuffix)
admin.site.register(DomainDetail)
admin.site.register(WebsiteName)
admin.site.register(SearchedName)