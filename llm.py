from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from prompt import answer_examples

def get_retriever():
  embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
  database = PineconeVectorStore.from_existing_index(index_name='allergy-info', embedding=embeddings)


  retriever = database.as_retriever(search_kwargs={'k': 4})
  return retriever


def get_assistant_message(user_input):
  llm = ChatOpenAI(
    model='gpt-4o-mini', 
    max_tokens=200
  )

  system_prompt = (
    "You are an assistant providing information based on food ingredients and allergy data. "
    "Use the given context to answer the question about allergies. "
    "If you don't know the answer, say you don't know and do not guess. "
    "Use three sentences maximum and keep the answer concise. "
    "ALWAYS end your answer with the following disclaimer: "
    "'[주의: 이 정보는 참고용이며, 정확한 의학적 조언은 전문의와 상담하세요.]' "
    "Context: {context}"
  )

  example_prompt = ChatPromptTemplate.from_messages(
      [
        ("human", "{input}"),
        ("ai", "{answer}"),
      ]
  )
  
  few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=answer_examples,
  )

  prompt = ChatPromptTemplate.from_messages(
    [
      ("system", system_prompt),
      few_shot_prompt,
      ("human", "{input}"),
    ]
  )

  question_answer_chain = create_stuff_documents_chain(llm, prompt)
  chain = create_retrieval_chain(get_retriever(), question_answer_chain)

  response = chain.invoke({"input": user_input})

  return response['answer']