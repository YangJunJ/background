from bg.config.menu import register_model, register_page
from bg.helper.bg_page_helper import PageHelper
from bg.views.base_views import BaseView


b_model = register_model["live_or_die"]


class UserManagement(BaseView):
    title = "用户管理"
    headers = ["死亡时间", "死者名字", "性别", "死亡原因"]
    b_model = b_model
    page = "live_or_die/user_management.html"

    def search(self, page_helper: PageHelper):
        """
        随便返回几条数据
        """
        page_helper["data_list"] = [
            ["2022-07-08", "安倍晋三", "男", "死于正义之士枪杀"],
            ["2022-07-06", "张三", "男", "自然死亡"],
            ["2022-07-05", "李四", "男", "自然死亡"],
            ["2022-07-06", "张三2", "男", "自然死亡"],
            ["2022-07-05", "李四2", "男", "自然死亡"],
            ["2022-07-06", "张三3", "男", "自然死亡"],
            ["2022-07-05", "李四4", "男", "自然死亡"],
        ]


class UserDispose(BaseView):
    """
    用户处理
    """
    title = "用户处理"
    headers = []
    b_model = b_model
    page = "index.html"


class Reincarnation(BaseView):
    """
    投胎记录
    """
    title = "投胎记录"
    headers = []
    b_model = b_model
    page = "index.html"



