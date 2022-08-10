from django.shortcuts import render
from bg.helper.bg_page_helper import PageHelper

import logging
log = logging.getLogger()


def index(request):
    context = PageHelper(request)
    return render(request, 'index.html', context=context)



