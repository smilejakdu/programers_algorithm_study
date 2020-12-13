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
from collections import defaultdict
from operator import itemgetter


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
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
#
# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
#
# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

def solution(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play
    # 플레이 횟수의 합이 가장 큰 장르 순서대로 집어넣은 리스트 생성
    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
    final_dict = defaultdict(lambda: [])
    # 장르명을 key로 갖고 값으로는 각 노래의 플레이 횟수와 고유번호 리스트로 저장하는 딕셔너리 생성
    # {"classic": [(500,0), ...]}
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
    answer = []
    # 랭킹을 통해 플레이어 횟수가 가장 많은 장르부터 해당 잘르에서 가장 많이 플레이된 2개의 곡을 answer에 차례로 넣어 줌.
    # 곡이 2개 미만이면 1개만 넣어주기.
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])
    return answer