from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0,api_key='api')

def process_chat(prompt, vectorstore):
    if vectorstore:
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )
        return qa_chain.run(prompt)
    else:
        return llm.invoke(prompt)
