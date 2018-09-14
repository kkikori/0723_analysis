
class DummyPost():
    def __init__(self, id, parent_id, user_id, title, body, created_at, sample):
        self.id = int(id)
        if not parent_id:
            self.parent_id = None
        else:
            self.parent_id = int(parent_id)
        self.user_id = user_id
        if not parent_id:
            self.title = title
        else:
            self.title = None
        self.body = body
        self.created_at = created_at
        self.sample = sample
