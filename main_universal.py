from core.universal_boss import UniversalAIBoss
import json

def run_company(company_name, profile):
    print("="*60)
    print(f"🏢 启动公司: {company_name}")
    print(f"👉 赛道: {profile['industries']}")
    print("="*60)

    boss = UniversalAIBoss()
    
    # 第一阶段：AI 老板进行初步战略规划
    plan = boss.formulate_strategy(company_profile=profile)
    
    print(f"\n👔 [CEO 思考]: {plan['ceo_thoughts']}")
    print(f"🎯 [核心决策]: {plan['strategic_decision']}\n")
    
    print("📋 [任务清单]:")
    for task in plan['tasks']:
        if task['assignee'] == 'Human':
            print(f"  👤 [分配给人类]: {task['task_name']} - {task['description']}")
        else:
            print(f"  🤖 [分配给 AI]: {task['task_name']} (使用工具: {task['tool_to_use']})")

    # 假设这里是 AI 自动执行完毕，并且人类也提交了打卡反馈
    # 这里模拟获取到了一些新数据 (比如电商得到了销量，做软件得到了用户反馈)
    print("\n... 一段时间后，收集到了新的执行反馈与数据 ...\n")
    
    mock_feedback_data = ""
    if "跨境电商" in profile['industries']:
        mock_feedback_data = "人类已联系工厂拿货，AI 查到的网页数据：商品A昨日销售额3000美金，转化率极高。"
    elif "软件开发" in profile['industries']:
        mock_feedback_data = "人类已完成架构设计，AI 从 Github 提取的信息：目前开源社区最火的同类项目缺少多模态支持。"

    # 第二阶段：通用 AI 老板根据新数据，重新进行 OODA 循环，修正战略
    print("🔄 [触发战略复盘更新]")
    profile['current_phase'] = "已有初步反馈，进入迭代期"
    updated_plan = boss.formulate_strategy(company_profile=profile, external_data=mock_feedback_data)
    
    print(f"\n👔 [CEO 新思考]: {updated_plan['ceo_thoughts']}")
    print(f"🎯 [最新决策]: {updated_plan['strategic_decision']}")


if __name__ == "__main__":
    
    # 案例 1：完全用这套代码跑【跨境电商】
    ecommerce_profile = {
        "industries": "跨境电商, TikTok 独立站",
        "resources": "5万人民币起步资金, 会剪辑视频, 有国内小商品供应链",
        "current_phase": "寻找第一批爆款"
    }
    run_company("赛博出海贸易公司", ecommerce_profile)
    
    print("\n\n" + "*"*60 + "\n\n")

    # 案例 2：一字不改核心代码，用同样的逻辑跑【AI 软件开发工作室】
    software_profile = {
        "industries": "AI 辅助编程工具开发, SaaS",
        "resources": "1名资深全栈工程师(人类), 熟悉 Python/React, 无推广预算",
        "current_phase": "构思 MVP(最小可行性产品)"
    }
    run_company("未来代码实验室", software_profile)
