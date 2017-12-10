import random
Coda = random.randint(1,999)
Codb = random.randint(1,999)
Codc = random.randint(1,999)

def CodeGenerator():
    A = False
    Codes = {}
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","r","t","u","v","w","x","y","z"," ","-","!",".",",","1","2","3","4","5","6","7","8","9","0","+","="]

    for i in letters:
        while A == False:
            Code = str(random.randint(1,999))
            if Code not in Codes.values() and str(Code) != str(Coda) and str(Code) != str(Codb) and str(Code) != str(Codb):
                if int(Code) < 10:
                    if "00" + str(Code) not in Codes.values():
                        Codes[i] = "00" + str(Code)
                        A = True
                elif int(Code)< 100:
                    if "0" + str(Code) not in Codes.values():
                        Codes[i] = "0" + str(Code)
                        A = True
                else:
                    Codes[i] = str(Code)
                    A = True         
        A = False

    print "Codes: " + str(Codes)
CodeGenerator()
print Coda
CodeGenerator()
print Codb
CodeGenerator()
print Codc
        
