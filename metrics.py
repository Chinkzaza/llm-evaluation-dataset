import json

with open("sample_data.json") as f:
    data = json.load(f)

def evaluate_responses(dataset):
    for item in dataset:
        print(f"Task {item['id']}: Input='{item['input']}' | Expected='{item['expected']}'")

evaluate_responses(data)
