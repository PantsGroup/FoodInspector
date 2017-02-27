from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from .models import Restaurant, Address

from tastypie.authentication import BasicAuthentication, SessionAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization, ReadOnlyAuthorization, Authorization
from tastypie.resources import ModelResource

from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.http import HttpUnauthorized, HttpForbidden, HttpApplicationError
from tastypie.resources import Resource, ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash
from tastypie.bundle import Bundle
from tastypie import fields
from tastypie.models import ApiKey, create_api_key
from django.contrib.auth import authenticate, login, logout

import logging
logger = logging.getLogger()

import json
#import urllib.parse
#import urllib.parse
#from urlparse import urlparse
#from urllib.parse import urlparse
import urlparse
from tastypie.serializers import Serializer
from tastypie.exceptions import Unauthorized, ImmediateHttpResponse
from tastypie import http

class urlencodeSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'urlencode']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'urlencode': 'application/x-www-form-urlencoded',
        #'multipart': 'multipart/form-data',
        }
    def from_urlencode(self, data,options=None):
        """ handles basic formencoded url posts """
        qs = dict((k, v if len(v)>1 else v[0] )
            for k, v in urlparse.parse_qs(data).iteritems())
        return qs

    def to_urlencode(self,content): 
        pass

    def format_date(self, data):
        return data.strftime("%d-%m-%Y")


class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurant'
        authorization = Authorization()
        serializer = urlencodeSerializer() # IMPORTANT
        #serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'plist'])
        filtering = {
            'business_name': ['ALL','exact','startswith','endswith'],
        }
        limit = 0
        always_return_data = True

class AddressResource(ModelResource):
    class Meta:
        queryset = Address.objects.all()
        resource_name = 'address'
        authorization = Authorization()
        serializer = urlencodeSerializer() # IMPORTANT
        #serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'plist'])
        filtering = {
            'business_name': ['ALL','exact','startswith','endswith'],
        }
        limit = 0
        always_return_data = True