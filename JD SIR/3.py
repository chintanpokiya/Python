def gender(str12):
    ans=""
    string=str12.strip().split()
    if string[3]=="M":
        ans = f"Mr. {string[0]} {string[1]}"
    else:
        ans = f"Mrs. {string[0]} {string[1]}"

gender("Neelkanth Parekh M")
