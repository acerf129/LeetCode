import bisect
import random

price_thresholds = [70, 80, 90, 100]
results = ['不合理', '超便宜', '便宜', '合理', '偏貴']

idx = bisect.bisect_left(price_thresholds, 75)
print(idx,price_thresholds)
print(random.random())