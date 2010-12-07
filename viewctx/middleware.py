#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

class ViewMiddleware(object):
    def process_view(self, request, view, args, kwargs):
        """Enriches the request object with the view name, args and kwargs"""
        request.view_name = ".".join((view.__module__, view.__name__))
        request.view_args = args
        request.view_kwargs = kwargs
        return None

