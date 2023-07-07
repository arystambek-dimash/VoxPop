class CommentRepository:
    def __int__(self):
        self.comments = [
            {"id" : 1,"user" : 'starboy','comment':'Hello my name is starboy. In this comment i want say about Goverment','category':'positive'},
            {"id": 2, "user": 'starboy11','comment': 'Hello my name is starboy. In this comment i want say about Goverment', 'category': 'negative'},
            {"id": 3, "user": 'starboy221','comment': 'Hello my name is starboy. In this comment i want say about Goverment', 'category': 'negative'},
            {"id": 4, "user": 'starboy33','comment': 'Hello my name is starboy. In this comment i want say about Goverment', 'category': 'positive'},
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