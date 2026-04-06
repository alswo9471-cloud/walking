import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 읽기
df = pd.read_csv('걷기.csv')
df['날짜/시간'] = pd.to_datetime(df['날짜/시간'])
df['요일'] = df['날짜/시간'].dt.dayofweek
start_date = pd.to_datetime('2025-12-15')
df['주차'] = ((df['날짜/시간'] - start_date).dt.days // 7) + 1

# 표 만들기
pivot_df = df.pivot(index='주차', columns='요일', values='걸음 수 (걸음)')

# 그림 그리기 (깔끔 버전)
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, cmap='YlGn', annot=False, linewidths=3, linecolor='white', square=True)
plt.xticks(ticks=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.yticks([])

# 파일로 저장 (중요: 이 이름으로 깃허브에 파일이 생길 겁니다)
plt.savefig('walking_grass.png')
