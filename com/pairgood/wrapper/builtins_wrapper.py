def wrapped_print(value):
    print(value)


def wrapped_print_no_return(value):
    print(value, end='')


def wrapped_input(value):
    return input(value)


def wrapped_exit():
    exit()
