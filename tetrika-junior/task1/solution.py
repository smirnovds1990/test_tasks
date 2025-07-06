from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        annotations = func.__annotations__
        args_with_names = list(zip(annotations, all_args))
        for arg, value in args_with_names:
            if not isinstance(value, annotations[arg]):
                raise TypeError(
                    f"'{arg}' argument should be {annotations[arg]}. "
                    f"Got {type(value)}."
                )
            continue
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
