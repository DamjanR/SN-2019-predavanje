print("")
print ("    MOJ PRVI KALKULATOR (+ - * /)    ")
print("-------------------------------------")

print("")
x = int(input("Vnos prve številke:  "))
y = int(input("Vnos druge številke: "))
znak = str(input("vnesi opreacijo:     "))

if znak == "+":
    print("")
    print("REZULTAT = " + str((x)+(y)))
    #    print(int(x) + int(y))
elif znak == "-":
    print("")
    print("REZULTAT = " + str((x)-(y)))
#    print(int(x) - int(y))
elif znak == "*":
    print("")
    print("REZULTAT = " + str((x)*(y)))
#    print(int(x) * int(y))
else:
    znak == "/"
    print("")
    print("REZULTAT = " + str((x)/(y)))
#    print(int(x) / int(y))

print("")
print("---------- Konec programa -----------")