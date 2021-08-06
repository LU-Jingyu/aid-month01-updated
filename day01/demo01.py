
"""
    汇率转换器
    first py tool
"""
_usdToCny = 6.46
_cnyToUsd = 0.15
#1. 获取数据
str_usd = input("USD: (enter 0 to quit)")

#2. 逻辑处理
res = float(str_usd) * _usdToCny

#3. 显示
print(res)

