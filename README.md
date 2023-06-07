# 저출산 담론의 구조와 출산율 패턴의 변화

## 프로젝트 기획 배경 및 목표
1. 경제적 요인 : 경제적 지원이 뒷받침되면 혼인율과 출산율이 높아질 것인가?
2. 가치관 변화 : 아니면 가치관 변화에 따라 출산율의 패턴이 변화한 것일까?

> 경제적 요인과 저출산을 둘러싼 여론의 변화를 분석해 원인과 대책을 짚어본다.

### [1] 경제적 측면 - 소득과의 연관성
(1) 분석 방법
>1) 국세청, 통계청에서 관련 자료 수집해 데이터베이스에 저장
>2) SQL로 통계자료를 불러와 Pandas, Numpy, statsmodels 등 파이썬 통계 라이브러리를 이용한 분석
>3) folium, Geo Pandas 등 파이썬 지도 라이브러리를 이용해 코로플레스 맵(지도상 히트맵)을 제작해 구별 지표 비교 시각화

(2) 분석 방향 : 소득과 출산율, 혼인율 간의 상관관계를 알아보기 위해 서울시 내 자치구 비교

### [2] 가치관 변화 - 가치관 변화에 따라 출산율의 패턴이 변화한 것일까?
(1) 분석 방법
>1) 통계청 사회조사 자료를 바탕으로 혼인과 출산에 대한 가치관 파악
>2) Youtube API를 이용한 영상 댓글 crawling
>3) 댓글 내용을 분석하기 위한 형태소 분석
>4) 단어의 의미를 감성 분석과 의미 연결망을 이용하여 분석

(2) 분석 방향
>1) '저출산' 키워드로 조회한 영상 댓글 분석
>2) '저출산' 연관 키워드로 조회한 영상 댓글 분석

(3) 분석 결과물
>1) 워드 클라우드
>2) flourish 시각화 자료
>3) 감성 분석 그래프
>4) 의미 연결망

### 인사이트 도출
(1) 경제적 여유가 없어서 출산하지 않는다?
- 근로소득 2.4배 차이의 상하위 3개 구들의 출산율, 혼인율에서 유의미한 차이가 없다는 것은 경제적 이유가 저출산의 주된 원인이라는 통념과 상반된다.

(2) 성 역할 인식 변화와 개인적 관점의 부상
- 전통적 성 역할에 대한 인식 변화
- 저출산을 바라보는 관점의 '국가적 관점'에서 '개인적 관점'으로의 변화

### 기대효과
(1) 저출산 이슈를 경제거 요인에 의한 문제로만 단정짓지 않고 가치관 변화와 젠더 문제등 인식의 관점에서 접근하도록 촉구하는 효과

(2) 따라서 경제적 뒷받침만으로는 저출산 문제가 해결될 수 없으며, 이러한 방향의 현재 정책적 접근을 재검토할 필요성 제기
