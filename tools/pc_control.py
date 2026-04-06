import subprocess

def execute_terminal_command(command: str) -> str:
    """让 AI 执行本地电脑终端命令"""
    print(f"\n⚠️ [安全警告] AI 老板请求执行电脑命令: \n> {command}")
    
    # 强制安全熔断机制：必须人类同意
    user_input = input("是否允许执行？(y/n): ")
    if user_input.lower() != 'y':
        return "Command execution rejected by human employee."

    try:
        # 执行命令并获取结果
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"
