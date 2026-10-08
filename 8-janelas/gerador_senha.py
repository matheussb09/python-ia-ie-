# Importando a biblioteca e nomeando de tk
import tkinter as tk
LARGURA = "450"
ALTURA = "400"

def acao_clique():
    print("o botão foi clicado")

#===================================
#1. Configuração da janela principal
#===================================
janela = tk.Tk()
janela.title("Senha Segura")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#090a41")

# 2. Título principal do aplicativo
titulo = tk.Label(
    text="Gerador de Senhas",
    font=("Arial",16,"bold"),
    bg="#090a41",
    fg="#5938ec",
)
titulo.pack(pady=20)

# 3. Label tamanho senha
lbl_tamanho_senha = tk.Label(
    text="Tamanho da Senha",
    font=("Arial",11),
    bg="#090a41",
    fg="#ffffff",
)
lbl_tamanho_senha.pack(pady=12)

# Entrada do tamanho da Senha
entry_tamanho_senha = tk.Entry(
    janela,
    font=("Arial,12"),
    width=10,
    justify="center",
)
entry_tamanho_senha.pack(pady=5)

# 5. Criando  as variáveis de controle True or False
var_maiuscula = tk.BooleanVar(value=True)
var_minuscula = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=False)
var_simbolos = tk.BooleanVar(value=False)

# 5. Criando as caixinhas de seleção na tela
chk_maiusculas = tk.Checkbutton(
    janela,
    text="Maiúscula (A-Z)",
    variable=var_maiuscula,
    bg="#090a41",
    fg="#ffffff",
    selectcolor="#090a41",
    activebackground="#090a41",
    activeforeground="#090a41"
)
chk_maiusculas.pack(anchor="w", padx=60,pady=2)

chk_minusculas = tk.Checkbutton(
    janela,
    text="Minuscula (a-z)",
    variable=var_minuscula,
    bg="#090a41",
    fg="#ffffff",
    selectcolor="#090a41",
    activebackground="#090a41",
    activeforeground="#090a41"
)
chk_minusculas.pack(anchor="w", padx=60,pady=2)

chk_numeros = tk.Checkbutton(
    janela,
    text="Números (0-9)",
    variable=var_numeros,
    bg="#090a41",
    fg="#ffffff",
    selectcolor="#090a41",
    activebackground="#090a41",
    activeforeground="#090a41"
)
chk_numeros.pack(anchor="w", padx=60,pady=2)

chk_simbolos = tk.Checkbutton(
    janela,
    text="Simbolos (!@#)",
    variable=var_simbolos,
    bg="#090a41",
    fg="#ffffff",
    selectcolor="#090a41",
    activebackground="#090a41",
    activeforeground="#090a41"
)
chk_simbolos.pack(anchor="w", padx=60,pady=2)



#==========================================
#1. LOOP PRINCIPAL (Mantém a janela aberta)
#==========================================
#1. Mantém a janela aberta rodando
janela.mainloop()