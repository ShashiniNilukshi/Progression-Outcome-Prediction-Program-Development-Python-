#Name:Shashini Nilukshi
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
#Student ID-20221258
#Date-14/12/2022
Credits=int()
Defer=int()
Fail=int()

x=[0,20,40,60,80,100,120]
value_list=[]
Results_list=[]
All_list=[Results_list,value_list]
file=open('histogram.txt','w')
def lists ():
    value_list.append([Credits,Defer,Fail])
    Results_list.append(Results)
    
def files ():
    for x in zip(*All_list): #https://www.w3schools.com/python/ref_func_zip.asp
        file.write ("{0}-{1}\n".format(*x))
#Histrogram
progress_total=0
progress_module_total=0
Exclude_total=0
Do_not_progress_module_total=0


print("Choose Student mode or staff mode\n Student mode\t:1\n staff mode\t:2\n")
while True:
    try:
        mode=int(input("Choose the mode\t:"))
        if mode!=1 and mode!=2:
            print("Invalid input")
            continue
        break
    except ValueError:
        print("Integer Required")
        continue

while True:
    try:
        
    
  
        Credits=int(input("Please enter your credits at pass:"))
        if Credits not in x:
            print("Out of range.")
            continue
        Defer=int(input("Please enter your credit at defer:"))
        if Defer not in x:
            print("Out of range.")
            continue
        Fail=int(input("Please enter your credit at fail:"))
        if Fail not in x:
            print("Out of range.")
            continue
    except ValueError:
       print("Integer Required.")
       continue
    if Credits+Defer+Fail >120:
       print("Total incorrect")
       continue
    
       
    if Credits==120 and Defer==0 and Fail==0:
        print("Progress")
        Results="Progress"
        progress_total=progress_total+1
        lists ()
    elif (Credits==100 and Defer==20 and Fail==0) or (Credits==100 and Defer==0 and Fail==20):
        print("progress(module trailer)")
        Results="progress(module trailer)"
        progress_module_total=progress_module_total+1
        lists ()
    elif ( Credits==40 or Credits==20 or Credits==0 ) and (Defer==0 or Defer==20 or Defer==40) and (Fail==80 or Fail==100 or Fail==120):
        print("Exclude")
        Results="Exclude"
        Exclude_total=Exclude_total+1
        lists ()
    else:
        print("Do not progress-module retriever")
        Results="Do not progress-module retriever"
        Do_not_progress_module_total=Do_not_progress_module_total+1
        lists ()
    Total=progress_total+progress_module_total+Exclude_total+Do_not_progress_module_total
    if mode==1:
        break




    while True:
        yes_or_no=str(input("Would you like to enter another set of data?(Enter y for yes and q for quit):"))
        if yes_or_no !='y' and yes_or_no!= 'q':
            print("Invalid command")
            continue
        break
        
    if yes_or_no=="y":
        continue
    
        
    elif yes_or_no=="q":
         
        print("-"*50)
        print("Histrogram")
        print("Progress\t:",progress_total*"*","\n",end=(''))
        print("Trailer \t:",progress_module_total*"*","\n",end=(''))
        print("Excluded\t:",Exclude_total*"*","\n",end=(''))
        print("Retriever\t:",Do_not_progress_module_total*"*","\n",end=(''))
        print(Total,"outcomes in Total.")
        print("-"*50)




    files()
    file.close()
    file=open('histogram.txt','r')
    file_contenet=file.read()
    print(file_contenet)
    file.close()
    break
      
        














    
    
