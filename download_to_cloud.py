# Proposta para realizar download automático de arquivos de um site e fazer upload no google cloud.
# Link de acesso aos dados de exemplo: http://ftp.dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios/

# Libraries
import requests
import os
from google.cloud import storage

### Função para download
def download_archives(url, adress):
    adress = os.path.basename(url.split("?")[0])   
    resp = requests.get(url, stream=True)
    with open(adress, 'wb') as new_arc:
        for p in resp.iter_content(chunk_size=256):
            new_arc.write(p)

# Execução do download
filelist = []
if __name__ == "__main__":
    test_url = 'http://ftp.dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios/202112/ben202112_{}.zip'
    uf_list = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO','XX']
    for i in uf_list:
        nome_arquivo = os.path.join(f'ben202112_{i}.zip')
        download_archives(test_url.format(i), nome_arquivo)
        filelist.append(nome_arquivo)

# Check dos nomes para iterar depois
filelist

# Lendo credenciais do gcloud - Você precisa criar sua própria credencial e bucket.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'yourcredential.json'
storage_client = storage.Client()

# Acessando meu bucket
bucket_name = 'sunagatest'
my_bucket = storage_client.get_bucket(bucket_name)


### Função de upload
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except:
        return False

      
# Execução do upload
file_path = os.getcwd()
for name in filelist:
    upload_to_bucket(name, os.path.join(file_path, name),'sunagatest')
