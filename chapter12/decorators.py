def extract_str_payload(args, kwargs):
    args_kwargs = list(str(n) for n in args) + [f"{k}={v}" for k, v in kwargs.items()]
    return ", ".join(args_kwargs)

def call_counter(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"[COUNT]: {calls}")
        return func(*args, **kwargs)
    return wrapper

def log_call(func):
    name = func.__name__
    def wrapper(*args, **kwargs):
        print(f"[LOG] {name}({extract_str_payload(args, kwargs)})")
        result = func(*args, **kwargs)
        print(f"[LOG] Returning {result}")
        return result
    return wrapper

@call_counter
@log_call
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, 3))