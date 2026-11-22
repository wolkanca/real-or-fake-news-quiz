# 🗞️ Gerçek Haber mi, Uydurma mı? — Wolkanca Oyunları #04

Wolkanca mini oyun serisinin dördüncü oyunu: **gerçekten yaşanmış şaşırtıcı haberler** ile **bu oyun için yazılmış kurgu haber başlıklarını** birbirinden ayır. Mobil öncelikli, tek sayfa HTML/CSS/JS, ücretsiz ve WordPress iframe uyumlu.

## Özellikler

- **24 haberlik havuz**: 12 kaynaklı gerçek olay + 12 özellikle oyun için üretilmiş kurgu.
- **10 soruluk turlar**: her tur tam 5 gerçek, 5 kurgu. Sorular her tur yeniden karıştırılır.
- Doğru cevap +100 puan, art arda doğru cevapta +20, +40, +60, +80’e kadar **seri bonusu**.
- İsteğe bağlı **18 saniyelik süreli mod**; süre dolarsa yanlış sayılır.
- Cevaptan sonra açıklama. Gerçek olaylarda **kaynağa git** bağlantısı; kurgu olanlarda açıkça **oyun için yazılmıştır** uyarısı.
- `localStorage` üzerinde kişisel rekor, tur sonu skor ekranı, sosyal paylaşım veya panoya kopyalama.
- Klavye: `1` = Gerçek, `2` = Uydurma.
- Harici CDN, backend, API anahtarı veya görsel kütüphanesi gerekmez.

## Başlat

`index.html` dosyasını tarayıcıda aç; tamamı tek dosyadadır. Ya da yerel sunucuda çalıştır:

```sh
python3 -m http.server 8000
```

Tarayıcıda `http://localhost:8000/` adresini aç.

## GitHub Pages

GitHub deposu: **[`wolkanca/real-or-fake-news-quiz`](https://github.com/wolkanca/real-or-fake-news-quiz)**.

1. Bu depoda oyun dosyalarının `main` dalında bulunduğunu kontrol et.
2. `Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save`.
3. Dağıtım tamamlandığında beklenen adres: `https://wolkanca.github.io/real-or-fake-news-quiz/`.
4. WordPress’te yazıya `wordpress-embed.html` içeriğini **Özel HTML** bloğuyla yerleştir. WordPress `<script>` bölümünü kaldırırsa yalnız iframe de sabit yükseklikte çalışır.

**SEO notu:** Oyunun kendisinde `noindex,follow` bulunur. Arama motorunda hedeflenen açılış sayfası Wolkanca.com’daki blog yazısıdır. GitHub Pages sürümünü ayrıca indeksletmek istersen metayı kaldır.

## Kaynak dosyalar

| Dosya | Açıklama |
|---|---|
| `index.html` | Yayına hazır tüm oyunu barındıran tek HTML |
| `news.json` | 24 haberin doğruluk türü, açıklaması ve kaynak bağlantıları |
| `index.template.html` | HTML/CSS/JS şablonu |
| `build.py` | `news.json` + şablon → `index.html` |
| `wordpress-embed.html` | iframe gömme + güvenli köken kontrolüyle otomatik yükseklik |

Yeni haber eklemek için `news.json` dosyasını düzenle ve `python3 build.py` komutunu çalıştır. Veri dosyasını düzenledikten sonra `python3 build.py` çalıştırman yeterlidir.

## Gerçekler, kurgu ve teyit

**Gerçek haber etiketleri**, güvenilir dış kaynaklarda belgelenmiş tarihî olaylara dayanır. `news.json` içinde gerçek kayıtların her biri için tam kaynak bağlantısı bulunur. Bu oyun, gerçek haberlerin tamamının bugün yaşandığı iddiasında değildir.

**Uydurma haberler**, belirli kayıtları yanlışlamak veya gerçek bir kişinin ya da kurumun itibarını zedelemek amacıyla yazılmamıştır. Eğlenceli bir ayırt etme testi için oluşturulmuş **özgün kurgu manşetlerdir**. Dünya üzerinde benzer bir olayın asla yaşanmadığına ilişkin kapsamlı bir iddiada bulunulmaz. Gerçek haberde de kurgu haberde de başlığın tek başına kanıt olmadığını unutma.

Gerçek haberlerde kaynak olarak NASA, Parks Australia, Google’ın resmî blogu, Guinness World Records, ABC News ve Oregon Encyclopedia kullanılmıştır. Doğrudan bağlantılar aşağıdadır.

## Yerel test

`index.html` dosyasını tarayıcıda açıp 10 soruluk bir tur tamamlayarak cevapları, zamanlayıcıyı, kaynak bağlantılarını ve sonuç ekranını test edebilirsin. İlk sürüm mobil ve masaüstü tarayıcı akışlarında sınanmıştır.

## Lisans

Bu oyun içindeki başlıklar ve açıklamalar birer özet veya özgün kurgudur. Kaynak sitelerin özgün haber metinleri ya da görselleri kopyalanmamıştır. Farklı kaynaklarla veya yeni haberlerle genişletmeden önce özgün kaynakların doğruluğunu tekrar denetle.