# RAG 智能客服 Demo

这是一个基于 LangChain、Chroma 和 Streamlit 的 RAG 知识库问答项目。

项目包含两个 Streamlit 页面：

- `app_file_uploader.py`：上传 TXT 文件，将文本切分后写入本地 Chroma 向量库。
- `app_qa.py`：智能客服问答页面，根据用户问题检索知识库内容，并结合对话历史生成回答。

## 功能

- TXT 文档上传
- 文本自动切分
- 文档内容向量化
- 本地 Chroma 向量库持久化
- 基于知识库的问答
- 本地文件保存会话历史
- 使用 MD5 避免重复导入相同内容

## 项目结构

```text
.
├── app_file_uploader.py    # 知识库上传页面
├── app_qa.py               # 智能客服问答页面
├── config_data.py          # 项目配置
├── file_history_store.py   # 本地聊天历史存储
├── knowledge_base.py       # 知识库写入服务
├── rag.py                  # RAG 问答链
├── vector_stores.py        # Chroma 向量检索封装
└── README.md
```

## 运行前准备

建议使用虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

安装依赖：

```bash
pip install streamlit langchain langchain-community langchain-chroma langchain-deepseek langchain-text-splitters dashscope
```

根据使用的模型服务配置对应环境变量，例如：

```bash
export DASHSCOPE_API_KEY="你的 DashScope API Key"
export DEEPSEEK_API_KEY="你的 DeepSeek API Key"
```

## 运行方式

启动知识库上传页面：

```bash
streamlit run app_file_uploader.py
```

启动智能客服页面：

```bash
streamlit run app_qa.py
```

## 本地运行数据

以下内容是运行时生成的数据，已经通过 `.gitignore` 排除，不会提交到 Git：

- `chroma_db/`：本地 Chroma 向量库
- `chat_history/`：本地聊天历史
- `md5.text`：已导入内容的 MD5 记录
- `__pycache__/`：Python 缓存文件

## 说明

当前项目默认使用：

- Embedding 模型：`text-embedding-v4`
- Chat 模型：`deepseek-chat`
- 向量库集合名：`rag`

相关配置可以在 `config_data.py` 中修改。
