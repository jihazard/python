'''
 과제0] class Score: 생성해서
           국어, 영어, 전산 점수 받을 수 있는 초기화 함수 만들고
 	   총점 구하는 함수
	   평균 구하는 함수 
	   출력하는 함수 만들어서
	   입력하는 함수 <--- 추가
 	객체 생성해서 결과 출력하는 프로그램 작성

'''

def printDeco(func):
	def decorated():
		print("=============================")
		func()
		print("=============================")
	return decorated


class Score:
# 초기화 함수
	def __init__(self, kor, eng, elec):
		self.kor = kor
		self.eng = eng
		self.elec = elec
# 입력하는 함수
	def setJumsu(self, kor, eng, elec):
		self.kor = kor
		self.eng = eng
		self.elec = elec
	
# 총점 구하는 함수
	def totalSum(self):
		return self.kor + self.eng + self.elec

# 평균 구하는 함수
	def totalAvg(self):
		return self.totalSum()/3
		
# 입력으로 처리하는 함수
	@printDeco
	def paintResult(self,mode):
		self.mode = mode
		if mode == "총합":
			return print(self.totalSum())
		elif mode == "평균":
			return print(self.totalAvg())
		else:
			return print("잘못입력하셨습니다 총점, 평균 중 선택해주세요")


def main():
    print("============================================")
    print("===============과제0 평균구하기===============")
    scorex = Score(10,10,10)
    scorex.paintResult("총합")
    scorex.paintResult("평균")
    scorex.setJumsu(50,50,50)
    scorex.paintResult("총합")
    scorex.paintResult("평균")


if __name__ == "__main__":
    main()


