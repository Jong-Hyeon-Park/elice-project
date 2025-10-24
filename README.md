# 🤧 알레르기 정보 RAG 챗봇

Streamlit, LangChain, OpenAI, Pinecone을 사용하여 구축한 RAG(검색-증강-생성) 기반 알레르기 정보 챗봇입니다.

## 1. 개발 환경

-   **Frontend:** Streamlit
-   **LLM:** OpenAI (gpt-4o-mini)
-   **Embedding:** OpenAI (text-embedding-3-large)
-   **Vector DB:** Pinecone
-   **Orchestration:** LangChain

## 2. 실행 방법

### 1. 라이브러리 설치
(가상환경을 생성한 후)
```bash
pip install -r requirements.txt

## 챗봇 서버 실행
streamlit run chat_bot.py