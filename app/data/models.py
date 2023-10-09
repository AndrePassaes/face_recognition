class Image(object):
    def __init__(self, path, category, score):
        self.path = path
        self.category = category
        self.score = score

    def __repr__(self):
        return f"Image({self.path}, {self.category}, {self.score})"
