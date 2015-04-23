# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:57:23 2015

@author: zhyfly711
"""

def minPayment(annualInterestRate, balance, monthlyPaymentRate):
    #Calculate the total amount paid and the remaining balance if
    #just pay the minimum amount each month
    monInterestRate = annualInterestRate/12
    totalPaid = 0
    for i in range(1, 13):
        monthlyPayMent = balance * monthlyPaymentRate
        monthlyInterest = monInterestRate * (balance - monthlyPayMent)
        balance = balance - monthlyPayMent + monthlyInterest
        totalPaid = totalPaid + monthlyPayMent
        print 'Month:' + ' ' + str(i)
        print 'minimum monthly payment:' + ' ' + str(round(monthlyPayMent, 2))
        print 'Remaining balance:' + ' ' + str(round(balance, 2))
    
    print 'Total paid: ' + str(round(totalPaid, 2))
    print 'Remaining balance: ' + str(round(balance, 2))



def cleanDebt(balance, annualInterestRate):
    # Calculate the minimum amount one should pay to clean all the
    # debt in a year. Amount paid is multiple of 10. Using bisection search.
    minMonthlyPayment = 10*(balance//12//10)
    monInterestRate = annualInterestRate/12
    leftBalance = balance
    while leftBalance > 0:
        leftBalance = balance
        for i in range(1, 13):
            monthlyInterest = monInterestRate * (leftBalance - minMonthlyPayment)
            leftBalance = leftBalance - minMonthlyPayment + monthlyInterest
        minMonthlyPayment += 10

    print 'lowest payment: ' + str(minMonthlyPayment - 10)

    

def cleanDebt2(balance, annualInterestRate):
    # Calculate the minimum amount that should be paid to clean all the
    # debt in a year. Amount paid is accurate to cent. Using bisection search
    monInterestRate = annualInterestRate/12
    highestBalance = balance
    for i in range(1, 13):
        monthlyInterest = monInterestRate * highestBalance
        highestBalance = highestBalance + monthlyInterest
        
    minMonthlyPayment = balance/12
    maxMonthlyPayment = highestBalance/12 
    leftBalance = minMonthlyPayment
    monthlyPayment = 0

    while abs(leftBalance) > 0.02:
        monthlyPayment = (minMonthlyPayment + maxMonthlyPayment)/2
        leftBalance = balance
        for i in range(1, 13):
            monthlyInterest = monInterestRate * (leftBalance - monthlyPayment)
            leftBalance = leftBalance - monthlyPayment + monthlyInterest

        if leftBalance > 0:            
            minMonthlyPayment = monthlyPayment
        else:
            maxMonthlyPayment = monthlyPayment
       

    print 'lowest payment per month: ' + str(round(monthlyPayment, 2))

balance = input('Please input your balance: ')
annualInterestRate = input('Please input your AnnualInterestRate: ')

cleanDebt2(balance, annualInterestRate)