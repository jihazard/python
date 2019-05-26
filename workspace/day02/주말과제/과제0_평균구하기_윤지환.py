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
	def paintResult(self,mode):
		# 삼항연사자로 처리
		# result = self.totalSum() if mode=="총합" else self.totalAvg()
		#딕셔너리 타입으로 처리
		map = {"총합": self.totalSum(), "평균": self.totalAvg()}
		print("{} : {}".format(mode, map.get(mode)))			


def main():
	print("==============================================")
	print("===============과제0 평균구하기===============")
	scorex = Score("111",10,10)
	scorex.paintResult("총합")
	scorex.paintResult("평균")
	print(scorex.totalSum())
	print(scorex.totalAvg())
	print("==============================================")


if __name__ == "__main__":
    main()


