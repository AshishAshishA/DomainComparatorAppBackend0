from .models import DomainSuffix, DomainDetail, WebsiteName, SearchedName
from rest_framework import serializers

class WebsiteNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteName
        fields = ['name']

class DomainSuffixSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainSuffix
        fields = ['suffix']

class DomainDetailSerializer(serializers.ModelSerializer):
    websiteName = WebsiteNameSerializer()
    domainSuffix = DomainSuffixSerializer()
    class Meta:
        model = DomainDetail
        fields = ['domainName','price','created_at','updated_at','websiteName','domainSuffix']
        read_only = ['created_at','updated_at']

    def create(self,validated_data):
        websiteName = validated_data.pop('websiteName').get('name')
        suffix = validated_data.pop('domainSuffix').get('suffix')
        domainName = validated_data.get('domainName')
        price = validated_data.get('price')
        
        try:
            wbNameInstance = WebsiteName.objects.get(name__iexact=websiteName)
        except:
            wbNameInstance = WebsiteName.objects.create(name=websiteName)
        
        try:
            suffixInstance = DomainSuffix.objects.get(suffix__iexact=suffix)
        except:
            suffixInstance = DomainSuffix.objects.create(suffix=suffix)

        try:
            domainDetailInstance = DomainDetail.objects.get(domainName__iexact=domainName, websiteName=wbNameInstance,domainSuffix=suffixInstance)
            domainDetailInstance.price = price
            domainDetailInstance.save()
        except:
            domainDetailInstance = DomainDetail.objects.create(**validated_data,websiteName=wbNameInstance,domainSuffix=suffixInstance)
            
        return domainDetailInstance


class DomainSuffixSerializerwithDetail(serializers.ModelSerializer):
    domainDetail = DomainDetailSerializer(many=True, read_only=True)
    class Meta:
        model = DomainSuffix
        fields = ['suffix','domainDetail']

class SearchedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchedName
        fields = ['searchedName','searchFreq','totalSearchFreq','stayIndex']
        read_only_fields = ['totalSearchFreq']

    def create(self, validated_data):
        print(validated_data)
        searchedName = validated_data.pop('searchedName')
        searchFreq = validated_data.pop('searchFreq')
        stayIndex = validated_data.pop('stayIndex')

        try:
            searchedNameInstance = SearchedName.objects.get(searchedName__iexact=searchedName)
            if searchFreq == 0:
                searchedNameInstance.searchFreq = 0
            else:

                searchedNameInstance.searchFreq += 1
                searchedNameInstance.totalSearchFreq += 1

            if stayIndex != 2:
                searchedNameInstance.stayIndex =stayIndex

            searchedNameInstance.save()
            
        except SearchedName.DoesNotExist:
            searchedNameInstance = SearchedName.objects.create(searchedName=searchedName)
        
        return searchedNameInstance

    