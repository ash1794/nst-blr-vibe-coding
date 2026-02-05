def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


def format_name(first, last):
    return f"{last}, {first}"


def repeat_message(message, times):
    result = []
    for i in range(times):
        result.append(message)
    return result


if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(format_name("Arjun", "Kumar"))
    print(repeat_message("NST", 3))
