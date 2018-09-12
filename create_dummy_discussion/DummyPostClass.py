from .fetch_api import get_access_token


class DummyPost():
    def __init__(self, id, parent_id, user_id, title, body, created_at, sample, index):
        self.index = index
        self.original_id = id
        self.parent_original_id = parent_id
        self.user_id = user_id
        if not parent_id:
            self.title = None
        else:
            self.title = title
        self.body = body
        self.created_at = created_at
        self.sample = sample
