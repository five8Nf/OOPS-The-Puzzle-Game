def page(title, text):
    page_len = 39
    print(f"╔{"═"*page_len}╗")

    new = title.split(" ")
    line_len = 0
    line = ""
    printed = False
    for word in new:
        if line_len + len(word) <= page_len:
            line += f"{word}"
            line_len += len(word)
            if line_len+1 < page_len:
                line += " "
                line_len += 1
        else:
            print(f"║{line.center(page_len)}║")
            printed = True
            line = f"{word} "
            line_len = len(word)
    if not printed:
        print(f"║{line.center(page_len)}║")

    new = text.split(" ")

    line_len = 0
    line = ""
    for word in new:
        if word == "\n":
            print(f"║{line.ljust(page_len)}║")
            line = ""
            line_len = 0
        elif line_len + len(word) <= page_len:
            line += f"{word}"
            line_len += len(word)
            if line_len+1 < page_len:
                line += " "
                line_len += 1
        else:
            print(f"║{line.ljust(page_len)}║")
            line = f"{word} "
            line_len = len(word) + 1
    print(f"╚{"═"*page_len}╝")

