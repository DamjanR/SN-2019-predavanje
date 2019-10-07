print("")
print ("UGANI SKRITO ŠTEVILO")
stevilo = int(input ("Vnesi eno število med 1 in 10: "))

if stevilo > 5:
    print("")
    print("Žal, je " + str(stevilo)+ " prevelika številka.")
elif stevilo < 5:
    print("")
    print("Žal, je " + str(stevilo) + " premajhna številka.")
else:
    print("")
    print("*******************************************")
    print("*  BRAVO, ČESTITKE!!! SKRITO ŠTEVILO je " + str(stevilo) + " *")
    print("*******************************************")

print("")
print("--- Konec programa ---")