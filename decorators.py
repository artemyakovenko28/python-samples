def decorate_with_p(func):
    def wrapper(name):
        return '<p>' + str(name) + '<p>'

    return wrapper


def log_decorator(func):
    def wrapper(*args):
        arguments = locals()
        del arguments['func']
        print('execute ' + func.__name__ + 'with arguments: ' + str(arguments))
        result = func(args)
        print(func.__name__ + ' result: ' + str(result))
        return result

    return wrapper


@log_decorator
@decorate_with_p
def greeting(name):
    return 'greeting, ' + name + '!'


print(greeting('Artem'))

##########################################
######## Parametrized decorator ##########


def parametrized_decorator(tag_name):
    def decorator(func):
        def wrapper(string):
            return '<' + tag_name + '>' + \
                   func(string) + '</' + tag_name + '>'
        return wrapper
    return decorator


@parametrized_decorator('div')
def say_hello(name):
    return 'hello ' + name + '!'


print(say_hello('Artem'))
