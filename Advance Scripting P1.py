Case: We have an admission counsellor who wants to deliver a bulk message.

names = list(input().split(","))
ID = list(input().split(","))
CAP_Rank = list(input().split(","))
print("\n")
message = "Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship. \n\n" # write a for loop that iterates through each set of names, Admission_ID, and CAP ranks to print each student's message.
for i in range(len(names)):
    a = names[i]
    b = ID[i]
    c = CAP_Rank[i]
    print(message.format(a,a,b,c))