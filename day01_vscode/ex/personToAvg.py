



def main():
    print("=========================")
    print("==========cal avg========")

    kor_score = [50,50,50,50,50]
    eng_score = [60,60,60,60,60]
    math_score = [70,70,70,70,70]

    mid_score = [kor_score,eng_score,math_score]

    student_score = [0,0,0,0,0]
    index = 0
    for i in mid_score:
        print("i : " ,i)
        for j in i :
            print("j : ",j)
            student_score[index] += j
            index += 1
        index=0
    print("==========end game=======" , student_score)


if __name__ == "__main__":
    main()