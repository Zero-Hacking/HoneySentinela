# HoneySentinela
HoneyPot simples pra intrusão de rede agressivo!!

Copie seu código honeypot para uma pasta no sistema.
Certifique-se de que os arquivos sentinela.py e requirements.txt (dependências) estão no mesmo diretório.
Instale todas as bibliotecas necessárias listadas no requirements.txt
pip install -r requirements.txt

Execute o Honeypot.
Inicie o honeypot com o seguinte comando:
python3 sentinela.py

Solução de Problemas!!
Erro de Permissão para logs.txt:
Certifique-se de que o diretório atual possui permissões de escrita:
chmod +w logs.txt
Ou especifique um caminho alternativo para salvar o arquivo, como /tmp/logs.txt.

Erro ModuleNotFoundError (Scapy)
Caso a biblioteca Scapy não tenha sido instalada, instale-a separadamente:
pip install scapy

Para encerrar o honeypot, pressione Ctrl+C no terminal

