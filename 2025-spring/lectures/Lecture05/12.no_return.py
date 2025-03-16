from typing import NoReturn

def fatal_error(message: str) -> NoReturn:
    raise RuntimeError(f"Fatal Error: {message}")

fatal_error("Something went wrong!")
