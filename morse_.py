from playsound import playsound
import time
#two lists
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','','']
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/',' ','']
while True:
    time.sleep(0.5)
    twopaths = input("d for decrypt and e for encrypt: ")
    output = ""
    if twopaths == 'e':
        encrpt = list(input("lowercase letters: "))
        for i in encrpt:
            output = output + morse[alphabet.index(i)] + " "
        print(output)
    
    else:
        dcrpt = str(input("put morse code here: "))
        dcrpt_chunk = dcrpt.split(" ")
        for i in dcrpt_chunk:
            output = output + alphabet[morse.index(i)]
        print(output)

        for i in dcrpt:
            print(i)
            if i == ".":
                playsound("Documents/bep.wav")
            if i == "-":
                playsound("Documents/beeep.wav")
            if i == "/":
                playsound("Documents/beep_break.wav")
            if i == " ":
                time.sleep(0.2)
