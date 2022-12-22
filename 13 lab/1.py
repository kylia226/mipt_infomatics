# 1
import pickle

# Коллекция сериализуемых объектов
data = {
    'a': [1, 2.0, 3, 4 + 6j, float("nan")],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# Сериализация словаря data с использованием
# версии протокола по умолчанию.
print(pickle.dumps(data))

with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
# b'\x80\x04\x95\x82\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x01a\x94]\x94(K\x01G@\x00\x00\x00\x00\x00\x00\x00K\x03\x8c\x08builtins\x94\x8c\x07complex\x94\x93\x94G@\x10\x00\x00\x00\x00\x00\x00G@\x18\x00\x00\x00\x00\x00\x00\x86\x94R\x94G\x7f\xf8\x00\x00\x00\x00\x00\x00e\x8c\x01b\x94\x8c\x10character string\x94C\x0bbyte string\x94\x86\x94\x8c\x01c\x94\x8f\x94(\x89\x88N\x90u.'


import pickle

with open('data.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)
# {'a': [1, 2.0, 3, (4+6j), nan], 'b': ('character string', b'byte string'), 'c': {False, True, None}}

# 2
import pickle

numbers = [1,
           2,
           3]
numbers = iter(numbers)

print(pickle.dumps(numbers))

with open('numbers.pickle', 'wb') as f:
    pickle.dump(numbers.__next__(), f, pickle.HIGHEST_PROTOCOL)
# b'\x80\x04\x95&\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x04iter\x94\x93\x94]\x94(K\x01K\x02K\x03e\x85\x94R\x94K\x00b.'


# 3
import collections

with open('the.serialisation4', 'wb') as f:
    pickle.dump(collections.deque, f, pickle.HIGHEST_PROTOCOL)


# 4
class Zebra():
    def __init__(self, extra):
        self.additional_information = extra

    def information(self):
        return self.name, self.age, self.additional_information


with open('the.serialisation5', 'wb') as f:
    pickle.dump(Zebra, f, pickle.HIGHEST_PROTOCOL)
    print(pickle.dumps(Zebra))


#5
def through(a):
    if type(a) != int:
        return
    return a ** 2


with open('the.serialisation6', 'wb') as f:
    pickle.dump(through, f, pickle.HIGHEST_PROTOCOL)
    print(pickle.dumps(through))

