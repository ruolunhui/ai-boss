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
