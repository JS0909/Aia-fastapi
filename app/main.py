import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CaculatorService
from app.services.user import User, UserService

def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') # 입력받은 id, pw 콘솔에 출력하기
    menu = input('메뉴 선택>>>')
    return menu

def main():
    # 식 expression / for문 등등: statement / 변수    
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
            user.user(id,pw)

    
if __name__ == '__main__':
    main()