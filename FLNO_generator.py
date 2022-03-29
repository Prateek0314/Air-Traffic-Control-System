#module to generate plane numbers
import random
def plane_gen():
    no=str(random.randint(1000,9999))
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l=letters[random.randint(0,25)]+letters[random.randint(0,25)]
    flno=l+no
    return flno
