# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 입출력 예제
# phone_book	return
# [119, 97674223, 1195524421]	false
# [123,456,789]	true
# [12,123,1235,567,88]	false
# 입출력 예 설명
# 입출력 예 #1
# 앞에서 설명한 예와 같습니다.
#
# 입출력 예 #2
# 한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.
#
# 입출력 예 #3
# 첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.
# 테스트 케이스 8, 9 실패 --> 왜 틀렸을까?

# 이런저런 생각보다 해시 테이블의 순기능에 초점을 맞춰서 구현해 봤다.
# 해시테이블이란 key-value를 매핑해서 결과값을 제공해주는 자료구조이다.
# 이러한 해시테이블의 특성을 이용하기 위해서는 원하는 key 값을 넣었을때 존재 하느냐 마느냐를 이용하는게 좋다고 생각 했고!
# 자기 자신을 제외한 나머지 번호들의 숫자 갯수를 동일하게 맞춘뒤 해시 테이블에 담아두고 있는지 없는지 검사하게 작성해봄.
# 처음에 순서대로 배열의 수를 줄였는데 이게 패착, 앞 배열에 접두사가포함된 번호가 있고 접두사가 그 뒷 배열에서 나온다면?
# 여기에 대응하지 못해서 이를 대응하기 위해 고민하다가. 모든 배열을 해쉬에 구성하는데
# 근데 단순 배열보다 속도가 느림 ㅋㅋㅋㅋ 해시 함수를 더 좋게 사용할 수 있는 방법이 있을까? 모르겠다.

def phone_book_solution(phone_book):
    for book_index in range(0, len(phone_book)):
        phone_number = phone_book[book_index]
        phone_number_len = len(phone_number)
        dict_phone_book = {
            target_phone_number[:phone_number_len]: target_phone_number if len(target_phone_number) >= phone_number_len else None for target_phone_number in phone_book if target_phone_number != phone_number
        }
        if dict_phone_book.get(phone_number, None):
            return False
    return True


print(phone_book_solution(["119", "97674223", "1195524421"]))
print(phone_book_solution(["123", "456", "789"]))
print(phone_book_solution(["12", "123", "1235", "567", "88"]))
print(phone_book_solution(["010111", "010", "1235", "567", "88"]))
