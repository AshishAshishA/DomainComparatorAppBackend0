from django.db import models

# Create your models here.
class SearchedName(models.Model):
    searchedName = models.CharField(max_length=250)
    searchFreq = models.IntegerField(default=1)
    totalSearchFreq = models.IntegerField(default=1)
    stayIndex = models.IntegerField(default=1)

    class Meta:
        ordering = ['-searchFreq','-totalSearchFreq']

    def __str__(self):
        return self.searchedName

class DomainSuffix(models.Model):
    suffix = models.CharField(max_length=20)

    def __str__(self):
        return self.suffix

class WebsiteName(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class DomainDetail(models.Model):
    domainName = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)


    domainSuffix = models.ForeignKey(DomainSuffix,related_name='domainDetail',on_delete=models.SET_NULL, blank=True, null=True)
    websiteName = models.ForeignKey(WebsiteName,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return f"{self.domainName}.{self.domainSuffix.suffix} {self.websiteName.name}"