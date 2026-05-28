class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_palindrome(phrase: str) -> bool:

    cleaned = ""

    for char in phrase:
        if char.isalnum():
            cleaned += char.lower()

    deque = Deque()

    for char in cleaned:
        deque.add_rear(char)

    while deque.size() > 1:

        first = deque.remove_front()
        last = deque.remove_rear()

        if first != last:
            return False

    return True


text = "А роза упала на лапу Азора"

print(is_palindrome(text))
