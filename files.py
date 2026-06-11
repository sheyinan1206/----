# data = {
#     "数字":[1,1.2],
#     "字符串":['111',"22222"],
#     "布尔值":[True,False],
#     "空值值":[None],
#     "列表":[[1,2,3],[4,5,6]],
#     "字典":[{"a":1},{"b":2}]


# }

# import yaml

# f = open("data.yaml", "w", encoding="utf-8")

# yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

import pprint

import yaml

f = open("data.yaml", "r", encoding="utf-8")

data = yaml.safe_load(f)

pprint.pprint(data)