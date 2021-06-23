import numpy as np
import random as rn
def caller():
    #Generate Random 10 Files
    Arr = np.array(["A" ,"B" ,"C" ,"D" ,"E" ,"F"])
    for i in range(10):
        S = ""
        #Letters From 10 to 50 Letter
        N = rn.randint(10,50)
        for j in range(N):
            N2 = rn.randint(0,5)
            S += Arr[N2]
            #Write them to an .txt File
            F = open("D" + str(i) + ".txt" , "w")
            F.write(S)
            F.close()