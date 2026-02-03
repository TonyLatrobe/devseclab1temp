from modules.hello_utils.formatter import format_name

def say_hello(name: str) -> str:
    clean = format_name(name)
    return f"Hello {clean}"