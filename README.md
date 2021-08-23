""" </br>
demo_mortgage_payment_optimization.py </br>

Numerical optimization to find the optimum way for the quickest reduction in the mortage debt </br>
    while keeping the monthly payments as low as possible. </br>
    
Set lambda1 and lambda2 according to your priorities. </br>

mortgage_amount = initial mortgage amount </br>    
N_months = number of months </br>

X_debt = mortgage debt remaining after each month </br>
lambda1 = regularization for X_debt </br>

X_repayment = mortgage monthly payment after each month </br>
lambda2 = regularization for X_repayment </br>

interest = annual interest [%] </br>

minimize: </br> 
    f(X_debt, X_repayment) = 1 / 2 * (lambda1 * X_debt.T @ X_debt + lambda2 * X_repayment.T @ X_repayment); </br>      
subject to: </br> 
    X_debt(new) = (1 + interest / (100 * 12))  * X_debt(old) - X_repayment; </br>

"""
