# 📚 Sistema de Recuperação de Informações com LangChain, FAISS e Ollama

Este projeto implementa um sistema local de perguntas e respostas usando LangChain, FAISS e modelos da Ollama, com base no conteúdo do Projeto Pedagógico do Curso (PPC) de TSI EaD.

---

## 🧠 Objetivo

Criar um pipeline de RAG (Recuperação Aumentada por Geração) que:

- Carrega e divide um documento PDF em pedaços (chunks)
- Cria embeddings usando o modelo `llama2` local via Ollama
- Indexa os embeddings usando FAISS
- Permite fazer perguntas respondidas por um LLM (`llama2`) com base nos trechos mais relevantes

---

## 🛠 Tecnologias

- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Ollama](https://ollama.com/)
- Python 3.10+

---

## 📁 Estrutura

```
recuperacao-informacoes/
├── data/
│   └── PPC_TSI_EaD.pdf         # Documento base (PDF)
├── main.py                     # Código principal
├── requirements.txt            # Dependências
└── README.md                   # Instruções
```

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/recuperacao-informacoes.git
cd recuperacao-informacoes
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Instale e execute o Ollama

Se ainda não tem o Ollama instalado, veja: https://ollama.com/download

Depois, baixe os modelos necessários:

```bash
ollama pull llama2
```

> ⚠️ Este projeto utiliza o modelo `llama2` para **embeddings** e **LLM**.

---

## ▶️ Executando

Coloque o arquivo `PPC_TSI_EaD.pdf` na pasta `data/` e rode:

```bash
python main.py
```

Digite perguntas como:

```text
Qual o nome do curso?
Quais os objetivos do curso?
Quantas horas de estágio são exigidas?
```

Digite `sair` para encerrar.

---

## 🧪 Modo Teste

O sistema usa apenas os **10 primeiros chunks** do PDF para acelerar o processamento.

---

## 📌 Observações

- O sistema é **100% local**, não requer conexão com APIs externas.
- Você pode substituir o PDF por outro, mantendo o mesmo caminho na pasta `data/`.

---
