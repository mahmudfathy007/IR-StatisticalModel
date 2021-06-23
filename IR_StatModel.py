import os
import random
import string
from flask import *
app = Flask(__name__)
import numpy as np
import random as rn
arr = np.array(["A" ,"B" ,"C" ,"D" ,"E" ,"F"])

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
import os
import generate as g
#Index Local Host
@app.route('/')
def index():
   return render_template("index.html")
#Call the Generate Script to generate the 10 files
@app.route('/generate',methods=['GET'])
def generate():
    g.caller()
    return redirect('/')
#Calculate the Similarity
@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == "POST":
        #Take User Input with casting it to float
        q1=float(request.form["Input_1"])
        q2=float(request.form["Input_2"])
        q3=float(request.form["Input_3"])
        q4=float(request.form["Input_4"])
        q5=float(request.form["Input_5"])
        q6=float(request.form["Input_6"])
    f={'D0':0,'D1':0,'D2':0,'D3':0,'D4':0,'D5':0,'D6':0,'D7':0,'D8':0,'D9':0}
    freq=[]
    count_A=0
    count_B=0
    count_C=0
    count_D=0
    count_E=0
    count_F=0
    #count the Freq of each Letter in the document
    for i in range(10):
        m=""
        n=rn.randint(10,50)
        for j in range (n):
            n1=rn.randint(0,5)
            m+=arr[n1]+" "
            if n1==0:
                count_A=count_A+1
            if n1==1:
                count_B=count_B+1
            if n1==2:
                count_C=count_C+1
            if n1==3:
                count_D=count_D+1
            if n1==4:
                count_E=count_E+1
            if n1==5:
                count_F=count_F+1
                #Applying InnerProduct Rule and Calculate the InnerProduct
            c1=(count_A/len(m))*q1
            c2=(count_B/len(m))*q2
            c3=(count_C/len(m))*q3
            c4=(count_D/len(m))*q4
            c5=(count_E/len(m))*q5
            c6=(count_F/len(m))*q6
            #Write the values of the calculating Process
        freq.append(float(c1+c2+c3+c4+c5+c6))
        f= open("D"+str(i)+".txt","w")
        f.write(m)
        f.close()
        n=m.split()
        #Dict for the result to Rank them up
    f={'D0':freq[0],
        'D1':freq[1],'D2':freq[2],'D3':freq[3],'D4':freq[4],'D5':freq[5],'D6':freq[6],'D7':freq[7],'D8':freq[8],'D9':freq[9]}
        #Sort the Results from The highest to the lowest
    key_list = list(f.keys())
    f_sorted = {}
    #values el dic
    print(sorted(f.values(), reverse=True))
    sorted_values = sorted(f.values())
    for i in range(len(sorted_values)-1, 0, -1):
        for key, val in f.items():
            if val == sorted_values[i]:
                f_sorted[key] = val
#Return elemetes sorted
    return f_sorted
    #return f_sorted
    #return dict(sorted(f.items(),reverse=True))
    #return(f)
    #print(sorted(f, reverse=True))
        

if __name__ == '_main_':
   app.run(debug=True)