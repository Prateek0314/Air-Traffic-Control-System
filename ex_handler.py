
def ex_handler(l,a):
    while True:
        try:
            choice=int(input(a))
        except:
            print("invalid input")
            continue
        if choice not in l:
            print("invalid input")
            continue
        break
    return choice
