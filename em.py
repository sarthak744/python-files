message = input("> ")
words = message.split(' ')
output = " "
emoji = {
    ":)": "😁",
    ":(": "😒"
}
for word in words:
    output += emoji.get(word, word) + " "
print(output)
