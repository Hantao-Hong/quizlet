import json, re, sys
TAIL_RE = re.compile(r"\s*答案[:：]\s*[\u4e00-\u9fa5A-D]+$")

with open("qbank.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item["question"] = TAIL_RE.sub("", item["question"]).strip()

with open("new.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
