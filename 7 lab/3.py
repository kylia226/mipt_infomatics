class Mymeta(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__()
        y = list(attrs.keys())
        for i in range(len(y)):
            if "certain_line" not in y[i]:
                continue
            if 'function' not in str(attrs[y[i]]):
                continue
            raise Exception("Unsuitable fragment in the name of function.")
            return


class Proverka(object, metaclass=Mymeta):
    def certain_line_random(self):
        print(1)

    def normal_function(self):
        print("not_this")


if __name__ != '__main__':
    pass
else:
    Q = Proverka()
    Q.certain_line_random()
    Q.normal_function()
