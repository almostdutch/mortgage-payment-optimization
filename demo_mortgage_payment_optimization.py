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

import numpy as np
import matplotlib.pyplot as plt

mortgage_amount = 200000;
interest = 2;
lambda1 = 1.0; 
lambda2 = 2000.0;
N_months = 12 * 30; 
fontsize = 24;
labelsize = 24;

temp1 = lambda1 * np.eye(N_months, N_months);
temp2 = np.zeros((N_months, N_months));
temp3 = np.zeros((N_months, N_months));
temp4 = lambda2 * np.eye(N_months, N_months);
temp12 = np.concatenate((temp1, temp2), axis = 0);
temp34 = np.concatenate((temp3, temp4), axis = 0);
E = np.concatenate((temp12, temp34), axis = 1);

b = -1.0; 
temp1 = np.diag(np.repeat(-(1 + interest / (100 * 12)), N_months - 1), k = -1) + np.eye(N_months, N_months);
temp2 = -b * np.eye(N_months, N_months);
A = np.concatenate((temp1, temp2), axis = 1);

B = np.zeros((N_months, 1));
B[0] = (1 + interest / (100 * 12)) * mortgage_amount;

Einv = np.linalg.inv(E);
X = Einv @ A.T @ np.linalg.inv(A @ Einv @ A.T) @ B;

X_debt = X[0:N_months];
X_repayment = X[N_months:]; 
months = np.arange(1, N_months + 1);

fig_width, fig_height = 15, 10;
fig, ((ax1, ax2)) = plt.subplots(nrows=1, ncols=2, figsize=(fig_width, fig_height));

ax1.plot(months, X_debt)
ax1.set_title("Mortgage remaining debt", fontsize = fontsize)
ax1.tick_params(axis='both', which='major', labelsize = labelsize)
ax1.tick_params(axis='both', which='minor', labelsize = labelsize)
ax1.set_xlabel('Month #', fontsize = fontsize)
ax1.set_ylabel('Amount', fontsize = fontsize)
ax1.set_xlim([0, N_months])
ax1.set_ylim([0, mortgage_amount])

ax2.plot(months, X_repayment)
ax2.set_title("Mortgage monthly repayment", fontsize = fontsize)
ax2.tick_params(axis='both', which='major', labelsize = labelsize)
ax2.tick_params(axis='both', which='minor', labelsize = labelsize)
ax2.set_xlabel('Month #', fontsize = fontsize)
ax2.set_ylabel('Amount', fontsize = fontsize)
ax2.set_xlim([0, N_months])
ax2.set_ylim([0, X_repayment.max()])
plt.tight_layout()
