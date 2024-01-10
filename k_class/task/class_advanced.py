# Class 고급
# 회원
# 번호 , 아이디, 비밀번호, 이름
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 기준으로 자동으로 붙여준다.
# 다른 언어에서 파이썬에 있는 것에 접근 하기 위해서는 메소드 밖에 안됨
class User :
    # private : 자신의 클ㄹ래스 에서만 접근가능
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자.
    #__user_number = 0  >> private : 자신의 클래스에서만 접근 가능(앞에다 __ 붙히면 private , 안 붙히면 public)
    # private (__)쓰는 이유 1. 메소드로 접근해라, 2. 밖에서 못쓰게 하려고 사용한다.
    user_number = 0
    def __init__(self,id,pw,name) : # 일반 회원
        self.id = id
        self.password = pw
        self.name = name
        self.user_number += 1


    @classmethod
    def admin(cls,id,pw,name): # 생성자를 쓰지 않고 어드민 메소드로 객체화!!! (래핑)
        if id.startswith("admin_"):
            print("어드민 계정 사용중")
        else :
            new_id = f"admin_{id}"
            return cls(new_id,pw,name)
while True :
    user_id = input("id 입력 : ")
    # 일반 회원가입
    choice = int(input("관리자로 로그인 하시겠습니까 ? 0(네)/1(아니요) : "))
    if choice == 0:
        # 관리자 회원가입
        admin_member= User.admin(user_id,"admin_pw", "Admin")
        print(f"아이디(admin) : {admin_member.id} " )
    elif choice == 1 :
        if user_id.startswith("admin_"):
            print("관리자 페이지로 이동하세요")

        else :
            member1 = User(user_id, "user_pw1", "User 1")
            print(f"아이디(user) : {member1.id}")

    else :
        break

#-----------------------------------------------------------------------------------------------------------------------
# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
# class User:
#     # private: 자신의 클래스에서만 접근 가능
#     # 1. 외부에서 접근하지 말자!
#     # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
#     __user_number = 0
#
#     def __init__(self, user_id, user_password, user_name):
#         User.__user_number += 1
#         self.user_number = User.__user_number
#         self.user_id = user_id
#         self.user_password = user_password
#         self.user_name = user_name
#
#     @staticmethod
#     def get_number():
#         return User.__user_number
#
#     @classmethod
#     def set_admin(cls, **kwargs):
#         kwargs['user_id'] = 'admin_' + kwargs['user_id']
#         return cls(**kwargs)
#
#
# user = User('hds', '1234', '한동석')
# print(user.user_id)
#
# admin = User.set_admin(user_id='hds', user_password='1234', user_name='한동석')
# print(admin.user_id)
#
#
# print(User.get_number())









