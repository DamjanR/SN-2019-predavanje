# 8 predavanje (1 naloga)
mood = input("Opiši svoje razpoloženje:")
if mood == "vesel":
    print("Lepo te je videti veselega!")
    print("")
elif mood == "žalosten":
    print("Ej stari 3× globoko vdihni!")
    print("")
else:
    print("NO GO!")
    print("Danes si lahko le >>vesel<< ali >>žalosten<<!")
    print("")
    if mood == "živčen":
        print("Danes so itak vsi živčni!")
        print("")
print("***** END *****")