class EprData:
    def __init__(self, repo_editor_dict: dict = None, editors: list = None, show_found_editors: bool = True):
        self.editors = editors or []
        self.repo_editor_dict = repo_editor_dict or {}
        self.show_found_editors = show_found_editors


    def __str__(self):
        return str({
            "editors": self.editors,
            "show_found_editors": self.show_found_editors
        })