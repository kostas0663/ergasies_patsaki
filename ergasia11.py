with open('numbers.txt') as f:
    x = [] # λιστα που περιεχει τις τετραδες απο το αρχειο .txt
    for line in f:
        line = line.split()  # για να μην συμπεριλαβει τα \n
        if line:            
            line = [int(i) for i in line]
          
            x.append(line)
print('δωστε 6 διαφορετικους αριθμους απο το 1 μεχρι το 9')
exada=[] # λιστα που περιεχει του αριθμους τησ εξαδας
for i in range(1,7):
 j= input("")
 exada.append(j)
c = [] # λιστα που περιεχει τις τετραδες απο το αρχειο .txt αφου χωριστουν σε ψηφια ( πχ c[0]-c[3] ειναι η πρωτη τετραδα)
a = len(x)
for k in x:
  b = str(k)
  b = b[1:-1] # για να αφαιρεθουν οι αγκυλες
  for digit in b:
    c.append(digit)
points = 0  
end = 0     # για να σταματησουν οι υπολοιποι ελεγχοι αν βρεθει τετραδα
for tetrada in range(0,a*4,4): # ελεγχει αν οι πρωτοι τεσσερις αριθμοι προτιμησης ταιριαζουν με τετραδα
  points = 0
  for i in range (tetrada,tetrada+4):
    for n in range (0,4):
      if (exada[n]==c[i]):
        points = points + 1
      else:
        points = points
  if (points==4):
    print("H τετραδα σου ειναι η:"+c[tetrada]+","+c[tetrada+1]+","+c[tetrada+2]+","+c[tetrada+3])
    end = 999
if (end==0): # ελεγχει αν οι πρωτοι τρεις αριθμοι ταιριαζουν με αριθμουσ τησ τετραδας και μετα δοκιμαζει τον πεμπτο και τον εκτο
  
  for tetrada in range(0,a*4,4):    # η καθε τετραδα πιανει τεσσερις θεσεις τησ λιστας c
    points = 0
    for i in range (tetrada,tetrada+4):
      for n in range (0,4):
        if (exada[n]==c[i]):
          points = points + 1
        else:
          points = points
    if (points==3 and exada[3]!=c[tetrada] and exada[3]!=c[tetrada+1] and exada[3]!=c[tetrada+2] and exada[3]!=c[tetrada+3]):
      for m in range (tetrada,tetrada+4):
        for n in range (4,6):
          if (exada[n]==c[m]):
            print("H τετραδα σου ειναι η:"+c[tetrada]+","+c[tetrada+1]+","+c[tetrada+2]+","+c[tetrada+3])
            end = 999
  if (end==0):  # ελεγχει αν οι δυο πρωτοι και ο τεταρτος αριθμος προτιμησης ταιριαζουν με τετραδα και μετα δοκιμαζει τον πεμπτο και τον εκτο
    for tetrada in range(0,a*4,4):
      points = 0
      for i in range (tetrada,tetrada+4):
        for n in range (0,4):
          if (exada[n]==c[i]):
            points = points + 1
          else:
           points = points
      if (points==3 and exada[2]!=c[tetrada] and exada[2]!=c[tetrada+1] and exada[2]!=c[tetrada+2] and exada[2]!=c[tetrada+3]):
       for m in range (tetrada,tetrada+4):
         for n in range (4,6):
           if (exada[n]==c[m]):
              print("H τετραδα σου ειναι η:"+c[tetrada]+","+c[tetrada+1]+","+c[tetrada+2]+","+c[tetrada+3])
              end = 999
         
  if (end==0):  # ελεγχει αν ο πρωτος ο τριτος και ο τεταρτος αριθμος προτιμησης ταιριαζουν με τετραδα και μετα δοκιμαζει τον πεμπτο και τον εκτο
    for tetrada in range(0,a*4,4):
      points = 0
      for i in range (tetrada,tetrada+4):
        for n in range (0,4):
          if (exada[n]==c[i]):
            points = points + 1
          else:
            points = points
      if (points==3 and exada[1]!=c[tetrada] and exada[1]!=c[tetrada+1] and exada[1]!=c[tetrada+2] and exada[1]!=c[tetrada+3]):
        for m in range (tetrada,tetrada+4):
          for n in range (4,6):
           if (exada[n]==c[m]):
              print("H τετραδα σου ειναι η:"+c[tetrada]+","+c[tetrada+1]+","+c[tetrada+2]+","+c[tetrada+3])
              end = 999
         
  if (end==0):  # ελεγχει αν ο δευτερος ο τριτος και ο τεταρτος αριθμος προτιμησης ταιριαζουν με τετραδα και μετα δοκιμαζει τον πεμπτο και τον εκτο
    for tetrada in range(0,a*4,4):
      points = 0
      for i in range (tetrada,tetrada+4):
        for n in range (0,4):
          if (exada[n]==c[i]):
            points = points + 1
          else:
            points = points
      if (points==3 and exada[0]!=c[tetrada] and exada[0]!=c[tetrada+1] and exada[0]!=c[tetrada+2] and exada[0]!=c[tetrada+3]):
        for m in range (tetrada,tetrada+4):
          for n in range (4,6):
           if (exada[n]==c[m]):
              print("H τετραδα σου ειναι η:"+c[tetrada]+","+c[tetrada+1]+","+c[tetrada+2]+","+c[tetrada+3])
              end = 999
         
  if (end==0): # ελεγχει αν δυο απο τους τεσσερις αριθμους προτιμησης ταιριαζουν με τετραδα και μετα δοκιμαζει αν ταιριαζουν και ο πεμπτος και ο εκτος
    for tetrada in range(0,a*4,4):
      points = 0
      for i in range (tetrada,tetrada+4):
        for n in range (0,4):
          if (exada[n]==c[i]):
            points = points + 1
          else:
            points = points
      if (points==2):
        for m in range (tetrada,tetrada+4):
          for n in range (4,6):
            if (exada[n]==c[m]):
              points = points + 1
              if (points==4 and end!=999):
               print("H τετραδα σου ειναι η:"+c[tetrada]+","+c[tetrada+1]+","+c[tetrada+2]+","+c[tetrada+3])
               end = 999
if (end==0): # Αν γινουν ολοι οι ελεγχοι και δεν βρεθει τετραδα
  print("Δεν υπαρχει διαθεσιμη τετραδα")