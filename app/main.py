import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CaculatorService
from app.services.user import UserService
from app.services.score import ScoreService
from app.services.grade import GradeService

def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') # 입력받은 id, pw 콘솔에 출력하기
    print('3. 성적표 프로그램')
    menu = input('메뉴 선택>>>')
    return menu

def main():
    # 식 expression / for문 등등: statement / 수 : value
    while 1:
        menu = print_menu()
        if menu == '0':
            print('전체프로그램을 종료합니다')
            break
        
        elif menu == '1':
            calcservice = CaculatorService()
            first = int(input('첫번째 값>>>'))
            second = int(input('두번째 값>>>'))
            calcservice.calculate(first, second)
            
        elif menu == '2':
            user = UserService()
            id = input('ID 입력>>>')
            pw = input('PW 입력>>>')
            user.login(id,pw)
            
        elif menu == '3':
            # score = ScoreService()
            name = input('이름: ')
            korean = float(input('국어점수: '))
            english = float(input('영어점수: '))
            math = float(input('수학점수: '))
            # score.average(korean,english,math)
            
            grade = GradeService(name,korean,english,math)
            grade = grade.get_grade()
            print(f'이름: {name} \t성적: {grade}')
            
if __name__ == '__main__':
    main()