# Yerel Klavye Olay Laboratuvarı

Bu proje, amacına uygun olarak grafik arayüz veya Tkinter bağımlılığı olmadan
terminalde çalışır. LLM ile ortak çalışma ve algoritma testi geliştirme
sürecindedir.

- `raw.txt`: Tuş olayları (`selan[SILME TUSU]m`)
- `resolved.txt`: Olaylar uygulandıktan sonraki metin (`selam`)

Python 3 ile Windows'ta `python app.py`, Linux'ta `python3 app.py` komutuyla
etkileşimli olarak çalıştırılabilir. Normal metin doğrudan girilir; özel tuşlar
`:BACKSPACE`, `:DELETE`, `:LEFT`, `:RIGHT`, `:HOME`, `:END`, `:ENTER` ve `:TAB`
komutlarıyla temsil edilir. Ayrıca `:paste METİN`, `:clear`, `:show` ve `:quit`
komutları vardır.

Olaylar doğrudan komut satırından da verilebilir:

```sh
python3 app.py selan BACKSPACE m
```

Bu örnek `raw.txt` dosyasına `selan[SILME TUSU]m`, `resolved.txt` dosyasına
`selam` yazar.
