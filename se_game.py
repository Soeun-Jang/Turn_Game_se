import random
import sys
import time

# 요구사항 : 이름 입력 -> 플레이어 생성
# 몬스터 -> 임의 생성
# while문에서 플레이어와 몬스터 전투 반복
# 플레이어 공격 타입 선택 -> 기본공격, 화살공격, 마법공격
# 몬스터 -> 일반 공격
# 매 전투시 플레이어& 몬스터 상태 출력
# 모든 공격 파워기준 랜덤성 ex) 파워: 10, 일반공격 8~12
# 몬스터 또는 플레이어 HP 0이 되면 전투 종료 후 승리나 패배 출력
# 추가기능
# 1) 플레이어 승리 시 레벨업 후 스킬 추가 획득
# 2) 전직 시 스킬 이름 변경 및 데미지 계수 조정
# 3) 보스 전투 요구 사항 : 플레이어 전직


# =========공통으로 사용될 부모 클래스 =========
class Unit:
    def __init__(self, name, hp, power, max_hp):
        self.name = name
        self.hp = hp
        self.power = power
        self.max_hp = max_hp

    def print(self):
        print(
            f"**몬스터가 생성되었습니다! 닉네임: {self.name}, 체력:{self.hp}, 파워:{self.power}**")

    def attack_damage(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        # 데미지 값 설정 - 파워기준 랜덤성 (-2, +2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태 : HP {self.hp}/{self.max_hp}")


# ========= 상속 받은 플레이어 클래스 =========
class Character(Unit):
    def __init__(self, name, hp, power, attack_type, max_hp):
        Unit.__init__(self, name, hp, power, max_hp)
        self.attack_type = attack_type

    def print(self):
        print(
            f"\n**플레이어가 생성되었습니다! 닉네임: {self.name}, 체력:{self.hp}, 파워:{self.power}, 공격타입:{attack_type_dict[self.attack_type]}**")

# --------- 레벨업 시 획득하는 공격타입 출력문 --------
    def Level_UP(self, New_Skill):
        print(f"공격타입을 새로 획득습니다! 공격타입:{attack_type_dict[New_Skill]}")

    def New_Skill_damage(self, other, New_Skill):
        damage = random.randint(self.power - 1, self.power + 7)
        other.hp = max(other.hp - damage, 0)
        print(
            f"{self.name}의 {attack_type_dict[New_Skill]}! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def Upgrade_Skill_damage(self, other, New_Skill):
        damage = random.randint(self.power - 0, self.power + 30)
        other.hp = max(other.hp - damage, 0)
        print(
            f"{self.name}의 {upgrade_skill_dict[New_Skill]}! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


# ===========게임 컨셉==========
print("""
평범한 일반인이었던 당신은 여느 때와 같이 내일의 일상을 위해 일찍 잠에 들었습니다.. .
(Enter를 누르시면 다음 문장이 실행됩니다.)
""")
input()
print("그런데 주말에 봤던 몬스터를 멋있게 무찌르는 게임과 그 주인공이 생각난 당신은 잠꼬대 아닌 잠꼬대를 나지막히 읊고는 잠이 들었습니다.")
input()
print(" \'...ㄴ..나도 플레이어가 되고싶다.\' ")
input()
print("누가 소원을 들어준걸까요? 당신은 플레이어가 되었습니다.")
input()

print("\n\nGame Start.\n")
# ==========게임 컨셉===========


# 플레이어 이름 설정
while True:
    name = input("\n플레이어 닉네임으로 사용할 이름을 입력해주세요: ")
    if name.strip():
        break
    else:
        continue


# 공격타입 선택
print("\n몬스터와 싸울 공격 타입을 선택하세요. ")
while True:
    attack_type = input("""1.기본공격 2. 화살공격 3. 마법공격 4. 불속성 공격 5.얼음 속성 공격
""")
    if attack_type != "1" and attack_type != "2" and attack_type != "3" and attack_type != "4" and attack_type != "5":
        print("잘못된 입력입니다. 1~5 사이 숫자를 입력하세요.")
    else:
        break


# attack_type 딕셔너리
attack_type_dict = {
    "1": "기본공격",
    "2": "화살공격",
    "3": "마법공격",
    "4": "불속성 공격",
    "5": "얼음 속성 공격",
}

# 플레이어 객체 생성
Player = Character(name, 200, 10, attack_type, 200)
Player.print()
# max_hp 변수 설정해서 Monster내의 hp와 max_hp 랜덤 값 동일하게 설정
monster_max_hp = random.randint(160, 220)
# 몬스터 객체 생성
Monster = Unit("몬스터", monster_max_hp, random.randint(5, 15), monster_max_hp)
Monster.print()


print("\n전투를 시작하시겠습니까? (y/n)")
while True:
    Fight = input()
    if Fight == "y":
        break
    elif Fight == "n":
        print(f"{Player.name}, 마음의 준비가 필요하신가요 .. ? ")
    if Fight != "y" and Fight != "n":
        print("잘못된 입력입니다. y 또는 n을 입력해주세요.")


# ========= 전투 반복문 ===========
while Player.hp > 0 and Monster.hp > 0:
    if Fight == "y":
        Player.attack_damage(Monster)
        Player.show_status()
        if Monster.hp <= 0:
            print(f"\n전투 종료. {Player.name}이(가) 승리하였습니다.")
            break
        Monster.attack_damage(Player)
        Monster.show_status()
        if Player.hp <= 0:
            print(f"\n전투 종료. {Monster.name}이(가) 승리하였습니다.")
            print("꿈에서 깨어났습니다. 꿈을 열심히 꾼 당신은 지각에 당첨되었습니다.")
            sys.exit()
        time.sleep(0.3)


# ======= Player 승리 시 Level up =======
if Player.hp > 0:
    Player = Character(name, 300, 20, attack_type, 300)
    print("\n***경험치 증가! Level Up!***")
    Player.show_status()

# 새 스킬 번호 New_Skill에 담아주기
print("""
레벨제한이 풀려서 스킬을 하나 더 획득할 수 있습니다. 새로운 스킬을 선택해주세요. (1~5)
1.기본공격 2. 화살공격 3. 마법공격 4. 불속성 공격 5.얼음 속성 공격
""")

while True:
    New_Skill = input("입력 : ")
    if attack_type != "1" and attack_type != "2" and attack_type != "3" and attack_type != "4" and attack_type != "5":
        print("획득 할 스킬 번호를 입력하세요.")
    elif New_Skill == Player.attack_type:
        print("중복된 값입니다. 다른 번호를 입력해주세요.")
    else:
        break


Player.Level_UP(New_Skill)
print("\n전투를 시작하시겠습니까? (y/n)")
# 싸울 객체 새로 지정(randint값 새로 설정)
Monster = Unit("몬스터", monster_max_hp, random.randint(15, 20), monster_max_hp)
Monster.print()

while True:
    Fight = input()
    if Fight == "y":
        break
    elif Fight == "n":
        print(f"{Player.name}, 마음의 준비가 필요하신가요 .. ? ")
    if Fight != "y" and Fight != "n":
        print("잘못된 입력입니다. y 또는 n을 입력해주세요.")

# ========= 전투 반복문(New_Skill 추가)==========
while Player.hp > 0 and Monster.hp > 0:
    if Fight == "y":
        Player.New_Skill_damage(Monster, New_Skill)
        Player.show_status()
        if Monster.hp <= 0:
            print(f"\n전투 종료. {Player.name}이(가) 승리하였습니다.")
            break
        Monster.attack_damage(Player)
        Monster.show_status()
        if Player.hp <= 0:
            print(f"\n전투 종료. {Monster.name}이(가) 승리하였습니다.")
            print("꿈에서 깨어났습니다. 꿈을 열심히 꾼 당신은 지각에 당첨되었습니다.")
            sys.exit()
        time.sleep(0.3)

if Player.hp > 0:
    print("\n***경험치 증가! Level Up!***")
    Player = Character(name, 850, 125, attack_type, 850)

print("\n======= 전직이 가능합니다! =========")
print("====== 전직... 하시겠습니까 ? ======")

while True:
    Upgrade = input("1.예 / 2.아니오 : ")
    if Upgrade != "1" and Upgrade != "2":
        print("잘못된 입력입니다. 1 또는 2를 입력하세요.")
    elif Upgrade == "2":
        print("전직을 하지 않으면 보스 전투 실행이 불가합니다.")
    else:
        break


# attack_type 딕셔너리 밸류 값 변경
attack_type_dict = {
    "1": "캡틴코리아",
    "2": "호크아이",
    "3": "해리포터",
    "4": "파이리",
    "5": "엘사",
}

print("\n\n최근에 획득한 공격타입과 같은 속성의 직업으로 전직합니다.")
print(f"{Player.name}은 [{attack_type_dict[New_Skill]}]로 전직했습니다! 축하합니다!")


# ===== Boss 몹 =======
print("""
...    
어디선가 알 수 없는 목소리가 들려오기 시작했다.
""")


print(
    f"\"{attack_type_dict[New_Skill]} {Player.name}. 당신은 이제 준비가 된 것 같군요. 최종 Boss를 잡으러 가시겠습니까? (y/n)\"")

Fight = input()
while True:
    if Fight == "y":
        break
    elif Fight == "n":
        print(f"{Player.name}, 마음의 준비가 필요하신가요 .. ? ")
        Fight = input()
    if Fight != "y" and Fight != "n":
        print("잘못된 입력입니다. y 또는 n을 입력해주세요.")
        Fight = input()

# 단순 공격주문 생성하기 위해 만든 딕셔너리임
upgrade_skill_dict = {
    "1": "고무고무피스톨!",
    "2": "arrow rain공격!",
    "3": "익스펙토패트로눔!",
    "4": "화염토치 공격!",
    "5": "고드름 공격!"
}

# 보스 생성 및 설정
monster_max_hp = random.randint(1500, 2000)
Monster = Unit("보스", monster_max_hp, random.randint(60, 70), monster_max_hp)
Monster.print()

# ========= 전투 반복문 ===========
while Player.hp > 0 and Monster.hp > 0:
    if Fight == "y":
        Player.Upgrade_Skill_damage(Monster, New_Skill)
        Player.show_status()
        if Monster.hp <= 0:
            print(f"\n전투 종료. {Player.name}이(가) 승리하였습니다.")
            break
        Monster.attack_damage(Player)
        Monster.show_status()
        if Player.hp <= 0:
            print(f"\n전투 종료. {Monster.name}이(가) 승리하였습니다.")
            print("꿈에서 깨어났습니다. 꿈을 열심히 꾼 당신은 지각에 당첨되었습니다.")
            sys.exit()
        time.sleep(0.3)


print("\n\n축하드립니다. 스테이지를 모두 클리어 하셨습니다 :) ")
print("\n\nmade by 장소은")
