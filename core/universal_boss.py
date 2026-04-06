import json
from openai import OpenAI
from core.memory_rag import MemoryVault

client = OpenAI()

class UniversalAIBoss:
    def __init__(self, model="gpt-4o"):
        self.model = model
        self.memory_vault = MemoryVault() # 挂载老板的长期记忆系统

    def formulate_strategy(self, company_profile, current_challenge_or_data=""):
        """
        搭载了 RAG 的战略制定方法。
        """
        print("🧠 [AutoCEO 思考中] 正在查阅公司历史档案与经验库...")
        
        # 【核心 RAG 步骤】：用当前面临的挑战去搜索历史记忆
        query_intent = f"行业: {company_profile.get('industries')}。当前面临的情况/数据: {current_challenge_or_data}"
        past_experiences = self.memory_vault.recall_memories(current_situation=query_intent)

        system_prompt = f"""
        你是 AutoCEO 系统的核心大脑。
        
        【公司当前状态档案】
        所属行业: {company_profile.get('industries')}
        核心资源/能力: {company_profile.get('resources')}
        
        【近期外部情报/复盘数据】
        {current_challenge_or_data if current_challenge_or_data else "无最新数据"}

        【历史经验教训 (长期记忆唤醒)】
        请绝对重视以下历史经验，避免踩坑，或复制成功的路径：
        {past_experiences}

        作为理智的 CEO，请结合历史经验和当前局势，输出你的通用决策与任务。
        必须严格输出 JSON 格式：
        {{
            "ceo_thoughts": "老板的思考过程，特别是如何结合【历史经验】做出的判断",
            "strategic_decision": "接下来的核心战略决策",
            "tasks": [
                {{"assignee": "Human", "task_name": "任务名称", "description": "详细描述"}}
            ]
        }}
        """

        response = client.chat.completions.create(
            model=self.model,
            response_format={ "type": "json_object" },
            messages=[{"role": "system", "content": system_prompt}]
        )
        
        plan = json.loads(response.choices[0].message.content)
        
        # 【记忆闭环】：决策做完后，将这次的战略反思作为新记忆存入大脑，供未来使用！
        memory_to_save = f"在面临 '{current_challenge_or_data}' 时，做出了决策: {plan['strategic_decision']}。思考逻辑: {plan['ceo_thoughts']}"
        self.memory_vault.add_memory(memory_to_save, category="strategy_decision", source="ceo_brain")
        
        return plan
        
    def add_external_feedback_to_memory(self, feedback_text):
        """让员工（人类或AI）把执行结果汇报给老板，存入记忆库"""
        self.memory_vault.add_memory(
            memory_text=feedback_text, 
            category="execution_feedback", 
            source="employee_report"
        )
