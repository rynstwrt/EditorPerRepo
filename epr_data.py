class EprData:
    def __init__(self, editors: list = None, last_used_show_found_editors: bool = True):
        self.editors = editors or []
        self.show_found_editors = last_used_show_found_editors


    def __str__(self):
        return str({
            "editors": self.editors,
            "show_found_editors": self.show_found_editors
        })