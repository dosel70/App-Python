#
# #
#
# #
#
# class School:
#     def __init__(self,name,place,student_count,teacher_count):
#         self.name = name
#         self.place = place
#         self.student_count = student_count
#         self.teacher_count = teacher_count
#
#     def print_school_info(self):
#         print(f'학교이름: {self.name}, 지역: {self.place}, 학생 수: {self.student_count}, 선생님 수: {self.teacher_count}\n')
#
# # # 학생
# # # 이름, 학년
# ## # 학교
# # #이름 , 지역 , 학생 수, 선생님 수
# class Student:
#     def __init__(self, student_name, student_grade,ability):
#         self.student_name = student_name
#         self.student_grade = student_grade
#         self.ability = ability
#
#     def print_info(self):
#         print(f'학생 명 : {self.student_name},학생 학년 : {self.student_grade},능력치 : {self.ability}')
#
# # # 선생님
# # # 이름, 과목, 학교
# # # 선생님이 추가될 때마다 선생님 수 1 증가
# # # 준비된 학생들에게 해당과목을 가르치면 학생들의 능력치 1증가
# # # 선생님 정보 출력 메소드
# class Teacher:
#     def __init__(self,teacher_name,subject,teaching_score):
#         self.teacher_name = teacher_name
#         self.subject = subject
#         self.school = school
#         self.teaching_count = 0
#         self.teaching_score = teaching_score
#
#     def teacher_info(self):
#         print(f"이름 : {self.teacher_name}, 과목 : {self.subject}, 학교 : {self.school} ")
#
#
#     def teach_student(self, students):
#         if self.teaching_score> 0:
#             for student in students:
#                 student.student_grade += 1
#             print(f"{self.teacher_name} 선생님이 {self.subject}을 가르쳐 학생들의 능력치가 {student.ability}증가했습니다.")
#         else:
#             print(f"{self.teacher_name}선생님은 아직 가르친적이 없어 학생들의 능력치가 오르지 않았습니다.")
#
#
#
#
# # 학교 생성
# school = School("ABC 초등학교", "서울", 300, 2)
#
# # 선생님 정보
# teacher = Teacher("김선생, 이선생","수학,과학",1)
#
# # 학생 생성
# student1 = Student("학생1", 3,1)
# student2 = Student("학생2", 5,1)
# students = [student1, student2]
#
# # 선생님 생성
# teacher1 = Teacher("김선생", "수학", 1)
# teacher2 = Teacher("이선생", "과학", 1)
# # 학생 정보 출력
# student1.print_info()
# student2.print_info()
# # 학교 정보 출력
# school.print_school_info()
#
# # 선생님 정보 출력
# teacher1.teacher_info()
# teacher2.teacher_info()
# teacher1.teach_student(students)
# teacher2.teach_student(students)
#---------------------------------------------------------------------------------------------------------------------
# 학교
# 이름, 지역, 학생 수, 선생님 수
# 학교 정보 출력 메소드
class School:
    def __init__(self, name, location, student_count=0, teacher_count=0):
        self.name = name
        self.location = location
        self.student_count = student_count
        self.teacher_count = teacher_count

    def print_info(self):
        print(self.name, self.location, self.student_count, self.teacher_count)


# 선생님
# 이름, 과목, 학교
# 선생님이 추가될 때마다 선생님 수 1증가
# 준비된 학생들에게 해당 과목을 가르치면 학생들의 능력치 1증가
# 선생님 정보 출력 메소드
class Teacher:
    def __init__(self, name, subject, school):
        self.name = name
        self.subject = subject
        self.school = school
        self.school.teacher_count += 1

    def print_info(self):
        print(self.name, self.subject)
        self.school.print_info()

    def teach(self, students):
        for student in students:
            student.ability += 1


# 학생
# 이름, 학년(grade), 학교, 능력치(초기값: 0), 담임 선생님
# 학생이 추가될 때마다, 학생 수 1증가
# 학생 정보 출력 메소드
class Student:
    def __init__(self, name, grade, school, teacher, ability=0):
        self.name = name
        self.grade = grade
        self.school = school
        self.teacher = teacher
        self.ability = ability
        self.school.student_count += 1

    def print_info(self):
        print(self.name, self.grade, self.ability)
        self.school.print_info()
        self.teacher.print_info()


school = School('영동고등학교', '서울')
teacher = Teacher('한동석', '컴퓨터', school)
students = [
    Student('홍길동', 1, school, teacher),
    Student('이순신', 1, school, teacher),
    Student('장보고', 2, school, teacher)
]

teacher.teach(students)
for student in students:
    student.print_info()








