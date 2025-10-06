class USER:
    name = 'salman'
    __password = '1234'
    def method(self):
        return self.__password
class Teacher(USER):
    # print(USER._password)
    pass

user = Teacher()
print(USER().method())