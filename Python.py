print('                             100 Game')
while True:
    sum=0
    count=0

    q=int(input('How many players will play ?'))
    if q==1:
        h=int(input('Hard game please enter 1 OR easy game please enter 2 : '))

    while q==2:
        #2players

              x=int(input('player 1 please enter number : '))
              while x>10 or x==0 or x<0:
                 print('Error please enter number from 1 to 10')
                 x=int(input('player 1 please enter number : '))
              sum=sum+x
              while sum>100 or x>10 or x==0 or x<0:
                  sum=sum-x
                  x=int(input('you cannot make sum > 100 please enter different number : '))
                  sum=sum+x
              print('sum = ',sum)
              if sum==100:
                 print ('player1 is the winner')
                 break

              y=int(input('player 2 please enter number : '))
              while y>10 or y==0 or y<0:
                  print('Error please enter number from 1 to 10')
                  y=int(input('player 2 please enter number : '))
            
              sum=sum+y
              while sum>100 or y>10 or y==0 or y<0:
                  sum=sum-y
                  y=int(input('you cannot make sum > 100 please enter different number : '))
                  sum=sum+y
              print('sum = ',sum)
              if sum==100:
                 print('player2 is the winner')
                 break
    while q==1:
         
         if h==1:
             #Hard
                  x=int(input('player 1 please enter number : '))
                  while x>10 or x==0 or x<0:
                      print('Error please enter number from 1 to 10')
                      x=int(input('player 1 please enter number : '))
                  sum=sum+x
                  while sum>100 or x>10 or x==0 or x<0:
                      sum=sum-x
                      x=int(input('you cannot make sum > 100 please enter different number : '))
                      sum=sum+x
                  
                  
                  
                  print ('sum = ',sum) 
                  if sum>=100:
                     print('player1 is the winner')
                     break
                  if count==7:
                      y=90-sum-1

                  else:
                      y=11-x
                  count+=1

                  print ('computer number = ',y)
                
                  sum=sum+y
                  print ('sum = ',sum)
                  
                  if sum>=100:
                     print('computer is the winner')
                     break
         elif h==2 :
                  #Easy
                  import random
                  y=random.randint(1,10)

                  print ('computer number = ',y)
                        
                  sum=sum+y
                  print ('sum = ',sum)
                     
                  if sum>=100:
                     print('computer is the winner')
                     break

                    
                  x=int(input('player 1 please enter number : '))
                  while x>10 or x==0 or x<0:
                      print('Error please enter number from 1 to 10')
                      x=int(input('player 1 please enter number : '))
                  sum=sum+x
                  while sum>100 or x>10 or x==0 or x<0:
                      sum=sum-x
                      x=int(input('you cannot make sum > 100 please enter different number : '))
                      sum=sum+x
                  
                  print ('sum = ',sum) 
                  if sum>=100:
                     print('player1 is the winner')
                     break
    m=int(input("play again=1 && exit=2: "))
    while m!=1 and m!=2:
        print("no more option")
        m=int(input("play again=1 && exit=2: "))
    if m==2:
        break
