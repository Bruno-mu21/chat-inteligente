import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Base de Conhecimento do Suporte
knowledge_base = [
    {"question": "não liga", "answer": "Verifique se o cabo de alimentação está conectado corretamente."},
    {"question": "vírus", "answer": "Execute um programa antivírus atualizado."},
    {"question": "drivers", "answer": "Visite o site do fabricante do hardware e baixe os drivers mais recentes."},
    {"question": "tela azul morte", "answer": "A tela azul da morte (BSOD) geralmente indica um problema sério no sistema operacional."},
    {"question": "cache", "answer": "Dependendo do navegador, vá para as configurações e procure a opção de limpar o cache."},
    {"question": "phishing", "answer": "Phishing é uma tentativa de enganar as pessoas para revelar informações confidenciais, como senhas e detalhes de cartão de crédito."},
    {"question": "velocidade computador?", "answer": "Remova programas desnecessários, atualize o hardware ou considere a desfragmentação do disco."},
    {"question": "wifi lento", "answer": "Verifique a conexão, reinicie o roteador e evite interferências de outros dispositivos."},
    {"question": "firewall", "answer": "Um firewall é um software ou hardware que monitora e controla o tráfego de rede, protegendo contra ameaças."},
    {"question": "restaurar", "answer": "Vá para as configurações do sistema e procure a opção de restauração do sistema."},
    {"question": "superaquecendo", "answer": "Certifique-se de que o sistema de refrigeração está funcionando corretamente e limpe eventuais obstruções."},
    {"question": "DLL", "answer": "Um arquivo DLL (Dynamic Link Library) contém código e dados que podem ser usados por mais de um programa simultaneamente."},
    {"question": "recuperar excluídos", "answer": "Use um programa de recuperação de dados antes que o espaço seja sobrescrito por novos dados."},
    {"question": "RAM", "answer": "RAM (Random Access Memory) é uma memória temporária usada pelo sistema operacional e aplicativos em execução."},
    {"question": "áudio", "answer": "Verifique as configurações de áudio, atualize os drivers e certifique-se de que os alto-falantes estejam conectados corretamente."},
    {"question": "SSD", "answer": "Um SSD (Solid State Drive) é um tipo de dispositivo de armazenamento mais rápido e durável do que os discos rígidos tradicionais."},
    {"question": "integridade", "answer": "Use a ferramenta CHKDSK para verificar e corrigir erros no disco rígido."},
    {"question": "IP estático", "answer": "Um IP estático é um endereço IP que não muda, ao contrário de um IP dinâmico, que pode ser atribuído automaticamente."},
    {"question": "malware", "answer": "Use um bom antivírus, mantenha o sistema e os programas atualizados e evite clicar em links suspeitos."},
    {"question": "senha", "answer": "Use uma combinação de letras maiúsculas e minúsculas, números e caracteres especiais, evite palavras comuns e mantenha-a longa."},
    {"question": "acelerar inicialização", "answer": "Desabilite programas desnecessários que são iniciados junto com o sistema. Você pode fazer isso no Gerenciador de Tarefas."},
    {"question": "nuvem", "answer": "A nuvem refere-se ao armazenamento e processamento de dados pela internet. É como ter um disco rígido online, permitindo o acesso a dados de qualquer lugar."},
    {"question": "diferença hardware software?", "answer": "Hardware são os componentes físicos do computador, como processador e disco rígido, enquanto software são os programas e aplicativos que executam tarefas no computador."},
    {"question": "segurança wifi?", "answer": "Além de usar uma senha forte, ative a criptografia WPA3, oculte oM nome da rede (SSID), e atualize regularmente a senha para evitar acessos não autorizados."},
    {"question": "VPN", "answer": "Uma VPN (Virtual Private Network) é uma conexão segura que cria uma rede privada sobre a internet pública, protegendo a privacidade e a segurança dos dados."},
    {"question": "fadiga visual longos períodos", "answer": "Faça pausas regulares, ajuste o brilho e contraste do monitor, e certifique-se de que o ambiente de trabalho tem iluminação adequada."},
    {"question": "Modo Avião", "answer": "O Modo Avião desativa todas as conexões sem fio do dispositivo, como Wi-Fi e Bluetooth, sendo útil durante viagens de avião e para economizar bateria."},
    {"question": "programação programar?", "answer": "Programação é a criação de instruções para computadores executarem tarefas. Aprender a programar proporciona habilidades analíticas, lógicas e a capacidade de criar soluções para problemas."},
    {"question": "superaquecimento laptop?", "answer": "Certifique-se de que as saídas de ventilação não estejam bloqueadas, use o laptop em uma superfície plana e considere o uso de bases de resfriamento."},
    {"question": "software código aberto", "answer": "Software de código aberto é aquele cujo código-fonte é disponibilizado ao público, permitindo que qualquer pessoa o visualize, modifique e distribua."},
    {"question": "organizar arquivos", "answer": "Crie pastas específicas para diferentes tipos de arquivos, renomeie-os de forma descritiva e faça backup regularmente para evitar a perda de dados importantes."},
    {"question": "navegador", "answer": "Um navegador da web é um aplicativo que permite a navegação na internet. Exemplos incluem Google Chrome, Mozilla Firefox e Microsoft Edge."},
    {"question": "compartilhar impressora", "answer": "Conecte a impressora ao computador host, vá para as configurações de compartilhamento e ative a opção de compartilhamento de impressora."},
    {"question": "cookiesE internet?", "answer": "Cookies são pequenos arquivos de texto armazenados no seu navegador que contêm informações sobre suas atividades online, sendo usados para personalizar a experiência de navegação."}
]

# Vetorização do texto
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(
    [item["question"] for item in knowledge_base] + [item["answer"] for item in knowledge_base])

# Variável global para controlar a linha atual no chat
chat_row = 1


# Função para obter a resposta
def get_answer(user_question):
    user_question_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_question_vector, tfidf_matrix)
    index_of_best_match = similarities.argmax()
    best_match_similarity = similarities[0, index_of_best_match]
    best_match = knowledge_base[index_of_best_match % len(knowledge_base)]

    similarity_threshold = 0.5

    if best_match_similarity < similarity_threshold:
        return "Desculpe, não possuo informações suficientes para ajudá-lo. Por favor, entre em contato com o nosso técnico pelo e-mail a seguir: fabinpro@uvatech.com."
    else:
        return best_match["answer"]


# Função chamada quando o botão "Enviar" é clicado
def submit_question():
    user_question = user_input.get()

    if user_question.lower() == 'sair':
        root.destroy()  # Fecha a janela se o usuário digitar 'sair'
    else:
        answer = get_answer(user_question)
        display_user_message(user_question)
        display_bot_message(answer)
        user_input.delete(0, tk.END)  # Limpa a caixa de entrada após cada pergunta


# Função para exibir mensagem do usuário
def display_user_message(message):
    user_message = f"{message}"
    create_bubble(user_message, "right")


# Função para exibir mensagem do bot
def display_bot_message(message):
    bot_message = f"Assistente: {message}"
    create_bubble(bot_message, "left")


# Função para criar bolhas de mensagem
def create_bubble(message, side):
    global chat_row

    bubble_frame = tk.Frame(chat_canvas, bg="#E0E0E0", bd=1, relief=tk.GROOVE)
    bubble_text = tk.Label(bubble_frame, text=message, wraplength=300, justify=tk.LEFT, bg="#E0E0E0",
                           font=("Arial", 10), padx=10, pady=5)

    if side == "right":
        bubble_frame.grid(row=chat_row, column=1, sticky=tk.E)
        bubble_text.pack()
    elif side == "left":
        bubble_frame.grid(row=chat_row, column=0, sticky=tk.W)
        bubble_text.pack()

    chat_row += 1


# Configuração da interface gráfica
root = tk.Tk()
root.title("Assistente de Suporte Técnico")
root.configure(bg='#87CEEB')  # Altera o fundo geral para um azul mais escuro

# Defina o ícone da janela
root.iconbitmap('icon.ico')  # Substitua pelo caminho real do seu ícone

root.title("Assistente de Suporte Técnico")
root.configure(bg='#87CEEB')  # Altera o fundo geral para um azul mais escuro


# Retângulo no topo do chat com o nome do bot
header_label = tk.Label(root, text="Assistente de Suporte Técnico", bg='#4682B4', fg='#FFFFFF',
                        font=("Arial", 14, "bold"), relief=tk.GROOVE, padx=10, pady=10)
header_label.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)  # Use grid em vez de pack

# Área para exibir a resposta do programa com bordas arredondadas
chat_canvas = tk.Canvas(root, bg='#87CEEB', highlightthickness=0)
chat_canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

# Adicionando a mensagem inicial do bot
initial_bot_message = "Bem-vindo ao Assistente Suporte Técnico UVA! Qual é a sua dúvida?"
display_bot_message(initial_bot_message)

# Área para o usuário inserir perguntas
user_input = tk.Entry(root, width=50, font=("Arial", 10), bd=2, relief=tk.GROOVE)
user_input.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W + tk.E)  # Use grid em vez de pack

# Retângulo na parte inferior onde o usuário pode escrever suas mensagens
submit_button = tk.Button(root, text="Enviar", command=submit_question, bg='#4682B4', fg='#FFFFFF', relief=tk.GROOVE,
                          font=("Arial", 10), padx=10, pady=10, bd=2)
submit_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W + tk.E)  # Use grid em vez de pack

# Iniciar a interface gráfica
root.mainloop()