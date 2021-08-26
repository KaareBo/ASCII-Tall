en = " _ \n| |\n| |\n| |\n| |\n| |\n| |\n| |\n|_|";

to = "   _____\n  / ___ \ \n /_/   \ \ \n       / /\n      / /\n     / /\n    / /\n __/ /___\n|________|"

tre = "  _____\n / ___ \ \n/_/   \ \ \n    __/ /\n   |__ |\n      \ \ \n__    | |\n\ \___/ /\n \_____/"

fire = " _     _ \n| |   | |\n| |   | |\n| |___| |\n|_____| |\n      | |\n      | |\n      | |\n      |_|"

fem = " _________\n|   ______|\n|  |\n|  |_____\n|_____   \ \n      \   \ \n___   |   |\n\  \__/   /\n \_______/"


enArr = ["___", "| |", "| |", "| |", "| |", "| |", "| |", "| |", "|_|"];

toArr = ["   _____", "  / ___ \ ", " /_/   \ \ ", "       / /", "      / /", "     / /", "    / /", " __/ /___", "|________|"];

treArr = ["  _____", " / ___ \ ", "/_/   \ \ ", "    __/ /", "   |__  |", "      \ \ ", "__    | |", "\ \___/ /", " \_____/"]

fireArr = [" _     _ ", "| |   | |", "| |   | |", "| |___| |", "|_____| |", "      | |", "      | |", "      | |", "      |_|"];

femArr = [" _________", "|   ______|", "|  |", "|  |_____", "|_____   \ ", "      \   \ ", "___   |   |", "\  \__/   /", " \_______/"]


def linjeNr(arr):
    x = 0;
    for i in arr:
        if(len(i) > x):
            x = len(i);
            return x;

def mellomrom(arr, i, buffer): #Regner ut mellomrom til linje. Mellomrom er lik lengden av den lengste linja, minus lengden på nåværende linje, pluss en buffer på 3
    return (linjeNr(arr) - len(arr[i])) + buffer;

for i in range(9):
    print(enArr[i] + " " * mellomrom(enArr, i, 3), end='');
    print(toArr[i] + " " * mellomrom(toArr, i, 5), end='');
    print(treArr[i] + " " * mellomrom(treArr, i , 5), end='');
    print(fireArr[i] + " " * mellomrom(fireArr, i, 5), end='');
    print(femArr[i]);
#print(linjeNr(toArr));
