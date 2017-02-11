prefix = "JKLMNOPQ"
sufix = "ack"

for name in prefix:
    if name == "O" or name == "Q":
        print name + "u" + sufix
    else:
        print name + sufix