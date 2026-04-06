import os
from core.memory import load_profile, save_profile, save_plan
from core.boss import AIBoss
from tools.pc_control import execute_terminal_command

def main():
    print("==================================================")
    print("🚀 欢迎启动 AutoCEO 系统 - 为你的 AI 效劳")
    print("==================================================\n")

    boss = AIBoss()
    
    # 1. 记忆读取与初始化
    profile = load_profile()
    if not profile:
        print("📊 未检测到公司档案，启动初始化面试流程...")
        profile = boss.conduct_interview()
        save_profile(profile)
        print("\n✨ 公司档案已建立：")
        print(f"👉 目标行业: {', '.join(profile['target_industries'])}")
        print(f"👉 初步战略: {profile['initial_strategy']}\n")
    else:
        print(f"📊 已读取公司档案。当前主攻行业: {', '.join(profile['target_industries'])}")

    # 2. 老板制定计划与分配任务
    print("\n--------------------------------------------------")
    plan = boss.generate_daily_plan(profile)
    save_plan(plan)
    
    print(f"🎯 今日核心目标: {plan['daily_goal']}\n")
    
    # 3. 任务分发与执行
    for index, task in enumerate(plan['tasks']):
        print(f"[{index + 1}] 📌 分配给: {task['assignee']}")
        print(f"    - 任务名: {task['task_name']}")
        print(f"    - 描述: {task['description']}")
        print("    - 状态: 等待执行...\n")

        # 简单的执行逻辑分支
        if task['assignee'] == "Human":
            input(f"👤 [人类员工]: 请去完成上述任务，完成后按 Enter 键向老板汇报打卡...")
            print("✅ 汇报成功。")
            
        elif task['assignee'] == "AI_Agent":
            print(f"🤖 [AI 员工]: 正在后台执行 {task['task_name']}...")
            # 这里未来可以接入具体的 Agent (比如联网搜索 Agent)
            # 举个电脑控制的例子：如果任务需要写一个文件
            if "文件" in task['task_name'] or "代码" in task['task_name']:
                # 测试: 建议 AI 创建一个测试文件
                cmd_response = execute_terminal_command('echo "Hello from AutoCEO" > test_output.txt')
                print(f"🤖 [AI 员工] 执行结果: {cmd_response}")
            print("✅ AI 执行完毕。")
            
    print("\n👔 [AutoCEO]: 今天的任务都已完成。干得不错，明天见。")

if __name__ == "__main__":
    # 运行前确保执行过: export OPENAI_API_KEY="your_api_key"
    main()
