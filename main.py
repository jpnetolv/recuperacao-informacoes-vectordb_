from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

def main():
    print("🔄 Carregando e processando o PDF...")
    loader = PyPDFLoader(r"data/PPC_TSI_EaD.pdf")
    pages = loader.load()
    print(f"✅ Documento carregado e dividido em {len(pages)} páginas.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(pages)
    print(f"✅ Documento dividido em {len(texts)} chunks.")

    texts = texts[:10]  # modo teste rápido para acelerar
    print("⚡ Modo teste rápido ativado: usando apenas 10 chunks.")

    print("🧮 Criando embeddings...")
    embeddings = OllamaEmbeddings(model="llama2")
    print("✅ Embeddings criados.")

    print("🧩 Construindo índice FAISS...")
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()

    print("🤖 Configurando modelo Ollama LLM...")
    llm = OllamaLLM(model="llama2")

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    print("\n✅ Sistema pronto! Faça perguntas (digite 'sair' para encerrar):")
    while True:
        query = input("\nPergunta: ")
        if query.lower() in ("sair", "exit", "quit"):
            print("👋 Encerrando.")
            break
        answer = qa.invoke({"query": query})["result"]
        print(f"\nResposta:\n{answer}")

if __name__ == "__main__":
    main()
