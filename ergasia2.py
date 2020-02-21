import re
list = []
string = ""
with open('keimeno_gia_ergasia2.txt', 'r') as file:
    data = file.read().replace('\n', '') 
    
    list = re.sub("[^\w]", " ",  data).split() # φτιαχνει λιστα με τις λεξεις του κειμενου χωρις να περιλαμβανει σημεια στιξης ουτε κενα
    a = len(list)
    for i in range(0,a):
      points = 0
      sumfwna = 0
      string = list[i] 
      b = len(string)
      for j in range(0,b):
        ch = string[j] # χωριζει τη καθε λεξη σε χαρακτηρες
        if(ch !='A' and ch !='a' and ch !='E' and ch !='e' and ch!='I' and ch!='i' and ch!='O' and ch!='o' and ch!='U' and ch!='u'): # βρισκει των αριθμο των συμφωνων
          sumfwna = sumfwna + 1
        if (ch=="f" or ch=="c" or ch=="r" or ch=="k"): # κανει ελεγχο για καθε χαρακτηρα
          points = points + 1
      if (points > (sumfwna - points)):    # ελεγχει αν τα συμφωνα f,c,k,r ειναι περισσοτερα των αλλων
        print(string,"Η λεξη ειναι κακια")
      else:
        print(string,"Η λεξη ειναι καλη")