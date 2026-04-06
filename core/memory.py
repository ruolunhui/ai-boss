import json
import os

DATA_DIR = "./data"
PROFILE_FILE = os.path.join(DATA_DIR, "company_profile.json")
PLAN_FILE = os.path.join(DATA_DIR, "business_plan.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_profile():
    ensure_data_dir()
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_profile(profile_data):
    ensure_data_dir()
    with open(PROFILE_FILE, 'w', encoding='utf-8') as f:
        json.dump(profile_data, f, ensure_ascii=False, indent=4)
    print("💾 [Memory] 公司与员工档案已保存。")

def save_plan(plan_data):
    ensure_data_dir()
    with open(PLAN_FILE, 'w', encoding='utf-8') as f:
        json.dump(plan_data, f, ensure_ascii=False, indent=4)
    print("💾 [Memory] 最新商业计划与任务已保存。")
