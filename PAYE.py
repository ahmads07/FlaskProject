import Calculation

def lessThan14000(gross_income):
    if gross_income < 0 or gross_income > 14000:
        return None
    taxrate = 10.5
    tax = Calculation.multiply(gross_income, taxrate/100)
    return tax

def lessThan48000(gross_income):
    if gross_income <= 14000 or gross_income > 48000:
        return None
    taxrate = 17.5
    tax_range = Calculation.subtract(gross_income, 14000)
    tax = Calculation.multiply(tax_range, taxrate / 100)
    tax = tax + lessThan14000(14000)
    return tax

def lessThan70000(gross_income):
    if gross_income <= 48000 or gross_income > 70000:
        return None
    taxrate = 30
    tax_range = Calculation.subtract(gross_income, 48000)
    tax = Calculation.multiply(tax_range, taxrate/100)
    tax = tax + lessThan48000(48000)
    # tax = tax + lessThan14000(14000)
    return tax

def lessThan180000(gross_income):
    if gross_income <= 70000 or gross_income > 180000:
        return None
    taxrate = 33
    tax_range = Calculation.substract(gross_income, 70000)
    tax = Calculation.multiply(tax_range, taxrate/100)
    tax = tax + lessThan70000(70000)
    # tax = tax + lessThan48000(48000)
    # tax = tax + lessThan14000(14000)
    return tax

def overThan180000(gross_income):
    if gross_income <= 180000:
        return None
    taxrate = 39
    tax_range = Calculation.subtract(gross_income, 180000)
    tax = Calculation.multiply(tax_range, taxrate / 100)
    tax = tax + lessThan180000(180000)
    # tax = tax + lessThan70000(70000)
    # tax = tax + lessThan48000(48000)
    # tax = tax + lessThan14000(14000)
    return tax

def totalTax(gross_income):
    if gross_income > 180000:
        return overThan180000(gross_income)
    elif gross_income > 70000: # 70000 - 180000
        return lessThan180000(gross_income)
    elif gross_income > 48000: # 48000 - 70000
        return lessThan70000(gross_income)
    elif gross_income > 14000: # 14000 - 48000
        return lessThan48000(gross_income)
    else: # up to 14000
        return lessThan14000(gross_income)