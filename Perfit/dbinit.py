from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.perf_it

db.qna.drop()

doc =[
    {'idx': 1, 'quiz': "가장 좋아하는 계절은?", 'ans_01': "봄", 'ans_02': "여름", 'ans_03': "가을", 'ans_04': "겨울"},
    {'idx': 2, 'quiz': "사랑을 한다면 어떤 사랑을 하고 싶은가", 'ans_01': "강렬하고 화려한 사랑", 'ans_02': "아름답고 신비로운 사랑", 'ans_03': "차갑고 도도하지만 섬세한 사랑", 'ans_04': "고귀하고 성스러운 사랑"},
    {'idx': 3, 'quiz': "간만에 휴가, 당신은 무엇을 할 것인가", 'ans_01': "반려동물과 포근한 낮잠을 잔다.", 'ans_02': "친구들과 함께 보낸다.", 'ans_03': "연인과 함께 시간을 보낸다.", 'ans_04': "혼자만의 시간을 즐긴다."},
    {'idx': 4, 'quiz': "집 한채를 장만하게 되면, 내가 살게 될 집은?", 'ans_01': "편안한 우디향으로 가득한 숲속의 집", 'ans_02': "시원한 바다가 한 눈에 보이는 별장", 'ans_03': "꽃이 가득한 정원이 있는 주택", 'ans_04': "사랑스러운 연인과 함께하는 도심 속 풀빌라"},
    {'idx': 5, 'quiz': "나를 가장 잘 표현하는 색은?", 'ans_01': "깨끗한 순백의 화이트", 'ans_02': "시크한 블랙", 'ans_03': "시원하고 청량한 블루", 'ans_04': "우아하고 화사한 핑크"},
]


db.qna.insert_many(doc);