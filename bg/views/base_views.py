from django.shortcuts import render
from django.views import View
from bg.helper.bg_page_helper import PageHelper

import logging
log = logging.getLogger()


class BaseView(View):
    title = ""
    b_model = ""  # 隶属的管理模块
    headers = []
    page = ""  # 页面

    def search(self, page_helper: PageHelper):
        pass

    def get(self, request, *args, **kwargs):
        page_helper = PageHelper(request)
        page_helper["active_page"] = self.title
        page_helper["active"] = self.b_model
        page_helper["headers"] = self.headers
        page_helper["data_list"] = []
        self.search(page_helper)
        return render(request, self.page, context=page_helper)

    def post(self, request, *args, **kwargs):
        page_helper = PageHelper(request)
        page_helper["active_page"] = self.title
        page_helper["active"] = self.b_model
        page_helper["headers"] = self.headers
        page_helper["data_list"] = []
        self.search(page_helper)
        return render(request, self.page, context=page_helper)

