
# File: main.py
def greet(name):
    """Greet someone with enthusiasm"""
    if not name:
        return "Hello there!"
    return f"Hello, {name}! Welcome to Cyberrange. 🚀"

if __name__ == "__main__":
    print(greet("Developer"))