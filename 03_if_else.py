# WAP to  find student is pass or failed , marks in each subject should be more than 30 
# and total should be more than 40


sub1 = int(input("Enter marks of subject 1  "))
sub2 = int(input("Enter marks of subject 2  "))
sub3 = int(input("Enter marks of subject 3  "))

if(sub1<30 or sub2<30 or sub3<30 ):
    print("You are failed beacuse of less than passing marks")

elif((sub1+sub2+sub3)/3 < 40):
    print("You are failed beacuse of less marks as total")


else:
    print("You are passed")
    