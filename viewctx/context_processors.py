#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

def view(request):
    return {
        'view': dict(
            view_name = request.view_name,
            kwargs = request.view_kwargs
        )
    }
