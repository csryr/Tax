def calcTax(salary,income,bracket):

    tax =0

    if salary > income[-1]:

        tax+= (salary - income[-1]) * bracket[-1]

    for i in range (len(income)):
        if salary > income[i]:

            tax += (income[i] -income[i-1]) * bracket[i]
        else:

            tax += (salary - income[i-1]) * bracket[i]

            break


    return tax


def calcTaxCredit(dividends,grossUp,taxCredit):

    taxCredit = dividends*grossUp*taxCredit

    return taxCredit


def calcTuitionCredit(tuition,fedbracket):


    tuition = tuition * fedbracket

    return tuition

def calcDonoCredit(dono,income,bracket):

    tax =0

    if dono < income:
        tax += dono*bracket[0]

    else:
        tax += (income*bracket[0])
        tax += (dono-income) *bracket[1]


    return tax
