class EprData:
    def __init__(self, repo_editor_dict: dict = None, editors: list = None,
                 show_found_editors: bool = True, last_used_editor_path: str = None):
        self.editors = editors or []
        self.repo_editor_dict = repo_editor_dict or {}
        self.show_found_editors = show_found_editors
        self.last_used_editor_path = last_used_editor_path


    def __str__(self):
        return str({
            "editors": self.editors,
            "repo_editor_dict": self.repo_editor_dict,
            "show_found_editors": self.show_found_editors
        })