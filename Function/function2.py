def disp(sh):
    print("Disp Function")
    return sh

def show():
    return "show function"

r_sh = disp(show)
print(r_sh())