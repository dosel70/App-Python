# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의
class Taxi:
    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    def calculate_fare(self):
        BASIC_FEE = 4000
        BASIC_DISTANCE = 2
        ADDITIONAL_FEE_PER_KM = 1000

        total_distance = max(0, self.distance - BASIC_DISTANCE)
        fare = BASIC_FEE + (total_distance * ADDITIONAL_FEE_PER_KM)
        return fare

    def calculate_change(self, paid_amount):
        fare = self.calculate_fare()
        if self.distance < 0:
            raise ValueError("잘못된 입력")

        if paid_amount >= fare:
            change = paid_amount - fare
            return change
        else:
            return "잔액이 부족합니다."


# 예시 사용
passenger_money = 30000
passenger_distance = 13
taxi = Taxi(passenger_money, passenger_distance)

fare_result = taxi.calculate_fare()
change_result = taxi.calculate_change(passenger_money)

print(f"택시 요금: {fare_result}원")
print(f"잔돈: {change_result}원")
#------------------------------------------------------------------------------------------------------------------------
#         self.distance = distance
#
#     def calculate_fare(self):
#         cost = Taxi.default_fare
#         if self.distance > Taxi.default_distance:
#             cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km
#
#         return cost
#
#     def get_change(self):
#         return self.money - self.calculate_fare()
#
#
# taxi = Taxi(20000, 1)
# print(taxi.calculate_fare(), taxi.get_change())
#
# taxi = Taxi(30000, 10)
# print(taxi.calculate_fare(), taxi.get_change())


# 2.
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self):
        self.income = 0

    def calculate_fare(self, money, distance):
        cost = Taxi.default_fare
        if distance > Taxi.default_distance:
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        self.income += cost

        def get_change():
            return money - cost

        return cost, get_change()


taxi = Taxi()
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))
print(taxi.income)
