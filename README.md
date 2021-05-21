# whatsauto

Este repositório contém código para automatização de envios de mensagens pelo whatsapp.
É necessário ter os contatos salvos no dispositivo.

## pré-requisitos

python3

selenium

chrome driver

## uso

### Windows

Coloque o executável chromedriver.exe na pasta raiz do repositório, ou seja, junto do arquivo script.py

Crie um arquivo contatos.txt e um arquivo mensagem.txt, na mesma pasta.

O arquivo contatos.txt deve ter um nome de contato por linha, exatamente como está salvo na lista de contatos do
dispositivo.

O arquivo mensagem.txt deve conter a mensagem como seria escrita no whatsapp. O programa insere os caracteres de
formatação, então caso queira colocar algo em negrito, escreva *assim*, caso queiram em itálico, _assim_

Dê duplo-clique no arquivo script.py, leia o código QR do whatsapp web com o dispositivo no qual os contatos estão
salvos, e o programa enviará a mensagem contida no mensagem.txt a todos os contatos possíveis de contatos.txt


### Linux e Mac

```bash
python script.py contatos mensagem
```
O executável chromedriver deve estar configurado no PATH.

O arquivo contatos deve possuir um nome de contato por linha, ou no mínimo parte do nome do contato,
que seja suficiente para identificar unicamente o contato.

O arquivo mensagem deve conter a mensagem a ser enviada aos contatos, que será a mesma para todos.
Ambos os arquivos devem ser salvos com codificação UTF-8.


