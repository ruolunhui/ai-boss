import json
from openai import OpenAI
from tools.universal_tools import web_search, read_and_extract_webpage

client = OpenAI()

class UniversalAIBoss:
    def __init__(self, model="gpt-4o"):
        self.model = model

    def formulate_strategy(self, company_profile, external_data=""):
        """
        通用的战略制定方法。
        根据读取的行业、资源、以及近期收集的情报，推演出下一步干什么。
        """
        system_prompt = f"""
        你是 AutoCEO 系统的核心大脑。你现在是一家初创公司的全权 CEO。
        
        【公司当前状态档案】
        所属行业: {company_profile.get('industries')}
        核心资源/能力: {company_profile.get('resources')}
        当前阶段: {company_profile.get('current_phase', '刚成立，寻找切入点')}
        
        【近期外部情报/复盘数据】
        {external_data if external_data else "无最新数据"}

        作为极其理智的 CEO，请思考当前的商业环境，并输出你的通用决策与任务。
        必须严格输出 JSON 格式：
        {{
            "ceo_thoughts": "老板的思考过程，分析当前局势和数据",
            "strategic_decision": "接下来的核心战略决策",
            "tasks": [
                {{
                    "assignee": "Human", 
                    "task_name": "任务名称", 
                    "description": "详细描述要求",
                    "expected_outcome": "预期人类交付的结果"
                }},
                {{
                    "assignee": "AI_Agent", 
                    "tool_to_use": "web_search / read_webpage / pc_control", 
                    "task_name": "任务名称", 
                    "tool_params": "如果是搜索，搜什么？如果是读网页，URL和提取目标是什么？"
                }}
            ]
        }}
        """

        print(f"🧠 [AutoCEO 思考中] 正在结合 {company_profile.get('industries')} 行业特质进行推演...")
        response = client.chat.completions.create(
            model=self.model,
            response_format={ "type": "json_object" },
            messages=[{"role": "system", "content": system_prompt}]
        )
        return json.loads(response.choices[0].message.content)

    def execute_ai_tasks(self, plan):
        """通用执行器：根据计划中的要求，动态调用工具箱"""
        ai_results = {}
        for task in plan.get("tasks", []):
            if task["assignee"] == "AI_Agent":
                tool = task.get("tool_to_use")
                params = task.get("tool_params")
                
                print(f"🤖 [AI 员工] 接收任务: {task['task_name']}")
                
                # 动态工具路由
                if tool == "web_search":
                    result = web_search(params)
                    ai_results[task['task_name']] = result
                elif tool == "read_webpage":
                    # 解析 JSON 中的 URL 和目标
                    # 实际工程中这里用 OpenAI Function Calling 会更标准
                    pass 
                
        return ai_results
