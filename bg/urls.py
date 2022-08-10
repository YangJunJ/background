from django.urls import path
import bg.views.index_views as index
import bg.views.live_or_die_views as ld
import bg.views.hell_money_views as hm
import bg.views.hell_views as ex

app_name = "bg"

urlpatterns = []

# 首页
urlpatterns += [
    path('', index.index)
]


# 生死簿
urlpatterns += [
    path('bg/people_page/', ld.UserManagement.as_view()),
    path('bg/dispose_page/', ld.UserDispose.as_view()),
    path('bg/reincarnation_page/', ld.Reincarnation.as_view()),
]


# 十八层地狱
urlpatterns += [
    path('bg/explain_page/', ex.Explain.as_view()),
    path('bg/punish_page/', ex.Punish.as_view()),
]


# 冥币管理
urlpatterns += [
    path('bg/money_page/', hm.HallMoney.as_view()),
    path('bg/hall_money/', hm.dispose_hall_money, name="dispose_hall_money"),
    path('bg/money_pay/', hm.HallMoneyPay.as_view()),
]





