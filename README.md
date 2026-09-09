# ASANSÖR SESSİZLİK PROTOKOLÜ

## Resmî İlan

Bu yazılım, asansör kabininde söz söyleme hakkını geçici olarak askıya alan, bilimsel temeli şüpheli fakat töreni çok ciddi bir **Sessizlik Protokolü** üretir.

1923 Asansör İçtihadı'na göre:

> Kabin hareket ettiği anda ağızlar mühürlenir, bakışlar kapının üstündeki rakamlara sabitlenir, hava durumu konuşulmaz.

Bu proje o içtihadın 21. yüzyıl Python uygulamasıdır. Çalışır. Gerçekten çalışır. Yasal olarak kimseyi bağlamaz. Duygusal olarak herkesi bağlar.

## Kurulum

```bash
python3 protokol.py
```

Bağımlılık yoktur. Standart kütüphane yeter. Asansör de yeter.

## Kullanım

Program sizden şunları sorar:

1. Kaç kişi binsiniz?
2. Kaçıncı kattan kaçıncı kata?
3. Kabinde hava durumu lafı geçti mi?

Sonra size:

- protokol numarası
- ihlal cezaları (hayalî)
- sessizlik süresi (saniye cinsinden, fizik kurallarına kısmen sadık)
- resmi bir sözleşme metni

basar.

## Bilimsel Yöntem

Sessizlik süresi şu formülle hesaplanır:

`saniye = abs(hedef - baslangic) * 3.7 + yolcu * 1.1 + (hava_durumu ? 12 : 0)`

3.7 katsayısı, 2011'de bir merdiven boşluğunda hissedilen utancın ortalama süresidir. Hakem heyeti itiraz kabul etmez.

## Sık Sorulan Sorular

**Bu mahkeme kararı mı?**  
Hayır. Daha ağır. Mahkeme kararı temyiz edilir. Utanç temyiz edilmez.

**Konuşursam ne olur?**  
Program bir ihlal kaydı basar. Gerçek hayatta komşunuz size bakar. İkisi de yeter.

**Neden Türkçe?**  
Çünkü asansörde susmak evrenseldir ama protokol yerlidir.

## Lisans

Sessizlik Lisansı v1. Kabinde yüksek sesle okunması yasaktır.

---

```
⚑ DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
TentiAŞ resmi olmayan mührü
9 Eylül 2026 · Eskişehir
Ciddiyet: yüksek
Ciddiyetsizlik: eşit derecede yüksek
Bu imza hem şaka hem kayıttır.
```
