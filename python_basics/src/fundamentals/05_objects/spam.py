def add_spam(menu=[]):
    menu.append("spam")
    return menu


print(add_spam())
print(add_spam(['add']))
print(add_spam(None)) # Failure Case