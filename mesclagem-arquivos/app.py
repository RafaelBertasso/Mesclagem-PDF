import PyPDF2
import os

# variável para juntar os PDFs
merge = PyPDF2.PdfMerger()

# variável para guardar os arquivos que serão mesclados
lista_arquivos = os.listdir("arquivos")

# colocar os arquivos em ordem
lista_arquivos.sort()

# percorrer a lista de arquivos
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merge.append(f"arquivos/{arquivo}")

# criar o arquivo final com os PDFs mesclados
merge.write("PDF-Final.pdf")