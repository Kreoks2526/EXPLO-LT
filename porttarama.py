import scapy.all as scapy
from scapy.layers.inet import IP, TCP

def port_taramasi(hedef_ip, baslangic_port, bitis_port):
    tarama_sonuclari = []
    
    for port in range(baslangic_port, bitis_port + 1):
        # TCP paketi oluştur
        paket = IP(dst=hedef_ip)/TCP(sport=port, dport=port, flags="S")
        
        # Paketi gönder
        cevap = scapy.sr1(paket, verbose=0, timeout=1)
        
        if cevap:
            if cevap.haslayer(TCP) and cevap[TCP].flags == 18:
                tarama_sonuclari.append(f"Port {port} açık")
        else:
            tarama_sonuclari.append(f"Port {port} kapalı")
    
    return tarama_sonuclari

if __name__ == "__main__":
    hedef_ip = input("Enter the IP address you want to scan: ")
    baslangic_port = int(input("Enter the start port: "))
    bitis_port = int(input("Enter the end port: "))
    
    sonuclar = port_taramasi(hedef_ip, baslangic_port, bitis_port)
    
    for sonuc in sonuclar:
        print(sonuc)
