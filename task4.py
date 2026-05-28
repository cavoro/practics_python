def validate_brackets(code: str) -> bool:
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in code:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


code = "{[(a+b) * (c+d)]}"

print(validate_brackets(code))
