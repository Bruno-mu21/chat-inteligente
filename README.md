# 🤖 Assistente Inteligente de Suporte Técnico (NLP & Tkinter)

> Chatbot interativo com interface gráfica desenvolvido em **Python**, utilizando técnicas de Processamento de Linguagem Natural (**TF-IDF** e **Similaridade do Cosseno**) via **Scikit-Learn** e interface gráfica com **Tkinter**[cite: 26].

---

## 📌 Sobre o Projeto

O **Assistente de Suporte Técnico** é uma aplicação desktop desenvolvida para solucionar dúvidas recorrentes de informática, redes, hardware e segurança da informação[cite: 26].

Diferente de sistemas baseados em correspondência estrita de palavras-chave, este assistente utiliza representação vetorial com **TF-IDF (Term Frequency-Inverse Document Frequency)** e calcula a **Similaridade do Cosseno** entre a dúvida digitada pelo usuário e os tópicos da sua base de conhecimento[cite: 26]. Caso a pontuação de relevância fique abaixo de um limiar (*threshold* de 0.5), o sistema orienta o usuário a acionar o suporte técnico humano[cite: 26].

---

## ✨ Principais Funcionalidades

- 🧠 **Recuperação Inteligente de Respostas (NLP / ML)**:
  - Extração de características e vetorização de texto via `TfidfVectorizer`[cite: 26].
  - Identificação da melhor resposta utilizando a métrica `cosine_similarity`[cite: 26].
  - Resposta padrão com encaminhamento para suporte humano para perguntas não contempladas[cite: 26].
- 💬 **Interface Gráfica Desktop Amigável**:
  - Janela desenvolvida em `tkinter` com layout em balões de diálogo (estilo chat de mensagens)[cite: 26].
  - Campo de entrada de texto com envio via botão ou encerramento rápido com a palavra `sair`[cite: 26].
- 💻 **Base de Conhecimento Especializada**:
  - Dúvidas sobre tela azul (BSOD), drivers, limpeza de cache, vírus/malware, VPN, segurança Wi-Fi, lentidão do computador, integridade de disco (CHKDSK), entre outros tópicos[cite: 26].

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)[cite: 26]
- **NLP & Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (`TfidfVectorizer`, `cosine_similarity`)[cite: 26]
- **Interface Gráfica (GUI):** `tkinter` (módulo nativo do Python)[cite: 26]

---

## 📁 Estrutura de Arquivos

```text
.
├── Chat inteligente.py      # Código-fonte principal com a base de conhecimento e interface gráfica[cite: 26]
├── icon.ico                 # Ícone da janela do assistente (opcional)[cite: 26]
└── README.md                # Documentação do projeto

Como Executar o Projeto
Pré-requisitos
Python 3.8 ou superior instalado.

Instalação da biblioteca scikit-learn.

Passo a Passo
Clone o repositório:

Bash


git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
cd NOME-DO-REPOSITORIO
Crie e ative um ambiente virtual (recomendado):

Bash


# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash


pip install scikit-learn
Inicie o assistente:

Bash


python "Chat inteligente.py"
💡 Como Funciona o Processamento de Texto
Plaintext


[Dúvida digitada pelo Usuário]
              │
              ▼
    [Vetorização TF-IDF]
              │
              ▼
[Similaridade do Cosseno vs. Base]
              │
    ┌─────────┴─────────┐
    ▼                   ▼
Score >= 0.5        Score < 0.5
    │                   │
Exibe resposta      Recomenda suporte humano
do assistente       via e-mail
