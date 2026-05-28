def search_dictionary(dictionary: list, word: str) -> str:
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2

        if dictionary[mid][0] == word:
            return dictionary[mid][1]

        elif dictionary[mid][0] < word:
            left = mid + 1

        else:
            right = mid - 1

    return "Слово не знайдено"


dictionary = [
    ("apple", "яблуко"),
    ("book", "книга"),
    ("cat", "кіт"),
    ("dog", "собака")
]

print(search_dictionary(dictionary, "cat"))
