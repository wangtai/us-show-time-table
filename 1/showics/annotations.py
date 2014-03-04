#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (cn.wang.tai@gmail.com)

"""
annotation for views
"""

__revision__ = '0.1'

import sys
import functools
import json

from django.conf.urls import *
from django.http import HttpResponse, HttpResponseRedirect

strlist = 'strlist'
intlist = 'intlist'

def login_required(is_ajax=False, access_token=None, login_page=''):
    def paramed_decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            request = args[0]
            if not request.user.is_authenticated() \
                    and not (access_token != None and access_token != '' and access_token == request.GET.get(
                            'access_token', '')):
                if not is_ajax:
                    return HttpResponseRedirect(login_page)
                else:
                    return HttpResponse(json.dumps({'rt': False, 'info': 'login first'}));
            return func(*args, **kwargs)

        return decorated

    return paramed_decorator


def to_url(url_pattern, *args, **kwargs):
    def paramed_decorator(func):
        @functools.wraps(func)
        def decorated(self):
            return func(self)

        module = sys.modules[func.__module__]
        if not hasattr(module, 'urlpatterns'):
            module.urlpatterns = patterns('', )

        module.urlpatterns += patterns('', url(url_pattern, decorated, *args, **kwargs), )
        return decorated

    return paramed_decorator


def _param(method_name, *p_args, **p_kwargs):
    '''
    @get('param1', 'param2')
    @get(param1={'name':'parameter_name', 'type':int, 'default':0})
    @get(param1={'type':int, 'default':0})
    @get(param1={'type':int })
    @get(param1=('param_name', int, 0))
    @get(param1=(int, 0))
    @get(param1=int)
    '''

    def paramed_decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            request = args[0]
            m = {'get': request.GET, 'post': request.POST, 'param': request.REQUEST}
            method = m[method_name]
            for k, v in p_kwargs.items():
                _name = None;
                _type = None;
                _default = None;

                if type(v) == str:
                    _type = str
                    _name = v
                elif type(v) == dict:
                    if v.has_key('name'):
                        _name = v['name']
                    if v.has_key('type'):
                        _type = v['type']
                    if v.has_key('default'):
                        _default = v['default']
                elif type(v) == tuple and len(v) == 3:
                    _name = v[0]
                    _type = v[1]
                    _default = v[2]
                elif type(v) == tuple and len(v) == 2:
                    _type = v[0]
                    _default = v[1]
                elif type(v) == type:
                    _type = v

                if _name == None:
                    _name = k
                if _type == None:
                    _type = str

                has_key = True
                try:
                    origin_v = method[_name].encode('utf-8').strip()
                    if len(origin_v) == 0:
                        has_key = False
                except:
                    has_key = False

                if has_key:
                    if _type == bool:
                        origin_v = origin_v.lower()
                        if origin_v == 'false' or origin_v == '0':
                            value = False
                        elif origin_v == 'true':
                            value = True
                        else:
                            value = bool(origin_v)
                    elif _type == strlist:
                        value = []
                        for item in origin_v.split(','):
                            if len(item) > 0:
                                value.append(item)
                    elif _type == intlist:
                        value = []
                        for item in origin_v.split(','):
                            try:
                                value.append(int(item))
                            except:
                                pass
                    else:
                        value = _type(origin_v)
                else:
                    if _default != None:
                        value = _default
                    else:
                        return HttpResponse(
                            json.dumps({'rt': False, 'info': 'Please specify the parameter : ' + _name}))
                kwargs.update({k: value})

            for k in p_args:
                try:
                    kwargs.update({k: method[k].encode('utf-8')})
                except:
                    return HttpResponse(json.dumps({'rt': False, 'info': 'Please specify the parameter : ' + k}))
            return func(*args, **kwargs)

        return decorated

    return paramed_decorator


def get(*p_args, **p_kwargs):
    """
    @get('param1', 'param2')
    @get(param1={'name':'parameter_name', 'type':int, 'default':0})
    @get(param1={'type':int, 'default':0})
    @get(param1={'type':int })
    @get(param1=('param_name', int, 0))
    @get(param1=(int, 0))
    @get(param1=int)
    """
    return _param('get', *p_args, **p_kwargs)


def post(*p_args, **p_kwargs):
    '''
    @post('param1', 'param2')
    @post(param1={'name':'parameter_name', 'type':int, 'default':0})
    @post(param1={'type':int, 'default':0})
    @post(param1={'type':int })
    @post(param1=('param_name', int, 0))
    @post(param1=(int, 0))
    @post(param1=int)
    '''
    return _param('post', *p_args, **p_kwargs)


def param(*p_args, **p_kwargs):
    return _param('param', *p_args, **p_kwargs)