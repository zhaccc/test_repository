# while moramo inkrementirati da odbroji
def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print "Takeoff!"
    
countdown(3)

# range odbrojava sam
def countdown_alt(n):
    print n
    for n in reversed(range(n)):
        print n
    print "Take"
    
countdown(7)

countdown_alt(777) #7777
