import json


class JsonGenerator(object):
    def evaluate(self, keys, *values):
        if keys is None or len(keys) == 0:
            return ""
        res = []

        # 每个字段的值
        for value in values:
            print(value)
            # 获得对应的Json
            assert len(keys) == len(value), "len(keys) != len(values), values="+value
            row = {}  # 单个字段的key-value
            for i in range(len(value)):
                if keys[i] == 'rt_srcType' and value[i] == 0:
                    break
                row[keys[i]] = value[i]
            if len(row) == len(keys):
                res.append(row)

        return json.dumps(res)


s = JsonGenerator()
print(s.evaluate(("ri_id", "ri_value", "rt_id", "ri_ruleName", "ri_type", "rt_srcType"),
                 ("4", "", "47", "最近一次全店离线", 0, 1), ("5", "", "47", "最近三日全店离线", 0, 1)))
