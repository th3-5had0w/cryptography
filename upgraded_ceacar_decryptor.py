paper = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
plaintext="";
ciphertext=raw_input("INPUT THE STRING YOU WANT TO BE DECRYPTED: ");
decrypt_complex=input("DECRYPT CODE (CHOOSE ANY NUMBER YOU WANT): ");
ciphertext_re=ciphertext.replace("899"," ").replace("731","`").replace("851","~").replace("809","!").replace("923","@").replace("107","#").replace("231","$").replace("697","%").replace("321","^").replace("489","&").replace("902","*").replace("908","(").replace("819",")").replace("201","-").replace("073","_").replace("909","=").replace("001","+").replace("012","{").replace("210","}").replace("912","[").replace("219","]").replace("008","\\").replace("009","|").replace("003",";").replace("004",":").replace("134","'").replace("054",'"').replace("002",",").replace("052",".").replace("155","<").replace("551",">").replace("651","/").replace("751","?").replace("066","0").replace("166","1").replace("266","2").replace("366","3").replace("466","4").replace("566","5").replace("666","6").replace("766","7").replace("866","8").replace("966","9");
rev=list(ciphertext_re);
rev.reverse();
for i in range(0,len(rev)):
    if rev[i]=="a":
        if 0-(decrypt_complex%52)<0:
            plaintext+=paper[0-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[0-(decrypt_complex%52)];
    elif rev[i]=="b":
        if 1-(decrypt_complex%52)<0:
            plaintext+=paper[1-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[1-(decrypt_complex%52)];
    elif rev[i]=="c":
        if 2-(decrypt_complex%52)<0:
            plaintext+=paper[2-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[2-(decrypt_complex%52)];    
    elif rev[i]=="d":
        if 3-(decrypt_complex%52)<0:
            plaintext+=paper[3-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[3-(decrypt_complex%52)];    
    elif rev[i]=="e":
        if 4-(decrypt_complex%52)<0:
            plaintext+=paper[4-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[4-(decrypt_complex%52)];    
    elif rev[i]=="f":
        if 5-(decrypt_complex%52)<0:
            plaintext+=paper[5-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[5-(decrypt_complex%52)];    
    elif rev[i]=="g":
        if 6-(decrypt_complex%52)<0:
            plaintext+=paper[6-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[6-(decrypt_complex%52)];    
    elif rev[i]=="h":
        if 7-(decrypt_complex%52)<0:
            plaintext+=paper[7-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[7-(decrypt_complex%52)];    
    elif rev[i]=="i":
        if 8-(decrypt_complex%52)<0:
            plaintext+=paper[8-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[8-(decrypt_complex%52)];    
    elif rev[i]=="j":
        if 9-(decrypt_complex%52)<0:
            plaintext+=paper[9-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[9-(decrypt_complex%52)];    
    elif rev[i]=="k":
        if 10-(decrypt_complex%52)<0:
            plaintext+=paper[10-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[10-(decrypt_complex%52)];    
    elif rev[i]=="l":
        if 11-(decrypt_complex%52)<0:
            plaintext+=paper[11-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[11-(decrypt_complex%52)];    
    elif rev[i]=="m":
        if 12-(decrypt_complex%52)<0:
            plaintext+=paper[12-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[12-(decrypt_complex%52)];    
    elif rev[i]=="n":
        if 13-(decrypt_complex%52)<0:
            plaintext+=paper[13-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[13-(decrypt_complex%52)];    
    elif rev[i]=="o":
        if 14-(decrypt_complex%52)<0:
            plaintext+=paper[14-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[14-(decrypt_complex%52)];    
    elif rev[i]=="p":
        if 15-(decrypt_complex%52)<0:
            plaintext+=paper[15-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[15-(decrypt_complex%52)];    
    elif rev[i]=="q":
        if 16-(decrypt_complex%52)<0:
            plaintext+=paper[16-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[16-(decrypt_complex%52)];    
    elif rev[i]=="r":
        if 17-(decrypt_complex%52)<0:
            plaintext+=paper[17-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[17-(decrypt_complex%52)];    
    elif rev[i]=="s":
        if 18-(decrypt_complex%52)<0:
            plaintext+=paper[18-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[18-(decrypt_complex%52)];    
    elif rev[i]=="t":
        if 19-(decrypt_complex%52)<0:
            plaintext+=paper[19-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[19-(decrypt_complex%52)];    
    elif rev[i]=="u":
        if 20-(decrypt_complex%52)<0:
            plaintext+=paper[20-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[20-(decrypt_complex%52)];    
    elif rev[i]=="v":
        if 21-(decrypt_complex%52)<0:
            plaintext+=paper[21-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[21-(decrypt_complex%52)];    
    elif rev[i]=="w":
        if 22-(decrypt_complex%52)<0:
            plaintext+=paper[22-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[22-(decrypt_complex%52)];    
    elif rev[i]=="x":
        if 23-(decrypt_complex%52)<0:
            plaintext+=paper[23-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[23-(decrypt_complex%52)];    
    elif rev[i]=="y":
        if 24-(decrypt_complex%52)<0:
            plaintext+=paper[24-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[24-(decrypt_complex%52)];    
    elif rev[i]=="z":
        if 25-(decrypt_complex%52)<0:
            plaintext+=paper[25-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[25-(decrypt_complex%52)];    
    elif rev[i]=="A":
        if 26-(decrypt_complex%52)<0:
            plaintext+=paper[26-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[26-(decrypt_complex%52)];    
    elif rev[i]=="B":
        if 27-(decrypt_complex%52)<0:
            plaintext+=paper[27-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[27-(decrypt_complex%52)];    
    elif rev[i]=="C":
        if 28-(decrypt_complex%52)<0:
            plaintext+=paper[28-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[28-(decrypt_complex%52)];    
    elif rev[i]=="D":
        if 29-(decrypt_complex%52)<0:
            plaintext+=paper[29-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[29-(decrypt_complex%52)];    
    elif rev[i]=="E":
        if 30-(decrypt_complex%52)<0:
            plaintext+=paper[30-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[30-(decrypt_complex%52)];    
    elif rev[i]=="F":
        if 31-(decrypt_complex%52)<0:
            plaintext+=paper[31-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[31-(decrypt_complex%52)];    
    elif rev[i]=="G":
        if 32-(decrypt_complex%52)<0:
            plaintext+=paper[32-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[32-(decrypt_complex%52)];    
    elif rev[i]=="H":
        if 33-(decrypt_complex%52)<0:
            plaintext+=paper[33-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[33-(decrypt_complex%52)];    
    elif rev[i]=="I":
        if 34-(decrypt_complex%52)<0:
            plaintext+=paper[34-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[34-(decrypt_complex%52)];    
    elif rev[i]=="J":
        if 35-(decrypt_complex%52)<0:
            plaintext+=paper[35-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[35-(decrypt_complex%52)];    
    elif rev[i]=="K":
        if 36-(decrypt_complex%52)<0:
            plaintext+=paper[36-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[36-(decrypt_complex%52)];    
    elif rev[i]=="L":
        if 37-(decrypt_complex%52)<0:
            plaintext+=paper[37-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[37-(decrypt_complex%52)];    
    elif rev[i]=="M":
        if 38-(decrypt_complex%52)<0:
            plaintext+=paper[38-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[38-(decrypt_complex%52)];    
    elif rev[i]=="N":
        if 39-(decrypt_complex%52)<0:
            plaintext+=paper[39-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[39-(decrypt_complex%52)];    
    elif rev[i]=="O":
        if 40-(decrypt_complex%52)<0:
            plaintext+=paper[40-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[40-(decrypt_complex%52)];    
    elif rev[i]=="P":
        if 41-(decrypt_complex%52)<0:
            plaintext+=paper[41-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[41-(decrypt_complex%52)];    
    elif rev[i]=="Q":
        if 42-(decrypt_complex%52)<0:
            plaintext+=paper[42-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[42-(decrypt_complex%52)];    
    elif rev[i]=="R":
        if 43-(decrypt_complex%52)<0:
            plaintext+=paper[43-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[43-(decrypt_complex%52)];    
    elif rev[i]=="S":
        if 44-(decrypt_complex%52)<0:
            plaintext+=paper[44-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[44-(decrypt_complex%52)];    
    elif rev[i]=="T":
        if 45-(decrypt_complex%52)<0:
            plaintext+=paper[45-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[45-(decrypt_complex%52)];    
    elif rev[i]=="U":
        if 46-(decrypt_complex%52)<0:
            plaintext+=paper[46-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[46-(decrypt_complex%52)];    
    elif rev[i]=="V":
        if 47-(decrypt_complex%52)<0:
            plaintext+=paper[47-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[47-(decrypt_complex%52)];    
    elif rev[i]=="W":
        if 48-(decrypt_complex%52)<0:
            plaintext+=paper[48-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[48-(decrypt_complex%52)];    
    elif rev[i]=="X":
        if 49-(decrypt_complex%52)<0:
            plaintext+=paper[49-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[49-(decrypt_complex%52)];    
    elif rev[i]=="Y":
        if 50-(decrypt_complex%52)<0:
            plaintext+=paper[50-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[50-(decrypt_complex%52)];    
    elif rev[i]=="Z":
        if 51-(decrypt_complex%52)<0:
            plaintext+=paper[51-(decrypt_complex%52)+52];
        else:
            plaintext+=paper[51-(decrypt_complex%52)];    
    elif rev[i]=="~":
        plaintext+="~";
    elif rev[i]=="`":
        plaintext+="`";    
    elif rev[i]=="!":
        plaintext+="!";
    elif rev[i]=="@":
        plaintext+="@";
    elif rev[i]=="#":
        plaintext+="#";
    elif rev[i]=="$":
        plaintext+="$";
    elif rev[i]=="%":
        plaintext+="%";
    elif rev[i]=="^":
        plaintext+="^";
    elif rev[i]=="&":
        plaintext+="&";
    elif rev[i]=="*":
        plaintext+="*";
    elif rev[i]=="(":
        plaintext+="(";    
    elif rev[i]==")":
        plaintext+=")";
    elif rev[i]=="-":
        plaintext+="-";
    elif rev[i]=="_":
        plaintext+="_";
    elif rev[i]=="=":
        plaintext+="=";
    elif rev[i]=="+":
        plaintext+="+";
    elif rev[i]=="{":
        plaintext+="{";
    elif rev[i]=="}":
        plaintext+="}";
    elif rev[i]=="[":
        plaintext+="[";
    elif rev[i]=="]":
        plaintext+="]";
    elif rev[i]=="\\":
        plaintext+="\\";
    elif rev[i]=="|":
        plaintext+="|";
    elif rev[i]==";":
        plaintext+=";";
    elif rev[i]==":":
        plaintext+=":";
    elif rev[i]=="'":
        plaintext+="'";
    elif rev[i]=='"':
        plaintext+='"';
    elif rev[i]==",":
        plaintext+=",";
    elif rev[i]=="<":
        plaintext+="<";
    elif rev[i]==">":
        plaintext+=">";
    elif rev[i]==".":
        plaintext+=".";
    elif rev[i]=="/":
        plaintext+="/";
    elif rev[i]=="?":
        plaintext+="?";
    elif rev[i]==" ":
        plaintext+=" ";
    elif rev[i]=="0":
        plaintext+="0";    
    elif rev[i]=="1":
        plaintext+="1";
    elif rev[i]=="2":
        plaintext+="2";
    elif rev[i]=="3":
        plaintext+="3";
    elif rev[i]=="4":
        plaintext+="4";
    elif rev[i]=="5":
        plaintext+="5";
    elif rev[i]=="6":
        plaintext+="6";
    elif rev[i]=="7":
        plaintext+="7";
    elif rev[i]=="8":
        plaintext+="8";
    elif rev[i]=="9":
        plaintext+="9";    
print("DECRYPTED: "+plaintext);