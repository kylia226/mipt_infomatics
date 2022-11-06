class BinTree:
    def __init__(self, val, left=None, right=None):
        self.length = 0
        self.start = None
        self.left = left
        self.right = right
        self.value = val

    @property
    def __iter__(self):
        for i in self.left:
            yield i.value
        yield self.value
        for i in self.right:
            yield i.value
