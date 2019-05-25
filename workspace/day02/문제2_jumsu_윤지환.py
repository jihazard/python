result = ""
with open("jumsu.txt","r") as f :
    lead = f.readlines()
    sum = 0
    for n in lead:
        sum += int(n)

    subjectNumber = len(lead)    
    result = "총합 : {} \n과목 : {}\n평균 : {}".format(sum, subjectNumber, sum/subjectNumber)
    print(result)

with open("avg_result_yoonjihwan.txt","w") as w :
    w.write(result)
    
