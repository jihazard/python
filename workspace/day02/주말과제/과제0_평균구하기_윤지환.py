'''
 과제0] class Score: 생성해서
           국어, 영어, 전산 점수 받을 수 있는 초기화 함수 만들고
 	   총점 구하는 함수
	   평균 구하는 함수 
	   출력하는 함수 만들어서
	   입력하는 함수 <--- 추가
 	객체 생성해서 결과 출력하는 프로그램 작성

'''

class Score:
# 초기화 함수
	def __init__(self, kor, eng, elec):	
		self.kor = kor
		self.eng = eng
		self.elec = elec

# 입력하는 함수
	def setJumsu(self, kor, eng, elec ,mode):
		self.kor = kor
		self.eng = eng
		self.elec = elec
		self.mode = mode
		self.paintResult(mode)

# 총점 구하는 함수
	def totalSum(self):
		return self.kor + self.eng + self.elec

# 평균 구하는 함수
	def totalAvg(self):
		return self.totalSum()/3
		
# 입력으로 처리하는 함수
	def paintResult(self,mode):
		result = {"총합": self.totalSum(), "평균": self.totalAvg()}
		print("{} : {}".format(mode, result.get(mode)))			


def main():
	print("==============================================")
	print("===============과제0 평균구하기===============")
	scorex = Score(10,10,10)
	scorex.paintResult("총합")
	scorex.paintResult("평균")
	# 입력받는 함수
	scorex.setJumsu(50,50,50,"총합")
	
	# 클래스의 함수로 호출
	print(scorex.totalSum())
	print(scorex.totalAvg())
	print("==============================================")


if __name__ == "__main__":
    main()


