import pydantic


def add_numbers(a: int, b: int):
    return a + b

out = add_numbers("a", "b")  # This will work and return 5

print(out)