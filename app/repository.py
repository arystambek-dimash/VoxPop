class CommentRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "user": 'Elon',
             'comment': 'I absolutely loved this book! The characters were so well-developed, and the plot kept me hooked from start to finish.This restaurant never disappoints! The food is always delicious, and the service is top-notch.',
             'category': 'positive',
             'date':'2022-10-5'},
            {"id": 2, "user": 'user-12020',
             'comment': 'I was really disappointed with the service at this restaurant. The waitstaff was rude, and the food took forever to arrive.This movie was a letdown. The plot was confusing, and the acting felt forced and unnatural.',
             'category':'negative',
             'date':'2022-10-6'},
            {"id": 3, "user": 'user-8048',
             'comment': 'I absolutely loved this book! The characters were so well-developed, and the plot kept me hooked from start to finish.This restaurant never disappoints! The food is always delicious, and the service is top-notch.',
             'category': 'positive',
             'date': '2022-10-5'},
            {"id": 4, "user": 'Aiko',
             'comment': 'I was really disappointed with the service at this restaurant. The waitstaff was rude, and the food took forever to arrive.This movie was a letdown. The plot was confusing, and the acting felt forced and unnatural.',
             'category': 'negative',
             'date': '2022-10-6'},{"id": 1, "user": 'RainbowDreamer',
             'comment': 'I absolutely loved this book! The characters were so well-developed, and the plot kept me hooked from start to finish.This restaurant never disappoints! The food is always delicious, and the service is top-notch.',
             'category': 'positive',
             'date':'2022-10-5'},
            {"id": 5, "user": 'Dima',
             'comment': 'I was really disappointed with the service at this restaurant. The waitstaff was rude, and the food took forever to arrive.This movie was a letdown. The plot was confusing, and the acting felt forced and unnatural.',
             'category':'negative',
             'date':'2022-10-6'},{"id": 1, "user": 'RainbowDreamer',
             'comment': 'I absolutely loved this book! The characters were so well-developed, and the plot kept me hooked from start to finish.This restaurant never disappoints! The food is always delicious, and the service is top-notch.',
             'category': 'positive',
             'date':'2022-10-5'},
            {"id": 6, "user": 'Muha',
             'comment': 'I was really disappointed with the service at this restaurant. The waitstaff was rude, and the food took forever to arrive.This movie was a letdown. The plot was confusing, and the acting felt forced and unnatural.',
             'category':'negative',
             'date':'2022-10-6'},
        ]


    def get_all(self):
        return self.comments

    def save(self, comment):
        if "id" not in comment:
            comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1