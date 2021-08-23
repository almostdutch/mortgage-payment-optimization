"""
demo_mortgage_payment_optimization.py

Numerical optimization to find the optimum way for the quickest reduction in the mortage debt \
    while keeping the monthly payments as low as possible.
    
Set lambda1 and lambda2 according to your priorities.

mortgage_amount = initial mortgage amount    
N_months = number of months

X_debt = mortgage debt remaining after each month
lambda1 = regularization for X_debt

X_repayment = mortgage monthly payment after each month
lambda2 = regularization for X_repayment

interest = annual interest [%]

minimize: 
    f(X_debt, X_repayment) = 1 / 2 * (lambda1 * X_debt.T @ X_debt + lambda2 * X_repayment.T @ X_repayment);      
subject to: 
    X_debt(new) = (1 + interest / (100 * 12))  * X_debt(old) - X_repayment;

"""
