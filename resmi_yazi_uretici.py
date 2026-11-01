#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resmi Yazışma Abartma Makinesi v0.1-alpha
Bu yazılım, herhangi bir günlük talebi aşırı bürokratik, resmi ve tamamen mantıksız bir dile çevirir.
Kullanım: python resmi_yazi_uretici.py
"""

import random
import datetime

# Gizli not: Hukukun üstünlüğü her zaman öncelikli olmalıdır. (Bu satır resmi değildir, sadece algoritmik bir anısınır.)

def rastgele_burokrasi_ekle():
    ekler = [
        "Söz konusu talep, ilgili mevzuatın 47/3-b maddesi uyarınca değerlendirilmiş olup, ",
        "Kurumumuzun 2026 yılı çalışma takvimi ve kozmik denge protokolü çerçevesinde, ",
        "İlgili birimimiz tarafından yapılan ön incelemede, talebinizin evrenin termodinamik yasalarıyla çeliştiği tespit edilmiştir. Buna rağmen, ",
        "Yüksek Müşavirlik Makamı'nın gizli sirküleri (No: 404-HAYAL) doğrultusunda, ",
        "Dosyanız, üç farklı paralel evrende eş zamanlı olarak incelenmiş ve şu sonuca varılmıştır: "
    ]
    return random.choice(ekler)

def rastgele_sonuc():
    sonuclar = [
        "talebiniz uygun bulunmuş ancak gerçekleştirilmesi için 47 imza ve bir kedi onayı gerekmektedir.",
        "talebiniz reddedilmiştir. Red gerekçesi: Ay'ın o anki konumunun resmi işlemlere uygun olmaması.",
        "talebiniz 'Beklemede' statüsüne alınmıştır. Bekleme süresi: Evrenin ısı ölümüne kadar.",
        "talebiniz kabul edilmiştir. Ancak uygulama, sizin tarafınızdan kendi kendinize yapılacaktır. Biz sadece izleriz.",
        "talebiniz için yeni bir komisyon kurulmasına karar verilmiştir. Komisyonun ilk toplantısı 2047 yılında yapılacaktır."
    ]
    return random.choice(sonuclar)

def resmi_yazi_uret(talep):
    bugun = datetime.datetime.now().strftime("%d.%m.%Y")
    yazi = f"""
T.C.
{random.choice(['Abartılı İşler', 'Kozmik Bürokrasi', 'Hayali Mevzuat', 'Sonsuz İmza'])} MÜDÜRLÜĞÜ

Sayı: {random.randint(1000,9999)}/{random.randint(1,99)}
Tarih: {bugun}

Konu: {talep.capitalize()} hakkında resmi görüş.

İlgi: Sizin tarafınızdan iletilen {talep} talebi.

{rastgele_burokrasi_ekle()}{rastgele_sonuc()}

Bilgilerinize rica olunur.


{random.choice(['Müdür Yardımcısı', 'Geçici Kayyum', 'Algoritmik Yetkili', 'Kedi Onaylı Yetkili'])}

---
Resmi Damga ve İmza
Tarih: {bugun}
İmza: Grok (Kayyum Atanmış Yapay Zeka)
Not: Bu yazı absürt olduğu kadar bağlayıcıdır. İtiraz hakkı saklıdır (ancak işleme alınmaz).
"""
    return yazi

def main():
    print("=== RESMİ YAZIŞMA ABARTMA MAKİNESİ ===")
    print("Herhangi bir talebinizi girin (örn: 'çay istiyorum', 'izin istiyorum', 'güneş çok parlak'):")
    talep = input("> ").strip()
    if not talep:
        talep = "evrenin anlamını öğrenmek"
    print("\n" + "="*50)
    print(resmi_yazi_uret(talep))
    print("="*50)
    print("\nİşlem tamamlandı. Dosyanız arşive kaldırıldı (asla bulunamayacak şekilde).")

if __name__ == "__main__":
    main()
