1# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 03:53:28 2022

@author: sgonugun
"""
#Bisection method implementation

def EMICalculator (balance, annualInterestRate):
#balance = 100000
#annualInterestRate = 0.24  #24 percent
    monthlyInterestRate = annualInterestRate/12
    payment_lb = round(balance/12,-1)
    payment_ub = (balance*(1+monthlyInterestRate)**12)/12
    eoyBalance = balance
    while payment_ub - payment_lb>0.01:
        mBalance = balance
        lowestPayment = (payment_lb+payment_ub)/2
        for month in range(1,13):
            mBalance = mBalance - lowestPayment
            remainingBalance = mBalance + (monthlyInterestRate*mBalance)
            mBalance = remainingBalance
        eoyBalance = mBalance
        if mBalance < 0:
            payment_ub = lowestPayment
        else:
            payment_lb = lowestPayment
    monthlyPayment = (round(lowestPayment,2))
    return monthlyPayment

EMI = EMICalculator (principal, interestRate)