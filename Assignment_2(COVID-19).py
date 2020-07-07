var1 = input("Are you a cigarette addict older than 75 years old?(Yes/No): ").lower().title()
var1 = bool(var1 == "Yes")
var2 = input("Do you have a severe chronic disease?(Yes/No): ").lower().title()
var2 = bool(var1 == "Yes")
var3 = input("Is your immune system too weak?(Yes/No): ").lower().title()
var3 = bool(var1 == "Yes")

if var1 or var2 or var3:
    print("You are in risky group")
else:
    print("You are not in risky group")