import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 불러오기
df = pd.read_csv('걷기.csv')
df['날짜/시간'] = pd.to_datetime(df['날짜/시간'])

# 2. 요일 및 주차 계산
df['요일'] = df['날짜/시간'].dt.dayofweek
start_date = pd.to_datetime('2025-12-15')
df['주차'] = ((df['날짜/시간'] - start_date).dt.days // 7) + 1

# 3. 피벗 테이블 생성
pivot_df = df.pivot(index='주차', columns='요일', values='걸음 수 (걸음)')
pivot_df.columns = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 4. 시각화 (잔디 스타일)
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_df, cmap='YlGn', annot=True, fmt='.0f', linewidths=2, square=True)
plt.title('My Walking Grass')

# 5. 이미지 저장
plt.savefig('walking_grass.png')
