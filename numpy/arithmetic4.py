import numpy as np
#Comparision operators
score1 =np.array([38,56,72,100,99])
score2 = np.array([45,24,57,99,13,54])
print(score1==100)
print(score2<=100)
score1[score1<60]=0
score2[score2<50]=0
print(score1)
print(score2)