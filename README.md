# whatsauto

Este repositório contém código para automatização de envios de mensagens pelo whatsapp.
É necessário ter os contatos salvos no dispositivo.

## pré-requisitos

python3

selenium

chrome driver

## uso

```bash
python script.py contatos mensagem
```

O arquivo contatos deve possuir um nome de contato por linha, ou no mínimo parte do nome do contato,
que seja suficiente para identificar unicamente o contato.


O arquivo mensagem deve conter a mensagem a ser enviada aos contatos, que será a mesma para todos.
Ambos os arquivos devem ser salvos com codificação UTF-8.


