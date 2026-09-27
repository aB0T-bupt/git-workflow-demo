"""简单的问候程序。"""


def greet(name: str) -> str:
    """返回对指定姓名的问候语。"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = input("Name: ")
    print(greet(user_name))
