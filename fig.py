import matplotlib.pyplot as plt

# 准备数据
categories = ['高频实体', '中频实体', '长尾实体', '未知实体']
model1_scores = [6.50, 7.20, 7.85, 7.95]
model2_scores = [5.80, 6.55, 7.15, 7.45]

# 设置中文字体 (防止方块乱码)
plt.rcParams['font.sans-serif'] = ['SimHei'] 

# 绘制折线
plt.plot(categories, model1_scores, marker='o', label='RAGEC+THUOCL', color='#1f77b4')
plt.plot(categories, model2_scores, marker='s', label='RAGEC+THUOCL+CCKS', color='#ff7f0e')

# 添加标签和图例
plt.ylabel('错误率 / 性能指标')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()