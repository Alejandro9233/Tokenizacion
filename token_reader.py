import re

# Definición de expresiones regulares para diferentes tokens
tokens = {
    'identificador': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'asignacion': r'=',
    'entero': r'\b\d+\b',
    'flotante': r'\b\d+\.\d+\b',
    'flotante_negativo': r'\b-\d+\.\d+\b',
    'real': r'\b\d+\.\d+E-?\d+\b',
    'multiplicacion': r'\*',
    'resta': r'-',
    'division': r'/',
    'potencia': r'\^',
    'comentario': r'//.*',
    'numero_entero': r'\b[0-9]+\b',
    'correo_electronico': r'\S+@\S+\.\S+',
    'fecha': r'\b\d{2}/\d{2}/\d{4}\b',
    'numero_telefono': r'\+?\d{1,3}-\d{2,4}-\d{6,8}',
}

def tokenize(text):
    token_list = []
    for tk_type, tk_regex in tokens.items():
        for match in re.finditer(tk_regex, text, re.IGNORECASE):
            token_list.append((match.start(), tk_type, match.group()))
    return sorted(token_list, key=lambda x: x[0])

# Leer el archivo de entrada
with open('content.txt', 'r') as file:
    content = file.read()

# Tokenizar el contenido
tokenized_content = tokenize(content)

# Procesar y agrupar los tokens
# Este es un ejemplo básico, necesitarás adaptarlo según tus necesidades
for pos, tk_type, value in tokenized_content:
    print(f"{value}\t{tk_type}")
