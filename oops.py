from car import BlueCar

maruti:BlueCar = BlueCar("MARUTI", "C", 3)
kia:BlueCar = BlueCar(brand="Kia", power_rating="B", overall_rating=3.5)

print(repr(kia))
print(kia)
print(maruti.overall_rating)
 
 
'''
maruti.turn_on()
maruti.run(12)
maruti.turn_off()
print("\n")


kia.turn_on()
kia.run(30)
kia.turn_off()


print(maruti.brand)
print(maruti.power_rating)
print(maruti.overall_rating)
print("\n")
kia:BlueCar = BlueCar(brand="Kia", power_rating="B", overall_rating=3.5)
print(kia.brand)
print(kia.power_rating)
print(kia.overall_rating)
'''
