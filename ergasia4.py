def metatropiSseASC():

       print('Dose string')
       string = input ()
       a = len(string)
       arithmos = 0 
       sum= ""
       for i in range(0,a):
 
          Num = string[i]
          Num =  ord(Num) # μετατρεπει καθε χαρακτηρα σε ascii
          sum =  sum + str(Num) #ενωνει τα ascii ως string για να μην προσθετονται μεταξυ τους 
          arithmos = int(sum,10) # μετατρεπει το τελικο string σε ακεραιο για να ελεγξει  επειτα αν ειναι πρωτος η συνθετος
       print (arithmos)
       c = 0
       for j in range(2,arithmos) : 
          if arithmos%j == 0 :
              c = 1
       if c == 0 :
           print (arithmos,' einai prwtos')
       else :
           print (arithmos,' einai synthetos')
      
       
     
metatropiSseASC()


       


