#недоделано
class Student():
    def __init__(self, name:str,  number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        if self.number != other.number:
            return True
students = {
    ("Афанасий Афанасьевич", 111),
    ("Иван Иванович", 111),
    ("Анастасия Медведева", 213)
}
for name, number in students:
    for i in range(len(students)-1):
        
    print(name, number)
