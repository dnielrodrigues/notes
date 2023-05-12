# Diretórios do Linux

```
/ ____________ raiz  
/bin/ ________ binários principais do usuário  
/boot/ _______ arquivos do sistema de boot  
/dev/ ________ arquivos de dispositivos  
/etc/ ________ arquivos de configuração do sistema  
/home/ _______ diretórios dos usuários comuns do sistema  
/lib/ ________ bibliotecas essenciais do sistema e os módulos do kernel  
/media/ ______ montagem de dispositivos  
/mnt/ ________ montagem de dispositivos (mesmo que media)  
/opt/ ________ instalação de programas não oficiais da distribuição ou por conta do usuário  
/sbin/ _______ arquivos executaveis q representam comandos administrativos. ex: shutdown  
/srv/ ________ diretório para dados de serviços fornecidos pelo sistema  
/tmp/ ________ diretório para arquivos temporários  
/usr/ ________ segunda hierarquia do sistema, onde ficam os usuários comuns do sistema e programas  
/var/ ________ arquivos variaveis gerados pelos programas do sistema. ex: logs, spool, emails e cache  
/root/  ______ do usuário root  
/proc/ _______ diretório virtual controlado pelo kernel com configuração total do sistema  
```

# Geral/Úteis

Processo em segundo plano:
`bash /caminho/do/script.sh > /caminho/do/log.txt 2>&1`  
`bash /caminho/do/script.sh > /dev/null 2>&1`  

ZIP & TAR
`zip -r archive_name.zip _folder_to_compress_`  
`unzip _archive_name_.zip`  
`sudo tar -xzvf _file_.tar.gz -C /_path_/_to_/`  

Mover imagens de pastas e sub-pastas para um local único:  
`find */ -type f -name *.jpg -exec mv {} /path/to/put \;`  

Detalhes da memória RAM:  
`sudo dmidecode --type 17`  

Criar link simbólico:  
`sudo ln -s _from_/ _to_`  

Adicionar usuário atual ao grupo:  
`sudo adduser $USER _group_`  

Criar Ícone para aplicativo:  
Inserir no arquivo `~/.local/share/applications/_titulo_.desktop` ou `/usr/share/applications/_titulo_.desktop` :

```
[Desktop Entry]
Version=1.0
Type=Application
Name=Android Studio
Exec="/opt/android-studio/bin/studio.sh" %f
Icon=/opt/android-studio/bin/studio.png
Categories=Development;IDE;
Terminal=false
StartupNotify=true
StartupWMClass=jetbrains-android-studio
Name[en_GB]=android-studio.desktop
```  

## CURL
-i: detalhar o header  
-d: enviar dados no request. Ex: ` ... `   
-X: Declarar o método. Ex: `curl -X PUT http://localhost:3000`  
-T: Upload de arquivo  
-u: autenticação. Ex: `curl -u usuario:senha http://localhost:3000`  
-o: salvar resultado me arquivo. Ex: `curl -o meu.txt http://localhost:3000`  

## MarkDown online editor
[https://pandao.github.io/editor.md/](https://pandao.github.io/editor.md/ "https://pandao.github.io/editor.md/")

## Ubuntu Após Instalação
```
sudo apt install git zip vi
sudo apt install snapd snapd-xdg-open
snap install postman
```
