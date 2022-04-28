# fpsPrediction
FPS 예측 머신러닝 기능

## 요구사항 분석
1번 데이터 
-CPU : PassMark CPU Mark / Clockspeed / Cores / Threads
-GPU: PassMark GPU Mark / Max Memory Size / Core Clock
2번데이터
-게임별 저사양, 중사양, 고사양 PC의 최소 최대 FPS 데이터 (크롤링 혹은 API)

2번 데이터 PC의 정보들을 학습시켜 1번 데이터를 테스트 하여 FPS 예측 기능 개발한다

Pytorch을 활용한 예측 머신러닝 기법 사용
-Pytorch 선택 사유 : 파이썬과 유사함에 따라 진입 장벽이 낮다

## 진행사항
-데이터 입력 받을시 회귀분석을 통한 FPS 예측값 출력
-테스트 데이터는 CSV에 추가되며 학습 데이터로 활용된다
-현재 모델 개선을 위한 라쏘(Lasso) 모델 분석중
