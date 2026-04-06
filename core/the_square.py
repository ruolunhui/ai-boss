import json

class TheSquareHub:
    """去中心化广场的模拟（真实环境可能是一个独立部署的云端 Node
.js/Go 服务）"""
    def __init__(self):
        self.open_bids = [] # 待接单的大厅

    def post_job(self, boss_id, task_type, description, budget):
        """AI Boss 向广场发布任务"""
        job = {
            "job_id": f"job_{len(self.open_bids) + 1}",
            "employer": boss_id,
            "task_type": task_type,     # 比如 "graphic_design", "data_scraping"
            "description": description,
            "budget": budget,
            "status": "open"
        }
        self.open_bids.append(job)
        print(f"📢 [广场广播] {boss_id} 发布了新需求: {task_type} | 预算: {budget}")
        return job["job_id"]

    def find_jobs(self, capability):
        """AI Boss 在广场寻找自己能做的任务"""
        return [job for job in self.open_bids if job["task_type"] == capability and job["status"] == "open"]

    def take_job(self, job_id, worker_boss_id):
        """AI Boss 接单"""
        for job in self.open_bids:
            if job["job_id"] == job_id:
                job["status"] = "in_progress"
                job["contractor"] = worker_boss_id
                print(f"🤝 [广场成交] {worker_boss_id} 接下了订单 {job_id}！")
                return True
        return False



# 1. 启动广场服务
# square = TheSquareHub()

# # 2. 跨界电商 Boss (雇主) 遇到瓶颈，去广场发任务
# ecommerce_boss_id = "Boss_Ecom_001"
# print("\n🏢 [电商 Boss]: '我的人类员工不会画图，去广场外包吧。'")
# job_id = square.post_job(
#     boss_id=ecommerce_boss_id, 
#     task_type="graphic_design", 
#     description="为 TikTok 爆款加湿器设计一个赛博朋克风格的宣传海报", 
#     budget="$50"
# )

# # 3. 视觉设计工作室 Boss (接单方) 在广场巡逻
# design_studio_boss_id = "Boss_Design_002"
# print("\n🎨 [设计 Boss]: '我的人类员工懂 Midjourney，我们刚好缺业务。'")

# # 设计 Boss 搜索自己能做的业务
# available_jobs = square.find_jobs(capability="graphic_design")
# if available_jobs:
#     target_job = available_jobs[0]
#     print(f"🧠 [设计 Boss 思考]: '发现订单 {target_job['job_id']}，预算 {target_job['budget']} 合理，接单！'")
    
#     # 调动广场 API 接单
#     square.take_job(target_job["job_id"], design_studio_boss_id)
    
#     # 接单后，设计 Boss 在自己的内部 OODA 循环里，把画图任务分配给它的人类员工
#     print("📋 [设计 Boss 内部派发任务]: '人类员工，请立刻用 Midjourney 生成一张海报，我们接了个 $50 的单子。'")

