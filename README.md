# notes
Notes and commands reference about everything

# How to mirror a single page
Set a URL:
```
URL="https://www.governotransparente.com.br/acessoinfo/44669490/consultarcontratoaditivo?inicio=01%2F01%2F2021&fim=13%2F10%2F2021&contr=&ano=12&credor=-1&clean=false&datainfo=MTIwMjExMDEzMTExMVBQUA%3D%3D"
```
Using wget:
```
wget -erobots=off --no-parent --wait=3 --limit-rate=20K -r -p -U "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)" -A htm,html,css,js,json,gif,jpeg,jpg,bmp $URL
```
Or using httrack:
```
sudo apt install httrack
httrack $URL -O "./public" $URL -v -s0 --depth=1 -n
```
