paper = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
cipertext="";
plaintext=raw_input("INPUT THE STRING YOU WANT TO BE ENCRYPTED: ");
encrypt_complex=input("ENCRYPT CODE (CHOOSE ANY NUMBER YOU WANT): ");
for i in plaintext:
    if i=="a":
        cipertext += paper[(0+encrypt_complex)%52];
    elif i=="b":
        cipertext += paper[(1+encrypt_complex)%52];
    elif i=="c":
        cipertext += paper[(2+encrypt_complex)%52];
    elif i=="d":
        cipertext += paper[(3+encrypt_complex)%52];
    elif i=="e":
        cipertext += paper[(4+encrypt_complex)%52];
    elif i=="f":
        cipertext += paper[(5+encrypt_complex)%52];    
    elif i=="g":
        cipertext += paper[(6+encrypt_complex)%52];    
    elif i=="h":
        cipertext += paper[(7+encrypt_complex)%52];    
    elif i=="i":
        cipertext += paper[(8+encrypt_complex)%52];    
    elif i=="j":
        cipertext += paper[(9+encrypt_complex)%52];    
    elif i=="k":
        cipertext += paper[(10+encrypt_complex)%52];    
    elif i=="l":
        cipertext += paper[(11+encrypt_complex)%52];    
    elif i=="m":
        cipertext += paper[(12+encrypt_complex)%52];    
    elif i=="n":
        cipertext += paper[(13+encrypt_complex)%52];    
    elif i=="o":
        cipertext += paper[(14+encrypt_complex)%52];    
    elif i=="p":
        cipertext += paper[(15+encrypt_complex)%52];    
    elif i=="q":
        cipertext += paper[(16+encrypt_complex)%52];    
    elif i=="r":
        cipertext += paper[(17+encrypt_complex)%52];    
    elif i=="s":
        cipertext += paper[(18+encrypt_complex)%52];    
    elif i=="t":
        cipertext += paper[(19+encrypt_complex)%52];    
    elif i=="u":
        cipertext += paper[(20+encrypt_complex)%52];    
    elif i=="v":
        cipertext += paper[(21+encrypt_complex)%52];    
    elif i=="w":
        cipertext += paper[(22+encrypt_complex)%52];    
    elif i=="x":
        cipertext += paper[(23+encrypt_complex)%52];    
    elif i=="y":
        cipertext += paper[(24+encrypt_complex)%52];    
    elif i=="z":
        cipertext += paper[(25+encrypt_complex)%52];    
    elif i=="A":
        cipertext += paper[(26+encrypt_complex)%52];        
    elif i=="B":
        cipertext += paper[(27+encrypt_complex)%52];        
    elif i=="C":
        cipertext += paper[(28+encrypt_complex)%52];        
    elif i=="D":
        cipertext += paper[(29+encrypt_complex)%52];        
    elif i=="E":
        cipertext += paper[(30+encrypt_complex)%52];        
    elif i=="F":
        cipertext += paper[(31+encrypt_complex)%52];
    elif i=="G":
        cipertext += paper[(32+encrypt_complex)%52];    
    elif i=="H":
        cipertext += paper[(33+encrypt_complex)%52];    
    elif i=="I":
        cipertext += paper[(34+encrypt_complex)%52];    
    elif i=="J":
        cipertext += paper[(35+encrypt_complex)%52];    
    elif i=="K":
        cipertext += paper[(36+encrypt_complex)%52];    
    elif i=="L":
        cipertext += paper[(37+encrypt_complex)%52];    
    elif i=="M":
        cipertext += paper[(38+encrypt_complex)%52];    
    elif i=="N":
        cipertext += paper[(39+encrypt_complex)%52];    
    elif i=="O":
        cipertext += paper[(40+encrypt_complex)%52];
    elif i=="P":
        cipertext += paper[(41+encrypt_complex)%52];    
    elif i=="Q":
        cipertext += paper[(42+encrypt_complex)%52];    
    elif i=="R":
        cipertext += paper[(43+encrypt_complex)%52];    
    elif i=="S":
        cipertext += paper[(44+encrypt_complex)%52];    
    elif i=="T":
        cipertext += paper[(45+encrypt_complex)%52];    
    elif i=="U":
        cipertext += paper[(46+encrypt_complex)%52];    
    elif i=="V":
        cipertext += paper[(47+encrypt_complex)%52];    
    elif i=="W":
        cipertext += paper[(48+encrypt_complex)%52];    
    elif i=="X":
        cipertext += paper[(49+encrypt_complex)%52];    
    elif i=="Y":
        cipertext += paper[(50+encrypt_complex)%52];    
    elif i=="Z":
        cipertext += paper[(51+encrypt_complex)%52];    
    elif i==" ":
        cipertext += "998";    
    elif i=="`":
        cipertext += "137"; 
    elif i=="~":
        cipertext += "158";    
    elif i=="!":
        cipertext += "908";
    elif i=="@":
        cipertext += "329";
    elif i=="#":
        cipertext += "701";
    elif i=="$":
        cipertext += "132";
    elif i=="%":
        cipertext += "796";
    elif i=="^":
        cipertext += "123";
    elif i=="&":
        cipertext += "984";
    elif i=="*":
        cipertext += "209";    
    elif i=="(":
        cipertext += "809";
    elif i==")":
        cipertext += "918";
    elif i=="-":
        cipertext += "102";
    elif i=="_":
        cipertext += "370";    
    elif i=="=":
        cipertext += "909";    
    elif i=="+":
        cipertext += "100";
    elif i=="{":
        cipertext += "210";
    elif i=="}":
        cipertext += "012";
    elif i=="[":
        cipertext += "219";
    elif i=="]":
        cipertext += "912";
    elif i=="\\":
        cipertext += "800";    
    elif i=="|":
        cipertext += "900";    
    elif i==";":
        cipertext += "300";
    elif i==":":
        cipertext += "400";
    elif i=="'":
        cipertext += "431";
    elif i=='"':
        cipertext += "450";
    elif i==",":
        cipertext += "200";
    elif i==".":
        cipertext += "250";
    elif i=="<":
        cipertext += "551";
    elif i==">":
        cipertext += "155";    
    elif i=="/":
        cipertext += "156";
    elif i=="?":
        cipertext += "157";
    elif i=="0":
        cipertext += "660";
    elif i=="1":
        cipertext += "661";    
    elif i=="2":
        cipertext += "662";    
    elif i=="3":
        cipertext += "663";
    elif i=="4":
        cipertext += "664";
    elif i=="5":
        cipertext += "665";        
    elif i=="6":
        cipertext += "666";    
    elif i=="7":
        cipertext += "667";    
    elif i=="8":
        cipertext += "668";    
    elif i=="9":
        cipertext += "669";    
rev=list(cipertext);
rev.reverse();
ciphertext="";
for j in range(0,len(rev)):
    ciphertext+=rev[j];
print("ENCRYPTED: "+ciphertext);
