from bg.helper.menu_helper import get_menu_info


class PageHelper(dict):
    def __init__(self, request):
        super().__init__()

        data = {}
        if request.method == "POST":
            data = request.POST
        elif request.method == "GET":
            data = request.GET

        for k, v in data.items():
            if k == "csrfmiddlewaretoken":
                continue
            self[k] = v

        self['menuInfo'] = get_menu_info()
