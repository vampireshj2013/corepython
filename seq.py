class seq(object):
    def __init__(self, max_num=100):
        self.max_num = max_num
        self.N = self.max_num

    def __iter__(self):
        return self

    def next(self):
        self.max_num -= 1
        if self.max_num == 0:
            raise StopIteration
        return self.N - self.max_num


for i in seq():
    print i
