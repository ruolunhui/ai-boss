from duckduckgo_search import DDGS
import json

def search_industry_news(query: str, max_results=3):
    """
    AI 员工使用的工具：联网搜索最新的行业新闻和爆款趋势
    """
    print(f"🌐 [AI 抓取中] 正在搜索全网情报: {query}...")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

def scrape_store_sales_data(store_url: str):
    """
    AI 员工使用的工具：模拟控制浏览器，登录店铺后台抓取今日销量
    （这里用 Mock 数据模拟浏览器 Playwright 的抓取结果）
    """
    print(f"📊 [AI 抓取中] 正在控制浏览器读取店铺后台数据: {store_url}...")
    
    # 在真实项目中，这里会使用 Playwright 打开网页、定位 DOM 元素并提取数据
    # 例如：page.locator('.sales-amount').inner_text()
    
    # 模拟抓取到的真实业务数据
    mock_scraped_data = {
        "date": "2026-04-06",
        "traffic": 12500,
        "products": [
            {"name": "便携式桌面加湿器 (便携小家电)", "clicks": 8000, "sales": 120, "revenue_usd": 1800, "status": "爆单"},
            {"name": "复古机械键盘 (3C数码)", "clicks": 4500, "sales": 2, "revenue_usd": 150, "status": "亏损, 广告转化极低"}
        ]
    }
    return json.dumps(mock_scraped_data, ensure_ascii=False)
