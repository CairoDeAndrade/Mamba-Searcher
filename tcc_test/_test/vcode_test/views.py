from django.shortcuts import render
import docx2txt
import fitz
import unicodedata
import os
from operator import itemgetter


def mamba(request, ):
    # dirPath = r"C:\Users\entra21\Desktop\testes"
    dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes"  # Home
    lista_arquivos = next(os.walk(dirPath))[2]

    lista_quantidade_palavras, texto, lista_final, list_files_name, list_word_qtd, real_final = [], [], [], [], [], []
    total = 0
    caminho = ''
    result, final_dict = [], {}

    palavras_chave = 'python,ingles'
    novas_palavras = ''.join(ch for ch in unicodedata.normalize('NFKD', palavras_chave).lower()
                             if not unicodedata.combining(ch))
    novas_palavras = palavras_chave.split(",")

    for i in lista_arquivos:
        try:
            # caminho = fr"C:\Users\entra21\Desktop\testes\{i}"
            caminho = fr"C:\Users\cairo\OneDrive\Área de Trabalho\testes\{i}" # home
            sum = 0
            texto = docx2txt.process(caminho)
            novo_texto = ''.join(ch for ch in unicodedata.normalize('NFKD', texto).lower()
                                 if not unicodedata.combining(ch))

            total = len(novas_palavras)

            for palavra in novas_palavras:
                if palavra in novo_texto:
                    sum += 1
                else:
                    continue
            lista_quantidade_palavras.append(sum)
        except:
            quantidade = []
            text = ''
            sum = 0
            with fitz.open(caminho) as doc:
                for page in doc:
                    text = page.get_text()
            new_text = ''.join(ch for ch in unicodedata.normalize('NFKD', text).lower()
                               if not unicodedata.combining(ch))

            for j in novas_palavras:
                if j in new_text:
                    sum += 1
                else:
                    continue
            lista_quantidade_palavras.append(sum)

    for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
        final_dict = {'arquivo': arquivo, 'quantidade_palavras': quantidade_palavras, 'total': total}

        quantidade = [arquivo, quantidade_palavras, total]
        lista_final.append(final_dict)
        result = sorted(lista_final, key=itemgetter('quantidade_palavras'), reverse=True)

    for i in result:
        list_files_name.append(i['arquivo'])
        list_word_qtd.append(i['quantidade_palavras'])

    for files_name, word_qtd in zip(list_files_name, list_word_qtd):
        complete_list = [files_name, word_qtd]
        real_final.append(complete_list)

    return render(request, 'vcode_test/mamba.html', {'lista_final': lista_final,
                                                     'novas_palavras': novas_palavras, 'result': result,
                                                     'real_final': real_final, 'total': total,
                                                     })

#
# def index(request):
#     dirPath = r"C:\Users\entra21\Desktop\testes"
#     # dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\testes" # Home
#     lista_arquivos = next(os.walk(dirPath))[2]
#
#     lista_quantidade_palavras, palavras_chave, texto, lista_final = [], [], [], []
#     total = 0
#     quantidade = ''
#
#     for i in lista_arquivos:
#         sum = 0
#         texto = docx2txt.process(fr"C:\Users\entra21\Desktop\testes\{i}").lower()
#
#         # texto = docx2txt.process(fr"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test\{i}").lower()
#         palavras_chave = ['python', 'vitor da silva']
#         total = len(palavras_chave)
#
#         for palavra in palavras_chave:
#             if palavra in texto:
#                 sum += 1
#             else:
#                 continue
#         lista_quantidade_palavras.append(sum)
#
#     for arquivo, quantidade_palavras in zip(lista_arquivos, lista_quantidade_palavras):
#         quantidade = [arquivo, quantidade_palavras, total]
#         lista_final.append(quantidade)
#
#     return render(request, 'vcode_test/index.html', {'lista_final': lista_final,
#                                                      'palavras_chave': palavras_chave, })
