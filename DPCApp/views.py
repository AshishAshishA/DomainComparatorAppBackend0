from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .models import DomainSuffix, DomainDetail, WebsiteName, SearchedName
from .serializers import DomainSuffixSerializer, DomainDetailSerializer, WebsiteNameSerializer, SearchedNameSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class WebsiteNameViewSet(viewsets.ModelViewSet):
    queryset = WebsiteName.objects.all()
    serializer_class = WebsiteNameSerializer

class DomainDetailViewSetUnmodified(viewsets.ModelViewSet):
    queryset = DomainDetail.objects.all()
    serializer_class = DomainDetailSerializer

class DomainDetailViewSet(viewsets.ModelViewSet):
    # queryset = DomainDetail.objects.all()
    serializer_class = DomainDetailSerializer

    def get_queryset(self):
        suffix = self.request.query_params.get("suffix")
        domainName = self.request.query_params.get("domainName").strip()
        domain_detail_object = []

        suffix_object = DomainSuffix.objects.filter(suffix=suffix)

        if suffix_object and domainName != "":
            domain_detail_object = DomainDetail.objects.filter(domainName__icontains = domainName, domainSuffix=suffix_object[0])
        return domain_detail_object

class DomainSuffixViewSet(viewsets.ModelViewSet):
    queryset = DomainSuffix.objects.all()
    serializer_class = DomainSuffixSerializer

    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ["suffix"]

    def get_queryset(self):
        domainName = self.request.query_params.get("domainName")

        domain_suffix_set = set()

        domain_suffix_object = DomainSuffix.objects.filter(domainDetail__domainName__icontains = domainName)
        domain_suffix_set = {i for i in domain_suffix_object}
        domain_suffix_list = [i for i in domain_suffix_set]
        return domain_suffix_list

class SearchedNameViewSet(viewsets.ModelViewSet):
    queryset = SearchedName.objects.all()
    serializer_class = SearchedNameSerializer
