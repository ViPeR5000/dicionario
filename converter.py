#!/usr/bin/env python3
import unicodedata

# Vamos primeiro verificar a codificação do arquivo 'pt_pt.dic'
import chardet

ENTRADA = 'pt_pt.dic'

SAIDA = 'palavras.txt'

# Detectar a codificação do arquivo
with open(ENTRADA, 'rb') as file:
    raw_data = file.read()
    encoding_result = chardet.detect(raw_data)

encoding_result


def normalizar(txt):
    """Remove acentos e transforma em minúsculas."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', txt).lower()
        if not unicodedata.combining(c)
    )

def chave(txt):
    """Manter palavras acentuadas após as não acentuadas"""
    return (normalizar(txt), tuple(ord(c) for c in txt))

palavras = set()
with open(ENTRADA, encoding='utf-8') as entrada:
    next(entrada)  # Saltar a primeira linha
    for linha in entrada:
        palavra_base = linha.strip().split('/')[0]
        partes = palavra_base.split('-')
        sufixo = partes[-1]
        if len(sufixo) != 2 or sufixo.upper() != sufixo:
            palavras.update(parte for parte in partes if parte)

qt_original = sum(1 for _ in open(ENTRADA, encoding='utf-8')) - 1  # Conta as linhas excluindo a primeira
extra = len(palavras) - qt_original
print(f'{qt_original} palavras na lista original, {len(palavras)} na lista gerada: {extra} adicionadas')

palavras = sorted(palavras, key=chave)

with open(SAIDA, 'wt', encoding='utf-8') as saida:
    saida.write('\n'.join(palavras))
    saida.write('\n')
