def quiz():
     score=0
     print('--------------------------QUIZ--------------------------')
     print('TO EACH CORRECT ANSWER 10 POINTS WILL BE AWARDED')
     q1=input('''Q1. In which sport is the term "love" used?
     \na) Cricket
     \nb) Tennis
     \nc) Badminton
     \nd) Golf
     \nEnter the correct option(a,b,c,d):''')
     if q1=='b' or q1=='B':
          score=score+10
          print("CORRECT")
     else:
          print("CORRECT ANSWER IS TENNIS(B)")
          print("BETTER LUCK NEXT TIME")
     print("*********************************************************")
     q2=input('''Q2. The blue whale is the biggest known animal to have ever existed.
     \nEnter (T for true and F for False):''')
     if q2=='True' or q2=='T' or q2=="t" or q2=='TRUE':
          score=score+10
          print("CORRECT")
     else:
          print("CORRECT ANSWER IS TRUE")
          print("BETTER LUCK NEXT TIME")
     print("*********************************************************")
     q3=input('''Q3. Bats are blind and use ultrasound to determine their way while flying.
     \nEnter (T for true and F for False):''')
     if q3=='False' or q3=='f' or q3=="F" or q3=='FALSE':
          score=score+10
          print("CORRECT")
     else:
          print("CORRECT ANSWER IS FALSE")
          print('''Bats use echolocation to navigate, but they can see.''')
          print("BETTER LUCK NEXT TIME")
     print("*********************************************************")
     q4=input('''Q4. In which year did India gain independence from Britain?
     \na) 1950 
     \nb) 1947 
     \nc) 1962 
     \nd) 1971
     \nEnter the correct option(a,b,c,d):''')
     if q4=='b' or q4=='B':
          score=score+10
          print("CORRECT")
     else:
          print("CORRECT ANSWER IS 1947(B)")
          print("BETTER LUCK NEXT TIME")
     print("*********************************************************")
     q5=input('''Q5. The Amazon River is the longest river in the world.
     \nEnter (T for true and F for False):''')
     if q3=='False' or q3=='f' or q3=="F" or q3=='FALSE':
          score=score+10
          print("CORRECT")
     else:
          print("CORRECT ANSWER IS FALSE")
          print('''The Nile is often cited as the longest, though the Amazon is the largest by discharge volume.''')
          print("BETTER LUCK NEXT TIME")
     print("*********************************************************")
     print("TOTAL SCORE IS:",score)
     if score==50:
          print('''Perfect score! Congratulations on this fantastic result!
                \nYour general knowledge is truly impressive.
                \nKeep challenging yourself to learn and grow.''')
     elif score==40:
          print('''You were so close to a perfect score.
                \nUse this as motivation to push for that top mark next time!''')
     elif score==30:
          print('''This score is a great starting point.
          \nAnalyze your missed questions, and you'll easily see where you can make gains for next time''')
     elif score==20:
          print('''Don't be discouraged. An expert in anything was once a beginner. Keep at it!''')
     elif score==10:
          print('''The goal is learning, not just the score.
                \nA score of 10 means you started—and that is the first step towards getting better''')
     else:
          print('''Don't let this result define you.
             \nYour effort is what matters most, and that effort builds over time. Keep going!''')
     print('_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
     replay=input("Do you want to replay(y/n)?")
     L=replay.lower()
     if L=='yes' or L=='y':
          quiz()
     else:
          print("!!BYE!!")
quiz()

