f=open("srmtimetable.txt","r")
#print(f.read(50))
d=f.read()
#print(len(d))
room=1
print("\t CLASSROOM ALLOCATOR FOR SRM UNIVERSITY AMARAVATI\n")
print("Press 1 To Search in Day order wise\n")
print("Press 2 To Search Day Order according to specific class hours\n")
check=int(input("Please Enter Your Input:\n"))
room1=[201,202,205,206,207,208,209,"405a","406a",204,302,307,308,401,402,405,406,407,408,501,502,503,301,601,602]

def time(n,room):
    j=0
    for i in range(len(d)):
        if(d[i]=="\n") and(i!=len(d)-1):
            if(d[i+1]=="\n"):
                #print(i)
                print("Checking room number: ",room1[j])
                j=j+1
                k=(80*(room-1))+(2+(room-1))
                k=k+(16*(n-1))
                room=room+1
                for i in range(k,k+15):
                    if(d[i]=='0'):
                            #print(i)
                            print("Room is free during class hour: ",int((i-k)/2)+1)
def time1(n,m,room):
    j=0
    for i in range(len(d)):
        if(d[i]=="\n") and(i!=len(d)-1):
            if(d[i+1]=="\n"):
                #print(i)
                print("Checking room number: ",room1[j])
                j=j+1
                k=(80*(room-1))+(2+(room-1))
                k=k+(16*(n-1))
                room=room+1
                i=k+(m-1)*2
                if(d[i]=='0'):
                    #print(i)
                    print("Room is free during class hour: ",int((i-k)/2)+1)

    
if(check==1):
    n=int(input("Enter The Day Order You Want to check: "))
    time(n,room)
elif(check==2):
    n=int(input("Enter The Day Order You Want: "))
    m=int(input("Enter The class hour of that day order required:"))
    time1(n,m,room)
else:
    print("Invalid")     