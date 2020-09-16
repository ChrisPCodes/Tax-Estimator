
income = int(input("What is your 2019 taxable income? "))



if income >= 510300:
    tax_liability = 153798 + ((income - 510300) * .37)
    tax_rate = (tax_liability / income) * 100

elif income >=204100 and income < 510300:
    tax_liability = 46628 + ((income - 204100) * .35)
    tax_rate = (tax_liability / income) * 100

elif income >= 160725 and income < 204100:
    tax_liability = 32748 + ((income - 160725) * .32)
    tax_rate = (tax_liability / income) * 100

elif income >= 84200 and income < 160725:
    tax_liability = 14382 + ((income - 84200) * .24)
    tax_rate = (tax_liability / income) * 100

elif income >=39475 and income < 84200 :
    tax_liability = 4543 + ((income - 39475) *.22)
    tax_rate = (tax_liability/income) * 100

elif income >= 9700 and income < 39475:
    tax_liability = 970 + ((income -9700) * .12)
    tax_rate = (tax_liability / income) * 100

elif income < 9700 :
    tax_liability = income * .10
    tax_rate = (tax_liability / income) * 100
    


print(f"Your tax liability is, {tax_liability}")
print(f"Your effective tax rate is ${tax_rate}")


if income > 10000000:
    new_tax_liability = 3664987 + ((income - 10000000 ) * .70)
    new_tax_rate = (new_tax_liability / income) * 100
    print(f"With a new 70% bracket, your tax liability would be, {new_tax_liability}")
    print(f"Your effective tax rate with the new bracket would be {new_tax_rate}")
