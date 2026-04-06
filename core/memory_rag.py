import os
import chromadb
from openai import OpenAI

# 初始化 OpenAI 客户端用于生成 Embedding (文本向量化)
client = OpenAI()

class MemoryVault:
    def __init__(self, db_path="./data/chroma_db", collection_name="company_memories"):
        """初始化持久化向量数据库"""
        if not os.path.exists("./data"):
            os.makedirs("./data")
        
        # 使用持久化客户端，数据保存在本地硬盘
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        
        # 获取或创建记忆集合
        self.collection = self.chroma_client.get_or_create_collection(name=collection_name)
        print("💾 [Memory Vault] 长期记忆库已挂载。")

    def _get_embedding(self, text):
        """调用大模型将文本转化为向量 (使用最新且便宜的 embedding 模型)"""
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding

    def add_memory(self, memory_text: str, category: str, source: str):
        """
        存入新记忆
        :param memory_text: 记忆的具体内容 (比如："今天测试了TikTok广告，复古键盘亏了150刀")
        :param category: 记忆分类 ("strategy", "market_research", "vendor_feedback")
        :param source: 来源 ("daily_review", "web_scraping")
        """
        # 生成唯一 ID
        memory_id = f"mem_{self.collection.count() + 1}"
        
        # 向量化文本
        embedding = self._get_embedding(memory_text)
        
        # 存入 ChromaDB
        self.collection.add(
            ids=[memory_id],
            embeddings=[embedding],
            documents=[memory_text],
            metadatas=[{"category": category, "source": source}]
        )
        print(f"📥 [记忆归档] 已存入{category}类经验: {memory_text[:20]}...")

    def recall_memories(self, current_situation: str, n_results=3):
        """
        根据当前局势，唤醒相关的历史记忆 (RAG 核心)
        :param current_situation: 当前老板正在思考的问题 (比如："准备选品一款桌面加湿器")
        """
        if self.collection.count() == 0:
            return "[] (数据库暂无历史记忆)"

        # 将当前局势也向量化
        query_embedding = self._get_embedding(current_situation)
        
        # 在数据库中搜索最相似的历史经验
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=min(n_results, self.collection.count())
        )
        
        # 拼装检索到的记忆文本
        retrieved_docs = results['documents'][0]
        if retrieved_docs:
            print(f"💡 [记忆唤醒] AI 老板回想起了 {len(retrieved_docs)} 条相关往事...")
            return "\n".join([f"- {doc}" for doc in retrieved_docs])
        return "[] (未找到相关经验)"
