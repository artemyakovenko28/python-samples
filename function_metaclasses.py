def add_attributes(cls, *args, **kwargs):
    new_cls = type(cls, *args, **kwargs)
    setattr(new_cls, 'email', 'example@gmail.com')
    setattr(new_cls, 'phone', '0959457654')
    return new_cls


class User(metaclass=add_attributes):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return 'User: first_name = ' + self.first_name + \
               ', last_name = ' + self.last_name + \
               ', email = ' + self.email + \
               ', phone = ' + self.phone


user = User('Artem', 'Yakoveko')
print(user)
