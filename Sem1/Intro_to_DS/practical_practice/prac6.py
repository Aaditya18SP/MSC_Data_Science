import numpy as np
from scipy.stats import t, ttest_ind, ttest_1samp
# 1 sample t-test

print("=======1 sample t-test=========")
samp =np.arange(1500,3000,200)
h0_mean = 2500
h1_mean = np.mean(samp)
n = len(samp)
s = np.std(samp)
alpha =0.05

dof = n-1

test_statistic = (h1_mean - h0_mean)/(s/np.sqrt(n))

left_t = t.ppf(0.025,dof)
right_t = t.ppf(0.975,dof)
print(test_statistic)
print(left_t, right_t)

if(test_statistic < left_t or test_statistic >right_t):
    print("Reject H0")
else:
    print("Fail to reject H0")

print("======using inbuilt method=======")
result = ttest_1samp(samp,h0_mean)
print(result.statistic)
print("======2 sample t-test=======")
sam1 = np.linspace(10,1000,25)
sam2 = np.arange(0,1000,25)
s1_mean = np.mean(sam1)
s2_mean = np.mean(sam2)

s1 = np.std(sam1)
s2 = np.std(sam2)
n1 = len(sam1)
n2 =len(sam2)

alpha = 0.05

dof = ((s1**2/n1) + (s2**2/n2))**2/ (((s1**2/n1)**2/(n1-1)) + ((s2**2/n2)**2/(n2-1)))
se = np.sqrt((s1**2/n1) + (s2**2/n2))
test_statistic = (s1_mean - s2_mean)/se

print(dof, test_statistic)

crit_left = t.ppf(0.025,dof)
crit_right = t.ppf(0.975, dof)

if(test_statistic < crit_left or test_statistic > crit_right):
    print("reject H0")
else:
    print("fail to reject h0")

print("=====using inbuilt methods =======")
result = ttest_ind(sam1, sam2, equal_var=False) 
print(result)


print()
print("========one way anova==========")
