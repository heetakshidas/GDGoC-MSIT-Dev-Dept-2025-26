import random
import mysql.connector as m

mydb=m.connect(host="localhost",user="root",passwd="admin")
mycur=mydb.cursor()
mycur.execute("SHOW DATABASES")
show_dtbase=mycur.fetchall()
if ("todo",) not in show_dtbase:
     mycur.execute("create database todo")
mycur.execute("USE todo")

#to show the contents of the table
def to_do():
     mycur.execute("SHOW TABLES")
     tables=mycur.fetchall()
     if ("to_do_list",) in tables:
          mycur.execute("SELECT * FROM TO_DO_LIST")
          show=mycur.fetchall()
          no_rec=mycur.rowcount
          if no_rec==0:
               print("NO CONTENT IN THE TABLE")
          else:
               print("TASK\tDEADLINE\tLEVEL\tPOINTS\tMARK")
               for i in show:
                    print(i)
     else:
          print("NO TO_DO_LIST TABLE FOUND")
          
#to add tasks
def add_task():
     def adds():
          while True:
               task=input("ENTER THE TASK:")
               deadline=input("ENTER THE DEADLINE:")
               level=input("ENTER THE LEVEL(urgent,necessary,can wait,important):")
               insert_val='''INSERT INTO TO_DO_LIST(TASK,DEADLINE,LEVEL)VALUES("{}","{}",
                              "{}")'''.format(task,deadline,level)
               mycur.execute(insert_val)
               mydb.commit()
               d=input("DO YOU WANT TO ENTER MORE(Yy/Nn)?")
               if d in 'Yy':
                    continue
               else:
                    break
     n=input("Is your table created(y/n):")
     if n in 'yY':
          try:
               adds()
          except:
               print("CREATE THE TABLE FIRST")
     elif n in 'Nn':
          try:
               print("LETS CREATE THE TO_DO_LIST TABLE FIRST")
               mycur.execute('''CREATE TABLE TO_DO_LIST(TASK VARCHAR(200) primary key,DEADLINE VARCHAR(50),
                             LEVEL VARCHAR(50),POINTS INTEGER default 10,MARK VARCHAR(10))''')
               print("TO_DO_LIST TABLE CREATED")
               print("STRUCTURE OF TO_DO_LIST TABLE")
               mycur.execute("DESCRIBE TO_DO_LIST")
               desc=mycur.fetchall()
               for cont in desc:
                    print(cont)
          except:
               print("YOUR TABLE IS ALREADY CREATED")
               adds()
     else:
          print("Write in 'Yy' for yes and 'Nn' for No")
          print("TRY AGAIN to add details")
     
#to edit the content in the table    
def edit_task():
     while True:
          print("CHANGES IN")
          print("1.TASK")
          print("2.DEADLINE")
          print("3.LEVEL")
          print("4.POINTS")
          print("5.EXIT")
          q=int(input("ENTER NUMBER(1,2,3,4) TO MAKE A CHANGE:"))
          print("CONTENTS OF THE TABLE...FOR REFFERENCE") 
          mycur.execute("select * from TO_DO_LIST")
          rec=mycur.fetchall()
          for x in rec:
               print(x)
          if q==1:
               this=input("ENTER THE TASK YOU WANT TO CHANGE:")
               tpre=input("ENTER THE TASK YOU WANT TO REPLACE WITH THE CHANGE:")
               tupdate='''UPDATE TO_DO_LIST SET TASK="{}" where TASK="{}" '''.format(tpre,this)
               mycur.execute(tupdate)
          elif q==2:
               dhis=input("ENTER THE DEADLINE YOU WANT TO CHANGE:")
               dpre=input("ENTER THE DEADLINE YOU WANT TO REPLACE WITH THE CHANGE:")
               dupdate='''UPDATE TO_DO_LIST SET DEADLINE="{}" where DEADLINE="{}" '''.format(dpre,dhis)
               mycur.execute(dupdate)
          elif q==3:
               vhis=input("ENTER THE LEVEL YOU WANT TO CHANGE:")
               vpre=input("ENTER THE LEVEL YOU WANT TO REPLACE WITH THE CHANGE:")
               vupdate='''UPDATE TO_DO_LIST SET LEVEL="{}" where LEVEL="{}" '''.format(vpre,vhis)
               mycur.execute(vupdate)
          elif q==4:
               uhis=int(input("ENTER THE POINTS YOU WANT TO CHANGE:"))
               upre=int(input("ENTER THE POINTS YOU WANT TO REPLACE WITH THE CHANGE:"))
               cupdate='''UPDATE TO_DO_LIST SET POINTS={} where POINTS={} '''.format(upre,uhis)
               mycur.execute(cupdate)
          elif q==5:
               break
          else:
               print("INVALID INPUT....TRY AGAIN")
          mydb.commit()
          
#to delete the task
def delete_task():
     print("1.TO DELETE WHOLE TABLE")
     print("2.TO DELETE A (ROW FROM A TABLE)PARTICULAR TASK")
     print("NOTE!!!!!! BEFORE CHANGING ANY TASK...MAKE SURE TO WRITE AS IT IS GIVEN IN THE TABLE")
     dtq=int(input("ENTER(1 or 2):"))
     if dtq==1:
          mycur.execute('''DELETE FROM TO_DO_LIST''')
          print("TABLE IS DELETED")
     elif dtq==2:
          dq=input("ENTER THE TASK TO BE DELETED:")
          delete='''DELETE FROM TO_DO_LIST WHERE TASK="{}"'''.format(dq)
          mycur.execute(delete)
     else:
          print("INVALID")

#to sort task by level(IMPORTANT,URGENT,NECESSARY,CAN WAIT)
def check_level():
     print("1.TASKS WHICH ARE 'IMPORTANT'")
     print("2.TASKS WHICH ARE 'URGENT'")
     print("3.TASKS WHICH ARE 'NECESSARY'")
     print("4.TASKS WHICH ARE 'CAN WAIT'")
     say=int(input("Enter (1,2,3 or 4):"))
     if say==1:
          mycur.execute('''SELECT TASK FROM TO_DO_LIST WHERE LEVEL="IMPORTANT"''')
          imp=mycur.fetchall()
          for i in imp:
               print(i)
     elif say==2:
          mycur.execute('''SELECT TASK FROM TO_DO_LIST WHERE LEVEL="URGENT"''')
          urg=mycur.fetchall()
          for j in urg:
               print(j)
     elif say==3:
          mycur.execute('''SELECT TASK FROM TO_DO_LIST WHERE LEVEL="NECESSARY"''')
          nec=mycur.fetchall()
          for k in nec:
               print(k)
     elif say==4:
          mycur.execute('''SELECT TASK FROM TO_DO_LIST WHERE LEVEL="CAN WAIT"''')
          wait=mycur.fetchall()
          for m in wait:
               print(m)
     else:
          print("INVALID..TRY AGAIN")
          
#to mark the task           
def mark_task_complete():
     print("1.MARK TASK IN 'TO_DO_LIST' TABLE")
     print("2.MARK TASK IN 'multi_player_to_do' TABLE:")
     task_comp=int(input("ENTER (1/2):"))
     if task_comp==1:
          mark_task=input("Enter the task which should be marked:")
          mupdate='''UPDATE TO_DO_LIST SET MARK="DONE" WHERE TASK="{}"'''.format(mark_task)
          mycur.execute(mupdate)
          print("Task marked")
     elif task_comp==2:
          pswd=input("Enter password:")
          if pswd=="donut":
               mycur.execute("SELECT * FROM multi_player_to_do")
               ft=mycur.fetchall()
               for mu in ft:
                    print(mu)
               mark_task=input("Enter task to be marked:")
               mul_up='''UPDATE multi_player_to_do SET MARK="DONE" where task="{}"'''.format(mark_task)
               mycur.execute(mul_up)
               print("Task marked")
               print("CONGO!!")
          else:
               print("INCORRECT password")
     else:
          print("INVALID")
     mydb.commit()
#gamefication twist()
def gameie():
     print("1.!!TOTAL SCORE!!")
     print("2.PROGRESS REPORT")
     print("3.MOOD FRESH (2)GAMES")
     print("4.challenge")
     gamn=int(input("Enter the number(1,2,3 & 4):"))
     if gamn==1:
          mycur.execute('''SELECT SUM(POINTS) FROM TO_DO_LIST WHERE MARK="DONE"''')
          display_sum=mycur.fetchall()
          for i in display_sum:
               pass
          print("TOTAL SCORE:",i[0])
     elif gamn==2:
          mycur.execute('''SELECT sum(POINTS) FROM TO_DO_LIST WHERE MARK="DONE"''')
          sd=mycur.fetchall()
          for i in sd:
               pass
          mycur.execute('''SELECT sum(POINTS) FROM TO_DO_LIST''')
          total=mycur.fetchall()
          for j in total:
               pass
          avg=(i[0]/j[0])*100
          print("average perfomance:",avg)
          ####perfomance update comments#####
          if avg<=100 and avg>=90:
               print(''':D You should be very proud of this fantastic result.
                      \nKeep pushing your limits, and there's no telling what you'll achieve next.''')
          elif avg<90 and avg>=80:
               print('''*-* You are on an impressive track!
                     \nKeep pushing for that last bit of mastery, and nothing will be out of your reach.''')
          elif avg<80 and avg>=70:
               print(''':D Your consistent effort is admirable.
                     \nA little more confidence and pushing yourself outside of your comfort zone will make a big difference.''')
          elif avg<70 and avg>=60:
               print(''':D "Don't get discouraged.
                     \nYou are building momentum and with continued effort,you will find yourself moving up.
                     \nFocus on progress, not perfection.''')
          elif avg<60 and avg>=50:
               print( ''':D The results show you're capable of much more.
                        \nThe first step is always the hardest—let's keep going and focus on one topic at a time.''')
          elif avg<50 and avg>=40:
               print(''':D It’s not about how fast you go, as long as you don't stop.
                     \nEvery day is a new chance to learn and improve.
                     \nLet's start with a few small, achievable goals.''')
          else:
               print("work hard")
     elif gamn==3:
          import random
          nm=int(input("1.ODD EVEN GAME\n2.STONE,PAPER & SCISSOR\n ENTER(1/2):"))
          if nm==2:
               chanc=int(input("ENTER NUMBER OF ROUNDS:"))
               pnts=0
               pnts2=0
               while chanc>0:
                    chanc-=1
                    r=["stone","paper","scissor"]
                    st=input("ENTER(stone/paper/scissor):")
                    c=st.lower()
                    random_str=random.choice(r)
                    if c==random_str:
                         print("computer:",random_str)
                         print("SAME..NO POINTS")
                    elif c=="scissor" and random_str=="stone":
                         print("computer:",random_str)
                         pnts2=pnts2+10
                         print("computer WON")
                    elif c=="stone" and random_str=="scissor":
                         print("computer:",random_str)
                         pnts=pnts+10
                         print("YOU WON")
                    elif random_str=="scissor" and c=="paper":
                         print("computer:",random_str)
                         pnts2=pnts2+10
                         print("computer WON")
                    elif random_str=="paper" and c=="scissor":
                         print("computer:",random_str)
                         pnts=pnts+10
                         print("YOU WON")
                    elif random_str=="paper" and c=="stone":
                         print("computer:",random_str)
                         pnts2=pnts2+10
                         print("computer WON")
                    elif random_str=="stone" and c=="paper":
                         print("computer:",random_str)
                         pnts=pnts+10
                         print("YOU WON")
                    else:
                         print("ERROR..in the input")
                         print("'stone' or 'paper' or 'scissor'")
                         chanc=chanc+1
               print("YOUR TOTAL POINTS:",pnts)
               print("COMPUTER TOTAL POINTS:",pnts2)
               if pnts>pnts2:
                    print("!!YOU WON!!")
               elif pnts<pnts2:
                    print("COMPUTER WON")
               else:
                    print("same")
          elif nm==1:
               n=input(" Enter your name-")
               m=input(" Enter your enemy' s name-")
               while True:
                    try:
                         c=input("choose odd(O) or even(E):")
                         if (c in 'Ee') or (c in'Oo'):
                              break
                    except:
                         print("Sorry didn't get that...TRY AGAIN") 
               print("............LETS BEGIN...........")
               x=int(input("Enter a number(0 to 10)="))
               y=random.randint(0,10)
               print(m," Enter",y)
               if c in 'Ee':
                    if (x+y)%2==0:
                         print(n,"won")
                    else:
                         print(m," won")

               elif c in 'Oo':
                    if (x+y)%2==1:
                         print(n,"won")
                    else:
                         print(m,"won")
          else:
               print("INVALID..TRY AGAIN")
               
     elif gamn==4:
          import random
          print("!! CHALLENGE(ADD,SUB,MULTIPLY,DIVIDE) !!")
          def add(a,b):
               ans=a+b
               print(a,"+",b)
               user_ans=int(input("Enter the answer:"))
               if ans==user_ans:
                    print("GOOD JOB")
               else:
                    print("Correct answer is ",ans)
                    print("BETTER LUCK NEXT TIME")
          def sub(a,b):
               ans=a-b
               print(a,"-",b)
               user_ans=int(input("Enter the answer:"))
               if ans==user_ans:
                    print("GOOD JOB")
               else:
                    print("Correct answer is ",ans)
                    print("BETTER LUCK NEXT TIME")
          def mul(a,b):
               ans=a*b
               print(a,"*",b)
               user_ans=int(input("Enter the answer:"))
               if ans==user_ans:
                    print("GOOD JOB")
               else:
                    print("Correct answer is ",ans)
                    print("BETTER LUCK NEXT TIME")
          def div(a,b):
               ans=a/b
               print(a,"/",b)
               user_ans=int(input("Enter the answer:"))
               if ans==user_ans:
                    print("GOOD JOB")
                    s=s+10
               else:
                    print("Correct ans is ",ans)
                    print("BETTER LUCK NEXT TIME")
          L=int(input("1.(EASY)\n2.(MEDIUM)\n3.(HARD)\nENTER LEVEL:"))
          rounds=int(input("Enter the number of rounds :"))
          while rounds>0:
               rounds=rounds-1
               if L==1:
                    x=random.randint(0,20)
                    y=random.randint(0,20)
                    operator=random.choice(['+','-','*','/'])
                    if operator=="+":
                         add(x,y)
                    elif operator=="-":
                         sub(x,y)
                    elif operator=="*":
                         mul(x,y)
                    elif operator=="/":
                         div(x,y)
                    else:
                         print("----")
                    
               elif L==2:
                    x2=random.randint(20,50)
                    y2=random.randint(20,50)
                    operator=random.choice(['+','-','*','/'])
                    if operator=="+":
                         add(x2,y2)
                    elif operator=="-":
                         sub(x2,y2)
                    elif operator=="*":
                         mul(x2,y2)
                    elif operator=="/":
                         div(x2,y2)
                    else:
                         print("----")
                    
               elif L==3:
                    x3=random.randint(50,100)
                    y3=random.randint(50,100)
                    operator=random.choice(['+','-','*','/'])
                    if operator=="+":
                         add(x3,y3)
                    elif operator=="-":
                         sub(x3,y3)
                    elif operator=="*":
                         mul(x3,y3)
                    elif operator=="/":
                         div(x3,y3)
                    else:
                         print("----")
               else:
                    print("INVALID")
     else:
          print("INVALID")

#colaborative twist
def multi():
     print("BEFORE")
     mycur.execute('''SELECT * FROM multi_player_to_do''')
     s1=mycur.fetchall()
     for i in s1:
          print(i)
     friend1=input("Enter your NAME:")
     taskf=input("Enter TASK:")
     deadline=input("Enter deadline:")
     friend2=input("Enter NAME to whom you want to ASSIGN the task:")
     mycur.execute("show tables")
     show_tabl=mycur.fetchall()
     if ("multi_player_to_do",) not in show_tabl:
          mycur.execute('''create table multi_player_to_do(Friend1 varchar(100),TASK varchar(200),
                        Friend2 varchar(100),Deadline varchar(40),Mark varchar(10))''')
     ins='''INSERT INTO multi_player_to_do(friend1,task,friend2,deadline)VALUES
                         ("{}","{}","{}","{}")'''.format(friend1,taskf,friend2,deadline)
     mycur.execute(ins)
     mydb.commit()
     print("Done")
     mycur.execute('''SELECT * FROM multi_player_to_do''')
     s2=mycur.fetchall()
     for j in s2:
          print(j)
#-------------------------------MAIN PROGRAM-------------------------------
while True:
     print("****************************************************")
     print("1.TO SEE THE CONTENTS OF THE TABLE")
     print("2.TO ADD CONTENTS IN THE TO_DO_LIST TABLE")
     print("3.TO EDIT CONTENT IN THE TABLE")
     print("4.TO MARK THE TASK'DONE' IF COMPLETED")
     print("5.TO DELETE ANY TASK")
     print("6.FOR FIRENDS ASSIGNING TASK")
     print("7.GAMES AND PERFOMANCE")
     print("8.TO CHECK TASKS WHICH ARE (IMPORTANT,URGENT,NECESSARY,CAN WAIT)")
     print("9.EXIT")
     print("****************************************************")
     user=int(input("ENTER (1-8):"))
     if user==6:
          multi()
     elif user==7:
          gameie()
     elif user==1:
           to_do()
     elif user==2:
          add_task()
     elif user==5:
          delete_task()
     elif user==3:
          edit_task()
     elif user==4:
          mark_task_complete()
     elif user==8:
          check_level()
     elif user==9:
          break
     else:
          print("INVALID...TRY AGAIN")
