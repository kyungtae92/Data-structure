#학생클래스 생성
#멤버변수[속성] private형 - name, id
#getter[멤버변수값을 외부로 내보낼때 사용]: name, id,
#   def get_name(parameter):
#setter[멤버변수값을 외부에서 가져올때 사용]: name
#   def set_name(parameter):

class Student:

    def __init__(self, name, id):   #생성자 - 초기변수와 객체 생성시 초기값 설정할 때 사용
    #def __init__(self, name, id=10):
        self._name = name
        self.id = id
    def get_name(self):     #멤버변수값을 외부로 내보낼때 사용
        return self._name
    def get_id(self):
        return self.id
    def set_name(self,name):    #멤버변수값을 외부에서 가져올때 사용
        self._name = name
    def __str__(self):      #객체명을 출력에 이용할 경우의 사용할 명령 설정
        return self._name + ", " + str(self.id)

s1 = Student('kim', 100)    #객체변수 = 클래스명(생성자에 필요한 매개변수)
s1.id = 200
print(s1.get_name())         #print(s1._name) 이 방법은 지양
s1.set_name('hong')
print(s1)
# s2=Student('park')
# print(s2)
