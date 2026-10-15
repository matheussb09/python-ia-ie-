# Importando a biblioteca e nomeando de tk
import tkinter as tk
import random
import string
LARGURA = "450"
ALTURA = "400"

def gerar_senha():
    try:
        tamanho = int(entry_tamanho_senha.get())
        #Verificando se a quantidade de caracteres definida é menor do que 4
        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: Mínimo de 4 caracteres!",
                fg="#ff5555"
            )
            return

        caracteres = ""
        if var_maiuscula.get():
            caracteres += string.ascii_uppercase
        if var_minuscula.get():
                caracteres += string.ascii_lowercase
        if var_numeros.get():
                caracteres += string.digits
        if var_simbolos.get():
                caracteres += string.punctuation
        
        
        
        if not caracteres:
              lbl_resultado.config(
                    text= "Erro Selecione ao menos uma opção!",
                    fg="#ff5555"
                )
              return
           
        senha = "".join(random.choice(caracteres) for i in range(tamanho))

        lbl_resultado.config(
             text = f"Senha: {senha}",
             fg="#50fa7b"
        )



    except ValueError:
         lbl_resultado.config(
              text="Erro: Digite um número válido",
              fg="#ff5555"
         )
def copiar_senha():
    texto_resultado = lbl_resultado.cget("text")

    if "Senha: " in texto_resultado:
        senha_pura = texto_resultado.replace("Senha: ","")
          
          
          
        janela.clipboard_clear()
        janela.clipboard_append(senha_pura)
    else:
         lbl_status_copia.cofig(
              text= "Gere uma senha primeiro!",
              fg= "#ff5555"
            
         )
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

#6. Criar botão gerador de senha
bnt_gerar = tk.Button(
    janela,
    text="Gerar senha Segura",
    command=gerar_senha,
    bg="#00ffcc",
    fg="#1e1e2e",
    padx=10,
    pady=5
)
bnt_gerar.pack(pady=15)

#Label que apresenta o resultado no programa
lbl_resultado= tk.Label(
     text="A senha aparecerá aqui",
     font=("Arial",11,"bold"),
     fg="#f8f8f2"
)
lbl_resultado.pack(pady=5)

btn_copiar = tk.Button(
     janela,
     text="Copiar Senha",
     command=copiar_senha,
     font=("Arial",10,"bold"),
     bg = "#3b4252",
     fg = "#eceff4",
     padx=10,
     pady=3,
)
btn_copiar.pack(pady=5)

lbl_status_copia = tk.Label(
     janela,
     text="",
     font=("Arial",9),
     bg=("#1e1e2e"),
     fg=("#50fa7b")

)

lbl_status_copia.pack()

#==========================================
#1. LOOP PRINCIPAL (Mantém a janela aberta)
#==========================================
#1. Mantém a janela aberta rodando
janela.mainloop()