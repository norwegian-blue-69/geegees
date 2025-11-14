def greet(name: str) -> str:
    """Return a greeting for name."""
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()
