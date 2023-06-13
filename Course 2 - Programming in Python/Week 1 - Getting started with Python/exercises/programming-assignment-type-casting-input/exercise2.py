# Modify the line below

coffee = float(input('1 coffee @: $ '))
# Modify the line below

sandwich = float(input('1 sandwich @: $ '))
# Modify the line below

cake = float(input('1 cake @: $ '))
bill_total = coffee + sandwich + cake

# don't do this bill_total = "{:.2f}".format(bill_total)

#It will show an typeError
print('Your total bill is $ {:.2f}'.format(bill_total))  
