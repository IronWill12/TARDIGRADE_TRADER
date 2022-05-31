print("Convert to meters")
distance = int(input("What is the distance: "))
unit = input("What is the unit of measurement : ")

conversion = {
"yard" : 0.9144,
"inch" : 0.0254,
"foot" : 0.3048,
"mile" : 1609.34,
"meter" : 1,
"kilometer" : 1000,
}
output = distance * conversion[unit]
print(f"{distance} {unit} is {output} meters.")

