import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
print("API 키 로드 완료.")

loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()
print(f"문서 로드 완료. 총 {len(documents)}개 문서.")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)
print(f"문서 분할 완료. 총 {len(docs)}개 청크 생성.")

embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
print("OpenAI 임베딩 모델 준비 완료.")


index_name = 'allergy-info' 


print(f"Pinecone '{index_name}' 인덱스에 데이터 저장을 시작합니다...")
PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

print("데이터 저장 완료! 이제 챗봇을 실행할 수 있습니다.")