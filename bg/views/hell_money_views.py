from django.contrib import messages
from django.shortcuts import render
from bg.config.menu import register_model
from bg.helper.bg_page_helper import PageHelper
from bg.views.base_views import BaseView


b_model = register_model["hell_money"]


class HallMoney(BaseView):
    title = "冥币管理"
    b_model = b_model
    page = "hell_money/hell_money.html"


def dispose_hall_money(request):
    name = request.POST.get("name")
    money = request.POST.get("name", 0)
    remark = request.POST.get("remark")

    messages.info(request, f"{name} 因 {remark} 奖励 {money} 冥币 ！！！！")
    return render(request, "hell_money/hell_money.html", context=PageHelper(request))


class HallMoneyPay(BaseView):
    title = "冥币薪资流水"
    b_model = b_model
    page = "index.html"


