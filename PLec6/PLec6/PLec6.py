class Movie:
    ''' 
    영화 클래스입니다 
    '''
    count = 0

    title = "반지의 제왕"
    director = "피터 잭슨"
    def __init__(self, title, director):
        self.title = title
        self.director = director
        Movie.count += 1
        print(self.title + " 생성자 호출")

    def __del__(self):
        print(self.title + " 소멸자 호출")

    def showInfo(self):
        print(self.title + "/" + self.director)

    @staticmethod
    def showCount1():
        print(Movie.count)

    @classmethod
    def showCount2(cls):
        print(cls.count)

m1 = Movie("암살", "최동훈")
m2 = Movie("반지의 제왕", "피터잭슨")
m3 = Movie("베테랑", "류승완")
m4 = Movie("메이즈러너", "웨스 볼")

#print(type(m4))
#m4 = m3     #바로 m4의 객체가 사라진다. 참조 더이상 되지 않으니까
#            #즉 모든 파이썬 변수 타입들은 참조형
#            #대입연산하면 깊은 복사가 아니라 얕은 복사
#print(id(m4))   #id는 주소
#print(id(m3))
#m4.showInfo()

print(m1.count)
print(m2.count)
print()

Movie.showCount1()
Movie.showCount2()