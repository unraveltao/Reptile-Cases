import pandas as pd
# pandas --> 创建一个数据表格，对数据表格进行相关操作，最后将数据表格同步到excel

# 1. 创建数据表格
table = pd.DataFrame(columns = ['names', 'salary', 'job_title'])

# 2. 数据表格插入数据
table.loc[0] = ['Jay',4000,'singer']
table.loc[1] = ['Tom',10000,'sale']
print(table)
# 3.将数据表格转化成 Excel
table.to_excel('test2.xlsx', sheet_name='sheet1_name')