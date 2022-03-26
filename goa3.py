def string_test(p):
    n={"UPPER_CASE":0, "LOWER_CASE":0}
    for k in p:
        if k.isupper():
           n["UPPER_CASE"]+=1
        elif k.islower():
           n["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", p)
    print ("No. of Upper case characters : ", n["UPPER_CASE"])
    print ("No. of Lower case Characters : ", n["LOWER_CASE"])

string_test("i Am Waste feLLow")