def schl(mrks):
     scpr = mrks/2
     scpr = (25000*scpr)//100
     ttlfee = 25000-scpr
     ttlfee += 1500
     print("Amount to be paid",ttlfee)

mrks = int(input("enter marks"))
schl(mrks)