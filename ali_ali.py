stevilo_prijavljenih = 19
if stevilo_prijavljenih > 100:
    print("Dovolj prijavljenih: " + str(stevilo_prijavljenih))
    print("Druga vsrtica telesa if")
elif stevilo_prijavljenih > 90:
    print("Skoraj dovolj prijav")
else:
    print("Pogoj ni bil resničen")
    if 1 == 1:
        print("1 je enako kot 1")
    else:
        print("To se ne izvede nikoli")
print("Konec programa")