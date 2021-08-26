import os, time;
from tall import *;

def linjeNr(arr):
    x = 0;
    for i in arr:
        if(len(i) > x):
            x = len(i);
            return x;

def mellomrom(arr, i, buffer): #Regner ut mellomrom til linje. Mellomrom er lik lengden av den lengste linja, minus lengden på nåværende linje, pluss en buffer på 3
    return (linjeNr(arr) - len(arr[i])) + buffer;

def clear():
    command = "clear";
    if os.name in ('nt', 'dos'): #Sjekker om det kjører windows
        command = "cls";
    os.system(command);

tid = 0;

while 1:
    clear();
    for i in range(9): #Print hver linje av hvert tall
        for x in str(tid): #Print samme linje av hvert tall

            if(x == "1"):
                print(enArr[i] + " " * mellomrom(enArr, i, 5), end='');
            elif(x == "2"):
                print(toArr[i] + " " * mellomrom(toArr, i, 7), end='');
            elif(x == "3"):
                print(treArr[i] + " " * mellomrom(treArr, i, 7), end='');
            elif(x == "4"):
                print(fireArr[i] + " " * mellomrom(fireArr, i, 5), end='');
            elif(x == "5"):
                print(femArr[i] + " " * mellomrom(femArr, i, 5), end='');
            elif(x == "6"):
                print(seksArr[i] + " " * mellomrom(seksArr, i, 5), end='');
            elif(x == "7"):
                print(sjuArr[i] + " " * mellomrom(sjuArr, i, 4), end='');
            elif(x == "8"):
                print(åtteArr[i] + " " * mellomrom(åtteArr, i, 8), end='');
            elif(x == "9"):
                print(niArr[i] + " " * mellomrom(niArr, i, 7), end='');
            elif(x == "0"):
                print(nullArr[i] + " " * mellomrom(nullArr, i, 7), end='');

        print("");
    tid += 1;
    time.sleep(1);
