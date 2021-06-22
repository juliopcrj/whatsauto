# WhatsAuto

WhatsAuto é um script para automatizar o envio de mensagens através da plataforma web do WhatsApp.
Para utilizar, é necessário instalar alguns pré-requisitos no seu computador.
As instruções a seguir são para instalar os pré-requisitos em sistemas Windows.

## Python3
Para instalar o python3, você pode fazer o download do instalador [aqui](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe)
Abra o instalador, marque a caixa de "Adicionar Python3 ao PATH", e prossiga normalmente com a instalação.
Após instalar o python3, é necessário instalar a biblioteca selenium.

## Selenium
Para instalar o selenium, você deverá abrir o prompt de comando, ou o PowerShell.
Isso pode ser feito abrindo o menu iniciar e digitando "PowerShell" (sem aspas).
Com o powershell(ou cmd) aberto, digite
```
pip install selenium
```
e pressione enter. O gerenciador de pacotes do Python vai fazer a instalação do pip.

## Chrome Driver
O whatsauto funciona com o navegador Google Chrome. Se você não possui esse navegador instalado, clique [aqui](https://www.google.com/chrome/) para acessar a página de download do mesmo.
Com o navegador aberto, navegue até a página chrome://version, e procure a versão, na primeira linha.
A versão é o número que aparece logo após "Google Chrome:".
[Nessa página](https://chromedriver.chromium.org/downloads) você pode encontrar links para as versões mais recentes do Chrome Driver.
Selecione a versão correspondente à versão do seu navegador, e faça o download do arquivo chromedriver\_win32.zip .
A versão 32bits é compatível com o sistema de 64bits.
Descompacte o chromedriver, e coloque o executável chromedriver.exe na mesma pasta do script.py .

O seu dispositivo agora está pronto para utilizar o whatsauto.

## uso

Na pasta do script.py e chromedriver.exe, crie um arquivo chamado contatos.txt.
Esse arquivo deve ser preenchido com os nomes dos contatos, exatamente como constam no whatsapp do seu celular, um por linha.

Nessa mesma pasta, crie um arquivo camado mensagem.txt. Esse arquivo vai conter a mensagem que será enviada a todos os contatos indicados em contatos.txt.
A mensagem pode conter caracteres de formatação de texto do whatsapp, como \*negrito\* ou \_itálico\_.

Após ter os dois arquivos preparados, dê duplo-clique no arquivo script.py. Uma janela do chrome será aberta, na página do whatsapp web. A partir desse momento, você terá 25 segundos para fazer a leitura do código QR com o mesmo celular onde os contatos estão salvos.
Se a leitura for feita dentro do tempo, aguarde, e o programa começará a enviar as mensagens.

## Logs

Durante a execução, o programa salva registros de envios de mensagens no arquivo log\_day.txt, e registros de erros de envio em log\_error.txt
Ambos os arquivos possuem timestamp em todos os registros.

### IMPORTANTE
O whatsauto utiliza o whatsapp web para fazer o envio das mensagens, então não é possível ter os contatos salvos em um celular e enviar com outro. O celular com os contatos salvos deverá ser usado para isso.

