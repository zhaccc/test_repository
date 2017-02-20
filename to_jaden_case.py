import string

def toJadenCase(str):
    return string.capwords(str)
    
quote = "How can mirrors be real if our eyes aren't real"
print toJadenCase(quote)