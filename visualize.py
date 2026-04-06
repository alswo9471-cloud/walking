import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import timedelta

# 1. 데이터 불러오기
df = pd.read_csv('걷기.csv')
df['날짜/시간'] = pd.to_datetime(df['날짜/시간'])

# 2. 주차별 라벨 생성 (Week 1 (12.15~12.21) 형식)
start_date = pd.to_datetime('2025-12-15')
df['주차_num'] = ((df['날짜/시간'] - start_date).dt.days // 7) + 1
df['요일'] = df['날짜/시간'].dt.dayofweek

# 주차별 시작일과 종료일을 계산하여 라벨 만들기
week_labels = {}
for w in range(1, df['주차_num'].max() + 1):
    w_start = start_date + timedelta(days=(w-1)*7)
    w_end = w_start + timedelta(days=6)
    week_labels[w] = f"Week {w:02d} ({w_start.strftime('%m.%d')}~{w_end.strftime('%m.%d')})"

df['주차'] = df['주차_num'].map(week_labels)

# 3. 피벗 테이블 생성 (순서 유지를 위해 주차 라벨 정렬)
sorted_weeks = [week_labels[i] for i in range(1, df['주차_num'].max() + 1)]
pivot_df = df.pivot(index='주차', columns='요일', values='걸음 수 (걸음)')
pivot_df = pivot_df.reindex(sorted_weeks)
pivot_df.columns = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 4. 시각화 설정
plt.figure(figsize=(16, 10)) # 전체적인 크기를 키움

# 히트맵 그리기
ax = sns.heatmap(pivot_df, 
                 cmap='YlGn', 
                 annot=False, 
                 linewidths=5,    # 칸 사이 간격을 넓혀서 더 시원하게
                 linecolor='white', 
                 square=True, 
                 cbar_kws={'shrink': .5})

# 5. 요청사항 반영: 요일을 위로 이동
ax.xaxis.tick_top() # X축(요일)을 위로
ax.xaxis.set_label_position('top') 

# 글씨 크기 및 스타일 조정
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=12)
plt.title('My Walking Grass Map', fontsize=20, pad=30)
plt.ylabel('')
plt.xlabel('')

# 6. 이미지 저장
plt.tight_layout()
plt.savefig('walking_grass.png', dpi=100) # 해상도를 높여서 저장
