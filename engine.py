from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

def get_answer_from_engine(query, vector_store):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    
    return qa_chain.invoke(query)