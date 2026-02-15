# UI Overhaul Plan - Medium-Style Blog & Polished Portfolio

## Context
Blog ve portfolio sayfaları modernize edilmiş ancak tutarsız bir durumdaydı: blog_home modern gradient banner kullanırken diğer sayfalar eski template stilini kullanıyor. Template'lerde aşırı inline style, hardcoded iletişim bilgileri, kopyala-yapıştır HTML blokları ve eski FA4 ikon syntax'ı mevcut. Bu plan tüm sayfaları tutarlı, Medium kalitesinde bir deneyime taşır.

---

## Phase 0: CSS Design System Foundation

**Yeni dosya:** `static/css/site-modern.css`
- CSS custom properties (design tokens): renkler, gölgeler, border-radius
- Reusable component sınıfları: `.banner-modern`, `.card-hover-lift`, `.btn-gradient`, `.section-heading`, `.timeline-item`, `.nav-link-modern`, `.footer-modern`
- Medium-style article tipografisi: `.article-body` (Georgia/serif, 20px, max-width 680px)
- content_type varyantları: `.article-body--poem` (ortala, italic), `.article-body--tutorial` (sans-serif tut)
- Dark mode `[data-theme="dark"]` karşılıkları

**Düzenle:** `templates/includes/head.html` - yeni CSS dosyasını ekle

---

## Phase 1: Blog Detail - Medium-Like Reading Experience (EN ÖNCELİKLİ)

**Dosyalar:** `templates/blog_detail.html`, `static/css/markdown-styles.css`, `blog/views.py`

### blog_detail.html:
- Banner: Eski `banner_area > box_1620` yerine full-width hero (featured image arka plan veya gradient overlay)
- content_type badge'i göster (Şiir, Tutorial, Makale vb.) - model'de var ama template'de kullanılmıyor
- Tipografi: `article-body` sınıfı ile 680px max-width, Georgia serif font, 20px
- content_type'a göre koşullu stil: `article-body--{{ post.content_type }}`
- FA4 ikonları FA6'ya güncelle (`fa fa-user` → `fa-solid fa-user`)
- Yazar bilgi kartı (makale sonunda)
- Önceki/sonraki yazı navigasyonu
- Sosyal paylaşım butonları (X, LinkedIn, link kopyala)

### markdown-styles.css:
- Font-size: 16px → 20px, line-height: 1.8 → 1.9
- Şiir blockquote stili: dekoratif tırnak işareti, ortalanmış, italic
- Makale drop cap: ilk paragrafın ilk harfi büyük ve renkli
- Dark mode uyumu

### blog/views.py:
- `blog_detail`: Önceki/sonraki post sorguları ekle, context'e ekle

---

## Phase 2: Blog Home - Sayfalama ve Kategori Filtresi

**Dosyalar:** `templates/blog_home.html`, `blog/views.py`

### blog_home.html:
- Banner'dan emoji kaldır (📝)
- For-loop içindeki `<style>` bloğunu site-modern.css'e taşı
- Tüm inline style'ları CSS sınıflarına dönüştür
- content_type badge'i kartlara ekle
- Kategori filtre pilleri ekle (posts grid üstünde)
- Pagination UI ekle (alt kısım)
- Alt kısımdaki `<style>` bloğunu site-modern.css'e taşı

### blog/views.py:
- `blog_home`: `[:10]` slice yerine Django Paginator (sayfa başına 10)
- Kategori filtresi: `?category=slug` query parametresi desteği
- Kategorileri context'e ekle

---

## Phase 3: Index/Resume Page - Temiz ve DRY

**Dosyalar:** `templates/index.html`, `core/views.py`, **yeni:** `templates/includes/skill_section.html`

### index.html:
- Hardcoded iletişim bilgileri → context processor değişkenleri (`{{ contact_email }}` vb.)
- 4x kopyalanmış skill section → `{% include 'includes/skill_section.html' with skills=X title=Y icon=Z %}`
- Tüm inline style'ları CSS sınıflarına taşı
- Alt `<style>` bloğunu site-modern.css'e taşı

### core/views.py (`layout` context processor):
- GeneralSetting'den `contact_email`, `contact_phone`, `contact_location` oku, context'e ekle

### skill_section.html (yeni include):
- Tek bir skill kategorisi için reusable partial template

---

## Phase 4: Diğer Template'ler

### 4A: contact.html
- Eski banner → `.banner-modern`
- Hardcoded bilgiler → context processor değişkenleri
- Linericon ikonları → FA6 (`lnr lnr-home` → `fa-solid fa-location-dot`)
- textarea `rows="1"` → `rows="5"`
- Modern form stili

### 4B: portfolio.html
- Eski banner → `.banner-modern`
- FA4 ikonları → FA6
- `<style>` bloğunu site-modern.css'e taşı
- Kategori filtre butonları → gradient pill stili

### 4C: project_detail.html
- Eski banner → `.banner-modern`
- FA4 ikonları → FA6
- Sidebar kartlarına modern stil

---

## Phase 5: Navbar & Footer

### navbar.html:
- Tüm `onmouseover`/`onmouseout` handler'ları kaldır → CSS `:hover`
- Tüm inline style'ları → `.nav-link-modern`, `.btn-gradient` sınıfları
- Active state logic Django template'de kalsın, styling CSS'e taşınsın

### footer.html:
- Inline style'ları → `.footer-modern` sınıfı
- `onmouseover`/`onmouseout` → CSS `:hover`
- `<script>document.write(new Date().getFullYear())</script>` → `{% now "Y" %}`

---

## Phase 6: CSS & JS Temizliği

- `style.css` (3030 satır): Kullanılmayan selektörleri tespit et, sadece kullanılanları tut
- Linericon CSS referansını head.html'den kaldır (FA6'ya geçildiğinde)
- Kullanılmayan vendor CSS/JS'leri kontrol et
- `custom-override.css` içeriğini site-modern.css'e taşı ve dosyayı sil

---

## Doğrulama

1. Docker ile build & test: `docker compose up --build`
2. Tüm sayfaları tarayıcıda kontrol (/, /blog/, /blog/test-post/, /portfolio/, /contact/)
3. Dark mode toggle test
4. Mobil responsive test (tarayıcı dev tools)
5. Mevcut testleri çalıştır: `docker compose exec app python manage.py test`
6. HTML'de kırık link/ikon kontrolü
7. `collectstatic` çalıştır (ManifestStaticFilesStorage hash güncellemesi)

---

## Kritik Dosya Listesi

| Dosya | Değişiklik Tipi |
|-------|----------------|
| `static/css/site-modern.css` | YENİ - Design system |
| `static/css/markdown-styles.css` | DÜZENLE - Tipografi iyileştirme |
| `templates/blog_detail.html` | DÜZENLE - Tam yeniden yazım |
| `templates/blog_home.html` | DÜZENLE - Pagination, inline CSS temizliği |
| `templates/index.html` | DÜZENLE - DRY, inline CSS temizliği |
| `templates/contact.html` | DÜZENLE - Modernize |
| `templates/portfolio.html` | DÜZENLE - Banner, ikonlar |
| `templates/project_detail.html` | DÜZENLE - Banner, ikonlar |
| `templates/includes/navbar.html` | DÜZENLE - CSS'e taşı |
| `templates/includes/footer.html` | DÜZENLE - CSS'e taşı |
| `templates/includes/head.html` | DÜZENLE - Yeni CSS ekle |
| `templates/includes/skill_section.html` | YENİ - Reusable partial |
| `blog/views.py` | DÜZENLE - Pagination, prev/next |
| `core/views.py` | DÜZENLE - İletişim bilgileri context |
| `static/css/custom-override.css` | SİL (site-modern.css'e taşı) |
| `static/css/style.css` | DÜZENLE - Kullanılmayanları temizle |
