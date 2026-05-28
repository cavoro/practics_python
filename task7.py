class PhoneBook:

    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def add(self, name, phone):
        index = self.hash_function(name)

        for item in self.table[index]:
            if item[0] == name:
                item[1] = phone
                return

        self.table[index].append([name, phone])
        self.count += 1

        if self.count / self.size > 0.75:
            self.resize()

    def get(self, name):
        index = self.hash_function(name)

        for item in self.table[index]:
            if item[0] == name:
                return item[1]

        return "Контакт не знайдено"

    def remove(self, name):
        index = self.hash_function(name)

        for i in range(len(self.table[index])):
            if self.table[index][i][0] == name:
                del self.table[index][i]
                self.count -= 1
                return True

        return False

    def size_contacts(self):
        return self.count

    def resize(self):
        old_table = self.table

        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for name, phone in bucket:
                self.add(name, phone)


book = PhoneBook()

book.add("Іван", "111-11-11")
book.add("Марія", "222-22-22")

print(book.get("Іван"))

book.remove("Іван")

print(book.get("Іван"))
print(book.size_contacts())
