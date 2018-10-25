import os
import time
from datetime import date, timedelta
def home():
    d=open("e:/libms/text.txt","a")
    d.close()
    try:
        os.chdir("e:/")
        os.mkdir("libms")
        os.chdir("e:/libms")
    except:
        pass
    while(1):
        print("welcome to Library Management System".center(50,"*"))
        a=int(input('''enter a valid selection
1.Admin login
2.Admin register
3.Student login
4.Student register
0.EXIT\n'''))
        if a is 1:
              adlog()
        elif a is 2:
              adregister()
        elif a is 3:
              stdlog()
        elif a is 4:
              stdregister()
        elif a is 0:
              break
        else:
              print("Invalid selection")
def adlog():
              print("ADMIN Login".center(50,"-"))
              u=input("enter username\n")
              p=input("enter password\n")
              cred=u+','+p
              if cred in open("e:/libms/text.txt").read():
                  print("logged in")
                  adminblock()
              else:
                  print("incorrect credentials")
                  
def adregister():
              print("ADMIN Register ".center(50,"-"))
              eid=input("enter the employe id\n")
              u=input("enter username\n")
              p=input("enter password\n")
              x=open("e:/libms/text.txt").readlines()
              l=[i for i in x if i.split(',')[0]==eid]
              if len(l)==0:
                  open("e:/libms/text.txt","a").write(eid+','+u+','+p+'\n')
                  adlog()
              else:
                  print("employe id already exists\n")
                  adregister()
def stdlog():
              print("Student Login".center(50,"-"))
              u=input("enter username\n")
              p=input("enter password\n")
              cred=u+','+p
              if cred in open("e:/libms/stud.txt").read():
                  x=open("e:/libms/stud.txt").readlines()
                  l=[i.split(',')[0] for i in x if i.split(',')[1]==u and i.split(',')[2]==p+'\n']
                  sid=l[0]
                 
                  print("logged in")
                  secondsreen(sid)
              else:
                  print("incorrect credentials")
                  stdregister()
def stdregister():
              print("Student Register ".center(50,"-"))
              eid=input("enter the Student id\n")
              u=input("enter username\n")
              p=input("enter password\n")
              x=open("e:/libms/stud.txt").readlines()
              l=[i for i in x if i.split(',')[0]==eid]
              if len(l)==0:
                  open("e:/libms/stud.txt","a").write(eid+','+u+','+p+'\n')
                  stdlog()
              else:
                  print("Student id already exists\n")
                  stdregister()

def secondsreen(sid):
   while (1):
       print("WELCOME TO STUDENT PORTAL".center(50,"-"))  
       print("\nwelcome to Library Management System".center(50,"*"))
       print('''\n
1. BOOK ISSUE
2. BOOK RETURN
3. BOOK VIEW
4. FINE VIEW
0.EXIT''')
       a=int(input())
       if a is 1:
        issue(sid)
       elif a is 2:
            BookReturn(sid)
       elif a is 3:
          BookView(sid)
       elif a is 4:
           FineView(sid)
       elif a is 0:
           break
       else:
          print("invalid selection")

def issue(sid): 
     print("\nBOOK ISSUE PORTAL".center(50,'-'))
     name=input("\nenter book name\n")
     
     branch=input("enter branch\n")
     
     author=input("enter book author name\n")


     x=open('e:/libms/nonissue.txt','r').readlines()
     
     l=[i for i in x if i.split(',')[0]==name and i.split(',')[1]==branch and i.split(',')[2]==author and i.split(',')[3]!=0]
     
     if len(l)!=0:
          open('e:/libms/nonissue.txt','r').seek(0)
       
          curr_date=date.today().isoformat()
          return_date=returndate()
          data=open('e:/libms/nonissue.txt','r').read()
          open('e:/libms/nonissue.txt','w').write(data.replace(name+','+branch+','+author+','+l[0].split(',')[3],''))
          open('e:/libms/nonissue.txt','a').write(name+','+branch+','+author+','+str(int(l[0].split(',')[3])-1)+'\n')
                                        
          open('e:/libms/issue.txt','a').write(name+','+branch+','+author+','+sid+','+'1'+','+curr_date+','+returndate()+'\n')
          
          
     else:
         print("sorry this book is not available")
         
    
               

     
     secondsreen(sid)
     

############################################## BOOK VIEW ##############################################

    
def BookView(sid):
     print("List of available books".center(70,"-"))
     s=open('e:/libms/original.txt').readlines()
     for i in s:
         #print(i)
         for j in i.split(','):
             
            print(j,end='                    ')
         print('\n')   
     
     
     
     
##################################### FINE VIEW ##################################################

     
def FineView(sid):
     print("Fine View Portal".center(70,"-"))
     x=open('e:/libms/fine.txt').readlines()
     l=[i for i in x if i.split(',')[0]==sid]
     
     if len(l)!=0:
        print("your fine is :",sum([int(i.split(',')[1]) for i in l]))
     else:
         print("NO FINE")
     secondsreen(sid)


 ############################################ BOOK RETURN ########################################


     
def BookReturn(sid):
     print("BOOK RETURN PORTAL".center(50,'-'))
     name=input("\nenter book name\n")
     
     branch=input("enter branch\n")
     
     author=input("enter book author name\n")
     x=open('e:/libms/issue.txt','r').readlines()
     
     l=[i for i in x if i.split(',')[0]==name and i.split(',')[1]==branch and i.split(',')[2]==author and i.split(',')[3]==sid]
     print(l)
     if(len(l)!=0):
       curr=curr_date=date.today().isoformat()
       ret=l[0].split(',')[6]
      
       d1 = date(int(ret.split('-')[0]) , int(ret.split('-')[1]) , int(ret.split('-')[2]))
       d0 = date(int(curr.split('-')[0]) , int(curr.split('-')[1]) , int(curr.split('-')[2]))
       delta = d0 - d1
       print(ret)
       print(delta.days)
       if delta.days >0:
           open('e:/libms/fine.txt','a').write(sid+','+str(delta.days*100)+','+name+','+branch+','+author+'\n')  
       data=open('e:/libms/issue.txt','r').read()
       open('e:/libms/issue.txt','w').write(data.replace(l[0] , ''))  
       nonissudata=open('e:/libms/nonissue.txt','r').readlines()
       
       l1=[i for i in nonissudata if i.split(',')[0]==name and i.split(',')[1]==branch and i.split(',')[2]==author]
       
       open('e:/libms/nonissue.txt','r').seek(0)
       
       
       
       data=open('e:/libms/nonissue.txt','r').read()
       open('e:/libms/nonissue.txt','w').write(data.replace(name+','+branch+','+author+','+l1[0].split(',')[3],''))
       open('e:/libms/nonissue.txt','a').write(name+','+branch+','+author+','+str(int(l1[0].split(',')[3])+1)+'\n')
     else:
         print("no book is issued on this student id")
     secondsreen(sid)



######################################### RETURN DATE ############################################
def returndate():
    days_after = (date.today()+timedelta(days=10)).isoformat()
    return days_after



   ####################################### ADMIN BLOCK#####################################################  
def adminblock():
  while(1):
      print("WELCOME TO ADMIN PORTAL".center(50,"-"))
      print("\nenter valid selection")
      print('''\n1.ADD BOOKS
2.CALCULATE FINE
3.GROUPING BOOK
4.FINE COLLECTED
5.DELETE BOOK
0.EXIT\n''')
      a=input()
      if a=='1':
        adbook()
      
      elif a=='2':
        calulatefine()
      elif a=='3':
        group()
      elif a=='4':
        collected()
      elif a=='5':
          deletebook()
      elif a=='0':
         break
      else:
        print("invalid selection")
        
  ####################################### ADD BOOKS ################################

        
    
def adbook():
    print("ADD BOOK PORTAL".center(50,"-"))
    name=input('\nEnter Book Name\n')
    branch=input('Enter branch\n')
    author=input('Enter author name\n')
    quantity=input('Enter quantity\n')
    open('e:/libms/nonissue.txt','a').write(name+','+branch+','+author+','+quantity+'\n')
    open('e:/libms/original.txt','a').write(name+','+branch+','+author+','+quantity+'\n')
    adminblock()


############################### CALCULATE FINE #############################

def calulatefine():
    print("CALCULATE FINE PER STUDENT PORTAL ".center(50,"-"))
    print("\nCalculate fine\n")
    id=input("Enter Student ID")
    x=open('e:/libms/fine.txt').readlines()
    
    l=[i for i in x if i.split(',')[0]==id]
    #print(l)
    if len(l)!=0:
       print("fine is:  ",sum(l.split(',')[1] for i in l))
    else:
        print("no fine")
    adminblock()

################################## GROUPING OF BOOKS #############################

    
def group():
    branch=input('\nEnter branch\n')
    x=open('e:/libms/original.txt').readlines()
    d={}
    l=[[i.split(',')[2],i.split(',')[3]] for i in x if i.split(',')[1]==branch]
    for i in l:
        d[i[0]]=i[1]
        
    print("total book for ",branch+' :',len(l)  )
    author=input('Enter author name\n')
    if author in d:
        print("\nno of books for Author name ", author+' :',d[author])
    else:
        print("\nthis author book is not available")
    adminblock()


################################# FINE COLLECTED ###################################


def collected():
     print("TOTAL COLLECTED FINE".center(50,"-"))
     x=open('e:/libms/fine.txt').readlines()
     
     l=[int(i.split(',')[1]) for i in x if i.split(',')[0] is not '\n']
     if len(l) is not 0: 
       print("\ntoal collected fine :",sum(l))
     else:
         print("\nno fine collected")
     adminblock()

################################# DELETE BOOKS

     
def deletebook():
    print("DELETE BOOK PORTAL".center(50,"-"))
    name=input("\nenter book name\n")
    branch=input("enter branch name\n")
    author=input("enter author name\n")
    y=open('e:/libms/issue.txt').readlines()
    l1=[i for i in y if i.split(',')[0]==name and i.split(',')[1]==branch and i.split(',')[2]==author]
    if len(l1)==0:
      x=open('e:/libms/original.txt').readlines()
      l=[i for i in x if i.split(',')[0]==name and i.split(',')[1]==branch and i.split(',')[2]==author]
      y=open('e:/libms/original.txt').readlines()
      l2=[i for i in x if i.split(',')[0]==name and i.split(',')[1]==branch and i.split(',')[2]==author]
     
      if len(l)!=0:
        open('e:/libms/original.txt').seek(0)
        data=open('e:/libms/original.txt').read()
        open('e:/libms/original.txt','w').write(data.replace(name+','+branch+','+author+','+l[0].split(',')[3] , ''))
        open('e:/libms/nonissue.txt').seek(0)
        data=open('e:/libms/nonissue.txt').read()
        open('e:/libms/nonissue.txt','w').write(data.replace(name+','+branch+','+author+','+l2[0].split(',')[3] , ''))
      else:
         print("enter valid book details")
    
    else:
        print("this book you can not delete")
home()
              

          
