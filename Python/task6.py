def task6(string: str) -> dict:
    return {s: string.count(s) for s in set(string)}


if __name__ == '__main__':
    print(task6("Hello, World!"))
