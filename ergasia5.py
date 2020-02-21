import re
lista = []
lexi = []
string = ""
with open('keimeno.txt', 'r') as file:
    data = file.read().replace('\n', '') 
    print(data)
    lista = re.sub("[^\w]", " ",  data).split() # φτιαχνει λιστα με τις λεξεις του κειμενου χωρις να περιλαμβανει σημεια στιξης ουτε κενα
    a = len(lista)
    for i in range(0,a):
      
      string = lista[i] 
      b = len(string)
      if (b>3):
        lexi = list(string) # μετατρεπει τη λεξη σε λιστα χαρακτηρων
        c = lexi.pop(0)
        lexi.append(c)
        lexi.append("ay")
        string = ""
        for i in lexi:
          string += i # μετατρεπει τη λιστα χαρακτηρων σε λεξη
      print (string)
      