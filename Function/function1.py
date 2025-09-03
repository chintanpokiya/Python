def disp():
    def show():
        return "show function"
    print("Disp Function")
    return show

r_sh = disp()
print(r_sh())