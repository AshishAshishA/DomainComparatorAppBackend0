from django.urls import path, include
from rest_framework import routers
from .views import DomainSuffixViewSet, DomainDetailViewSet, WebsiteNameViewSet, DomainDetailViewSetUnmodified,SearchedNameViewSet

router = routers.DefaultRouter()
router.register('websites', WebsiteNameViewSet ,basename='websiteList')
router.register('domains/suffix',DomainSuffixViewSet, basename='suffixList')
router.register('domains/details', DomainDetailViewSet, basename='domainList')
router.register('domains/details1', DomainDetailViewSetUnmodified, basename='domainList1')
router.register('domains/searched',SearchedNameViewSet,basename="searchedName")

urlpatterns = [
    path('', include(router.urls)),
    # path('domains/suffix/',DomainSuffixViewSet.as_view(),name="suffixList")
]