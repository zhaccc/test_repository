def disemvowel(string):
    new = string    # moramo unaprijed zadati varijablu da je tu mjenja iteracijom, inace ce samo mijenjati zadnju iteraciju (npr. veliko "O" na "LOL")!
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in string:
        if x in vowels:
            new = new.replace(x, "")        
    return new
    
print disemvowel("This website is for losers LOL!")