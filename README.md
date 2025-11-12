# 은행 정기예금 마케팅 대상 추천 시스템 (Bank Marketing Recommendation System)


## 프로젝트 개요

이 프로젝트는 '데이터베이스' 수업 기말 프로젝트로, 은행의 텔레마케팅 데이터를 분석하여 정기예금 가입 가능성이 높은 잠재 고객을 선별하는 시스템을 구축하는 것입니다.

단조로운 CSV 데이터를 정규화하여 관계형 데이터베이스(MySQL)를 구축하고, SQL 쿼리를 통한 심층 분석 결과를 바탕으로 마케팅 효율을 극대화할 수 있는 **타겟 고객 추천 애플리케이션(Streamlit)** 을 개발하였습니다.


## 프로젝트 목표 

- **데이터베이스 설계**: 비정형 CSV 데이터를 3차 정규화(3NF)까지 수행하여 효율적인 RDBMS 구축.

- **SQL 데이터 분석**: 정기예금 가입 여부(y)에 영향을 미치는 주요 요인(직업, 연령, 시기 등)을 SQL로 분석.

- **시스템 구현**: 분석된 인사이트를 점수화 알고리즘으로 변환하여, 실무자가 사용할 수 있는 추천 웹 앱 개발.


## 사용 기술 

- Database: MySQL (SQLAlchemy, PyMySQL)

- Language: Python 3.x

- Data Analysis: Pandas, SQL

- Visualization: Matplotlib, Seaborn

- Application: Streamlit


## 데이터셋

- 데이터 출처: UCI Machine Learning Repository - Bank Marketing Data Set

- 데이터 크기: 45,211 rows, 17 columns


## 데이터베이스 정규화 

데이터의 중복을 최소화하고 무결성을 유지하기 위해 다음과 같이 테이블을 분리하였습니다.

- Customer: 고객 고유 정보 (나이, 잔액, 신용 정보 등)

- Campaign: 마케팅 캠페인 이력 (연락 시기, 통화 시간, 결과 등)

- Lookup Tables (Code Tables): Job, Education, MaritalStatus, Contact, Poutcome (반복되는 범주형 데이터 분리)

 
## 주요 분석 결과 

SQL 쿼리 분석을 통해 도출된 마케팅 성공의 핵심 요인은 다음과 같습니다.

- 직업(Job): 학생(28.7%)과 은퇴자(22.8%)의 가입률이 압도적으로 높음.

- 연령(Age): 경제 활동 인구인 30~40대보다 20대 이하와 50대 이상의 가입률이 높음.

- 시기(Month): 3월, 9월, 10월, 12월 등 특정 시즌에 성공률이 급상승함 (최대 52%).

- 이전 결과(Poutcome): 과거 캠페인에서 **'성공(Success)'** 했던 고객의 재가입률은 **64.7%** 에 달함.


## 추천 프로그램 

분석된 데이터를 기반으로 고객의 정보를 입력하면 가입 가능성 점수를 계산하여 추천 등급을 알려주는 Streamlit 앱입니다.

### 점수 산정 로직 (Scoring Logic)

SQL 분석 결과에 따라 가중치를 부여하는 규칙 기반(Rule-based) 알고리즘을 적용했습니다.

- 직업: 학생/은퇴자 (+3점), 관리자/실업자 (+2점) 등

- 이전 성공 여부: 성공 시 (+4점) - 가장 강력한 예측 변수

- 연락 수단: 휴대폰 (+2점)

- 시기: 3, 9, 10, 12월 (+2점)

### 실행 화면 예시

결과: 총점에 따라 적극 추천(Very High), 추천(High), 보통(Normal), 비추천(Low) 4단계로 분류


## 필수 라이브러리

본 프로젝트를 실행하기 위해서는 아래와 같이 필수 라이브러리를 설치해야 합니다.

```pip install pandas sqlalchemy pymysql matplotlib seaborn streamlit```
