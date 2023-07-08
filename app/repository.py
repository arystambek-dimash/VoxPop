class CommentRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "user": 'starboy', 'comment': 'Hello11 my name is starboy. In this comment i want say about Government', 'category': 'positive'},
            {"id": 2, "user": 'starboy11', 'comment': 'Hello my name is starboy. In this comment i want say about Government', 'category': 'negative'},
            {"id": 3, "user": 'starboy221', 'comment': 'Hello my name is starboy. In this comment i want say about Government', 'category': 'negative'},
            {"id": 4, "user": 'starboy33', 'comment': 'Hello my name is starboy. In this comment i want say about Government', 'category': 'positive'},
        ]

    def get_all(self):
        return self.comments

    def save(self, comment):
        if not comment["id"]:
            comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1