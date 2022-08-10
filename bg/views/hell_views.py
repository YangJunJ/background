from bg.config.menu import register_model
from bg.views.base_views import BaseView


b_model = register_model["hell"]


class Explain(BaseView):
    """
    投胎记录
    """
    title = "十八层地狱说明"
    headers = []
    b_model = b_model
    page = "index.html"


class Punish(BaseView):
    """
    处罚流程
    """
    title = "处罚流程"
    headers = []
    b_model = b_model
    page = "index.html"



