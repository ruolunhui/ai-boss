import json
from duckduckgo_search import DDGS

def web_search(query: str, max_results=3):
    """通用工具：全网搜索"""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

def read_and_extract_webpage(url: str, extraction_goal: str, llm_client, model="gpt-4o"):
    """
    通用工具：网页分析器。
    AI 老板可以派它去任何网页（后台、竞品官网、新闻网），并告诉它“去提取什么”。
    """
    print(f"🤖 [Agent]: 正在浏览 {url}，目标: {extraction_goal}...")
    
    # [模拟逻辑] 真实情况是用 Playwright 抓取网页全量 Text 或 HTML
    mock_scraped_text = f"这是从 {url} 抓取到的网页原始乱码文本和数据..." 
    
    # 使用通用 LLM 充当“数据清洗器”
    prompt = f"你是一个网页信息提取助手。网页内容: {mock_scraped_text}。请根据目标：【{extraction_goal}】提取出结构化数据。"
    
    response = llm_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
