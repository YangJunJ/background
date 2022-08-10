from bg.config.menu import register_page, register_model, register_menu


def get_menu_info():
    """
    获取后台菜单
    """
    menu = {}
    for page_model in register_menu:
        menu[register_model[page_model]] = []
        for page, page_name in register_page[page_model].items():
            menu[register_model[page_model]].append(dict(
                url=f"/bg/{page}/",
                name=page_name
            ))
    return menu





