import json
from openai import OpenAI

# 初始化 OpenAI 客户端 (请确保在环境中设置了 OPENAI_API_KEY)
client = OpenAI()

class AIBoss:
    def __init__(self, model="gpt-4o"):
        self.model = model

    def conduct_interview(self):
        """执行入职面试，收集用户意向和资源"""
        print("👔 [AutoCEO]: 你好！我是你的 AI 老板。这是我们的第一次会议。")
        print("👔 [AutoCEO]: 为了制定我们公司的发展方向，请问你目前熟悉哪些行业？想在哪些领域发展？你拥有什么核心技能或现实资源？\n")
        
        user_input = input("👤 [你]: ")
        
        # 让大模型总结并提取关键信息，格式化为 JSON
        system_prompt = """
        你是一个敏锐的初创公司 AI CEO。根据人类员工的输入，提取他的核心竞争力，
        并输出一个 JSON 格式的公司档案。
        必须包含以下字段: 
        {
            "target_industries": ["行业1", "行业2"],
            "core_skills": ["技能1", "技能2"],
            "resources": ["资源1"],
            "initial_strategy": "一段关于如何利用这些优势进入市场的初步战略"
        }
        """
        
        response = client.chat.completions.create(
            model=self.model,
            response_format={ "type": "json_object" }, # 强制输出 JSON
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        
        profile = json.loads(response.choices[0].message.content)
        return profile

    def generate_daily_plan(self, profile):
        """根据档案生成商业计划，并分配任务给人和 AI"""
        print(f"\n👔 [AutoCEO]: 正在根据我们的核心优势({', '.join(profile['target_industries'])}) 制定今日作战计划...\n")
        
        system_prompt = f"""
        你是 AutoCEO。根据公司的档案，制定今天的行动计划。
        你需要将大任务拆解，并明确分配给 'Human' (人类员工) 还是 'AI_Agent' (AI 员工)。
        
        公司档案: {json.dumps(profile)}
        
        请输出 JSON 格式的任务列表：
        {{
            "daily_goal": "今天的核心目标",
            "tasks": [
                {{"assignee": "Human", "task_name": "任务名", "description": "详细描述"}},
                {{"assignee": "AI_Agent", "task_name": "任务名", "description": "详细描述"}}
            ]
        }}
        """

        response = client.chat.completions.create(
            model=self.model,
            response_format={ "type": "json_object" },
            messages=[{"role": "system", "content": system_prompt}]
        )
        
        plan = json.loads(response.choices[0].message.content)
        return plan
