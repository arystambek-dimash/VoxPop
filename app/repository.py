class CommentRepository:
    def __init__(self):
        self.comments = []


    def get_all(self):
        return self.comments
    def save(self, comment):
        if "id" not in comment:
            comment["id"] = self.get_next_id()
        self.comments.insert(0,comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1