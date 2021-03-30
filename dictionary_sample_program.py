##Dictionary Sample program

# phone = input("Phone: ")

# digits = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# outp = ""
# for x in phone:
#     outp += digits.get(x, "!") + " "
# print(outp)

def emoji(msg):
    words = msg.split(' ')

    emojis = {
        ":)":":smile:",
        ":(":":sad:"
    }
    outp = ""
    for word in words:
        outp += emojis.get(word, word) + " "
    return outp


msg = input("> ")
print(emoji(msg))


