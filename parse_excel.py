import pandas as pd
import json

# 读取食物营养率表
food_df = pd.read_excel('体重管理.xlsx', sheet_name='19日常食物营养率')

# 提取食物数据
foods_data = {
    '碳水': [],
    '蛋白质': []
}

current_category = None
current_subcategory = None

for idx, row in food_df.iterrows():
    col1 = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ""
    col2 = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else ""
    col3 = str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else ""
    col4 = str(row.iloc[4]).strip() if pd.notna(row.iloc[4]) else ""
    
    # 检测大类
    if col1 in ['碳水', '蛋白质', '脂肪']:
        current_category = col1
        current_subcategory = None
        continue
    
    # 跳过标题行和空行
    if col1 == '大类' or col2 == '食物' or (not col1 and not col2):
        continue
    
    # 如果col1有值，col2有值，col3是数字，则col1是子类别，col2是食物名
    if col1 and col2 and col3:
        try:
            rate = float(col3)
            if 0 < rate <= 1:  # 合理的营养率范围
                # 如果col1看起来像子类别名（不是数字序号）
                if not col1.replace('.', '').replace('-', '').isdigit():
                    current_subcategory = col1
                    food_item = {
                        'subcategory': current_subcategory,
                        'name': col2,
                        'rate': rate,
                        'gi': col4 if col4 and col4 not in ['NaN', 'nan', ''] else None
                    }
                    if current_category in ['碳水', '蛋白质'] and current_category in foods_data:
                        foods_data[current_category].append(food_item)
        except (ValueError, TypeError):
            pass

# 特殊处理：有些食物行col1为空，col2是食物名
current_category = None
current_subcategory = None

for idx, row in food_df.iterrows():
    col0 = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
    col1 = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ""
    col2 = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else ""
    col3 = str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else ""
    col4 = str(row.iloc[4]).strip() if pd.notna(row.iloc[4]) else ""
    
    # 检测大类
    if col1 in ['碳水', '蛋白质', '脂肪']:
        current_category = col1
        current_subcategory = None
        continue
    
    # 如果col1是子类别，col2是食物名，col3是数字
    if col1 and col2 and col3 and col1 != '大类' and col2 != '食物':
        try:
            rate = float(col3)
            if 0 < rate <= 1:
                if current_category in ['碳水', '蛋白质']:
                    # 检查是否已存在
                    exists = any(f['name'] == col2 and f['rate'] == rate for f in foods_data.get(current_category, []))
                    if not exists:
                        food_item = {
                            'subcategory': col1,
                            'name': col2,
                            'rate': rate,
                            'gi': col4 if col4 and col4 not in ['NaN', 'nan', ''] else None
                        }
                        if current_category in foods_data:
                            foods_data[current_category].append(food_item)
        except:
            pass

# 处理蛋白质的特殊情况（如鸡蛋、牛奶）
# 读取减脂方案表查看蛋白质食物
plan_df = pd.read_excel('体重管理.xlsx', sheet_name='1减脂-早饭后练（早起版）')

# 添加常见的蛋白质食物
protein_foods = [
    {'subcategory': '蛋奶', 'name': '鸡蛋', 'rate': 0.12, 'gi': None, 'note': '约6g蛋白质/个'},
    {'subcategory': '蛋奶', 'name': '牛奶', 'rate': 0.03, 'gi': None, 'note': '约10g蛋白质/250ml'},
    {'subcategory': '蛋奶', 'name': '酸奶', 'rate': 0.05, 'gi': None, 'note': '约10g蛋白质/200ml'},
]

for pf in protein_foods:
    if not any(f['name'] == pf['name'] for f in foods_data['蛋白质']):
        foods_data['蛋白质'].append(pf)

# 保存为JSON
output = {
    'foods': foods_data
}

with open('nutrition_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("数据提取完成！")
print(f"碳水食物: {len(foods_data['碳水'])} 种")
print(f"蛋白质食物: {len(foods_data['蛋白质'])} 种")

# 显示一些示例
print("\n碳水食物示例（前10种）:")
for f in foods_data['碳水'][:10]:
    print(f"  {f['subcategory']} - {f['name']}: {f['rate']}")

print("\n蛋白质食物:")
for f in foods_data['蛋白质']:
    print(f"  {f['subcategory']} - {f['name']}: {f['rate']}")
