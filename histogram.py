def histogram(s):
    d = dict()  # funkcija dict radi prazan dictionary iliti ***d = {}***
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return d
    
print histogram("hologram")
print histogram("kakarrot")
print histogram("mediastructure") # ili assert.equal
