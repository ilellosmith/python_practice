
def calculateMinPayment(balance, annualInterestRate): 
    '''Takes balance and annual interest rate, 
    uses bisection evaluation to return the minimum 
    monthly payment to pay off the balance within a year'''
    
    # initialize variables
    monthlyInterestRate = annualInterestRate/12
    lowerBoundPayment = balance/12
    upperBoundPayment = (balance*(1+monthlyInterestRate)**12)/12
    totalBill = balance 
    timeLimit = 12

    # run while loop with bisection algo until amount found
    amountNotFound = True
    iter = 0
    while amountNotFound:

        # get original balance 
        balance = totalBill
        # find mindpoint of current bounds 
        midPayment = lowerBoundPayment + (upperBoundPayment - lowerBoundPayment)/2
        
        # test if this payment can pay off balance in timeLimit months
        for month in range(timeLimit):
            balance -= midPayment
            balance *= (1+monthlyInterestRate)

        # show progress 
        print("iteration is %d" % iter)
        print("upper bound payment is %d" % upperBoundPayment)
        print("lower bound payment is %d" % lowerBoundPayment)
        print("mid payment is %d" % midPayment)
        print("amount remaining is %d" % balance)

        # select final value or update bounds
        if round(balance,2) == 0:
            amountNotFound = False # value found, exit loop, save min amount
            minAmount = midPayment
        elif balance < 0:
            upperBoundPayment = midPayment # if too much, midPayment becomes upper end
        else:
            lowerBoundPayment = midPayment # if too little, midPayment becomes lower
        iter += 1

    return minAmount

# algo: 
# calculate total bill 
# interval is lower bound to upper bound to start
# select midpoint
# if mid point is too big, use as upper bound
# repeat until midpoint is exactly the amount

