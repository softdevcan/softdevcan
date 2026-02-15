# Template Variables Reference

Bu dosya, Django template sisteminde kullanılan tüm değişkenleri, kaynaklarını ve veri tiplerini listeler.

---

## 1. Global Context (Layout Context Processor)

**Kaynak:** `core/views.py:layout()` — Tüm template'lerde otomatik olarak mevcuttur.
**Cache:** Redis, 1 saat (`layout_context` key). Signal ile invalidate edilir.

### 1.1 GeneralSetting Değişkenleri

Admin panelinde `GeneralSetting` modeli üzerinden yönetilir. Her biri `name` → `parameter` eşlemesidir.

| Değişken | Admin Name | Tip | Açıklama | Örnek Değer |
|----------|-----------|-----|----------|-------------|
| `{{ site_title }}` | `site_title` | `str` (max 1024) | Sitenin `<title>` etiketi | `Can Akyıldırım` |
| `{{ site_keywords }}` | `site_keywords` | `str` (max 1024) | `<meta name="keywords">` içeriği | `python, django, developer` |
| `{{ site_description }}` | `site_description` | `str` (max 1024) | `<meta name="description">` içeriği | `Software Developer Portfolio` |
| `{{ home_banner_name }}` | `home_banner_name` | `str` (max 1024) | Ana sayfa hero bölümündeki isim | `Can Akyıldırım` |
| `{{ home_banner_title }}` | `home_banner_title` | `str` (max 1024) | Ana sayfa hero bölümündeki unvan | `Software Developer` |
| `{{ home_banner_description }}` | `home_banner_description` | `str` (max 1024) | Ana sayfa hero bölümündeki açıklama metni | `I build modern web applications...` |
| `{{ about_myself_welcome }}` | `about_myself_welcome` | `str` (max 1024) | Ana sayfa "About" bölümü metni | `Welcome to my portfolio...` |
| `{{ about_myself_footer }}` | `about_myself_footer` | `str` (max 1024) | Footer ve blog yazar kartı açıklama metni | `Full-stack developer based in...` |
| `{{ contact_email }}` | `contact_email` | `str` (max 1024) | İletişim e-posta adresi | `akyildirimcan@gmail.com` |
| `{{ contact_phone }}` | `contact_phone` | `str` (max 1024) | İletişim telefon numarası | `+90 (552) 256 14 05` |
| `{{ contact_location }}` | `contact_location` | `str` (max 1024) | İletişim konum bilgisi | `Eskişehir, Turkey` |

### 1.2 ImageSetting Değişkenleri

Admin panelinde `ImageSetting` modeli üzerinden yönetilir. Her biri `name` → `file` (ImageField) eşlemesidir.

| Değişken | Admin Name | Tip | Açıklama | Kullanım |
|----------|-----------|-----|----------|----------|
| `{{ header_logo.url }}` | `header_logo` | `ImageField` | Navbar'daki site logosu | `navbar.html` |
| `{{ home_banner_image.url }}` | `home_banner_image` | `ImageField` | Ana sayfa hero arka plan resmi | `index.html` |
| `{{ site_favicon.url }}` | `site_favicon` | `ImageField` | Tarayıcı sekme ikonu (favicon) | `head.html` |

### 1.3 QuerySet Değişkenleri

| Değişken | Tip | Açıklama | Kullanım |
|----------|-----|----------|----------|
| `{{ documents }}` | `list[Document]` | Navbar'daki indirilebilir dosyalar (CV vb.) | `navbar.html` |
| `{{ social_medias }}` | `list[SocialMedia]` | Footer sosyal medya linkleri | `footer.html` |

---

## 2. Sayfa Bazlı Context Değişkenleri

### 2.1 Index / Ana Sayfa (`core/views.py:index`)

**Template:** `index.html` | **URL:** `/` | **Cache:** 15 dk

| Değişken | Tip | Açıklama |
|----------|-----|----------|
| `{{ backend_skills }}` | `QuerySet[Skill]` | Backend yetenekleri (`skill_type='backend'`) |
| `{{ frontend_skills }}` | `QuerySet[Skill]` | Frontend yetenekleri (`skill_type='frontend'`) |
| `{{ devops_skills }}` | `QuerySet[Skill]` | DevOps yetenekleri (`skill_type='devops'`) |
| `{{ other_skills }}` | `QuerySet[Skill]` | Diğer yetenekler (`skill_type='other'`) |
| `{{ experiences }}` | `QuerySet[Experience]` | İş deneyimleri (tarihe göre azalan) |
| `{{ educations }}` | `QuerySet[Education]` | Eğitim bilgileri (tarihe göre azalan) |

### 2.2 Blog Listesi (`blog/views.py:blog_home`)

**Template:** `blog_home.html` | **URL:** `/blog/`

| Değişken | Tip | Açıklama |
|----------|-----|----------|
| `{{ posts }}` | `Page[Post]` | Sayfalanmış blog yazıları (sayfa başına 10) |
| `{{ page_obj }}` | `Page[Post]` | Pagination objesi (aynı `posts`) |
| `{{ search_query }}` | `str` | Arama terimi (`?q=...`) |
| `{{ categories }}` | `QuerySet[Category]` | Tüm blog kategorileri |
| `{{ active_category }}` | `Category \| None` | Seçili filtre kategorisi (`?category=slug`) |

### 2.3 Blog Detay (`blog/views.py:blog_detail`)

**Template:** `blog_detail.html` | **URL:** `/blog/<slug>/`

| Değişken | Tip | Açıklama |
|----------|-----|----------|
| `{{ post }}` | `Post` | Blog yazısı objesi |
| `{{ previous_post }}` | `Post \| None` | Önceki yazı (sadece `title`, `slug`) |
| `{{ next_post }}` | `Post \| None` | Sonraki yazı (sadece `title`, `slug`) |

### 2.4 Portfolio (`core/views.py:portfolio`)

**Template:** `portfolio.html` | **URL:** `/portfolio/` | **Cache:** 15 dk

| Değişken | Tip | Açıklama |
|----------|-----|----------|
| `{{ featured_projects }}` | `QuerySet[Project]` | Öne çıkan projeler (`is_featured=True`) |
| `{{ projects }}` | `QuerySet[Project]` | Diğer projeler (`is_featured=False`) |
| `{{ categories }}` | `QuerySet[ProjectCategory]` | Proje kategorileri |
| `{{ active_category }}` | `ProjectCategory \| None` | Seçili filtre kategorisi |

### 2.5 Proje Detay (`core/views.py:project_detail`)

**Template:** `project_detail.html` | **URL:** `/portfolio/<slug>/`

| Değişken | Tip | Açıklama |
|----------|-----|----------|
| `{{ project }}` | `Project` | Proje objesi |
| `{{ related_projects }}` | `QuerySet[Project]` | Aynı kategoriden projeler (max 3) |

### 2.6 İletişim (`contact/views.py:contact`)

**Template:** `contact.html` | **URL:** `/contact/`

| Değişken | Tip | Açıklama |
|----------|-----|----------|
| `{{ contact_form }}` | `ContactForm` | Django form objesi (name, email, subject, message) |

---

## 3. Model Alan Detayları

### 3.1 Skill

| Alan | Tip | Açıklama |
|------|-----|----------|
| `skill.name` | `CharField(254)` | Yetenek adı (ör: Python, Django) |
| `skill.percentage` | `IntegerField(0-100)` | Yeterlilik yüzdesi |
| `skill.skill_type` | `CharField` | Kategori: `backend`, `frontend`, `devops`, `other` |
| `skill.order` | `IntegerField` | Sıralama |
| `skill.get_icon()` | `method → str` | Devicon/FA6 HTML ikonu döndürür |

### 3.2 Experience

| Alan | Tip | Açıklama |
|------|-----|----------|
| `exp.company_name` | `CharField(254)` | Şirket adı |
| `exp.job_title` | `CharField(254)` | Pozisyon |
| `exp.job_location` | `CharField(254)` | Konum |
| `exp.start_date` | `DateField` | Başlangıç tarihi |
| `exp.end_date` | `DateField \| None` | Bitiş tarihi (None = devam ediyor) |

### 3.3 Education

| Alan | Tip | Açıklama |
|------|-----|----------|
| `edu.school_name` | `CharField(254)` | Okul adı |
| `edu.major` | `CharField(254)` | Bölüm / Ana dal |
| `edu.department` | `CharField(254)` | Departman |
| `edu.start_date` | `DateField` | Başlangıç tarihi |
| `edu.end_date` | `DateField \| None` | Bitiş tarihi (None = devam ediyor) |

### 3.4 Post (Blog)

| Alan | Tip | Açıklama |
|------|-----|----------|
| `post.title` | `CharField(200)` | Başlık |
| `post.slug` | `SlugField(250)` | URL slug (otomatik üretilir) |
| `post.excerpt` | `TextField(500)` | Kısa özet (otomatik üretilir) |
| `post.content` | `TextField` | İçerik (Markdown) |
| `post.image` | `ImageField` | Öne çıkan görsel |
| `post.category` | `FK → Category` | Kategori |
| `post.tags` | `M2M → Tag` | Etiketler |
| `post.author` | `FK → User` | Yazar |
| `post.content_type` | `CharField` | `article`, `poem`, `tutorial`, `news`, `other` |
| `post.status` | `CharField` | `draft`, `published` |
| `post.published_date` | `DateTimeField` | Yayın tarihi |
| `post.meta_description` | `CharField(160)` | SEO açıklama |
| `post.meta_keywords` | `CharField(255)` | SEO anahtar kelimeler |
| `post.view_count` | `PositiveIntegerField` | Görüntülenme sayısı |
| `post.reading_time` | `property → int` | Tahmini okuma süresi (dk) |
| `post.get_absolute_url()` | `method → str` | `/blog/<slug>/` |

### 3.5 Category (Blog)

| Alan | Tip | Açıklama |
|------|-----|----------|
| `cat.name` | `CharField(100)` | Kategori adı |
| `cat.slug` | `SlugField(100)` | URL slug |
| `cat.description` | `TextField` | Açıklama |

### 3.6 Tag (Blog)

| Alan | Tip | Açıklama |
|------|-----|----------|
| `tag.name` | `CharField(50)` | Etiket adı |
| `tag.slug` | `SlugField(50)` | URL slug |

### 3.7 Project

| Alan | Tip | Açıklama |
|------|-----|----------|
| `project.title` | `CharField(200)` | Proje başlığı |
| `project.slug` | `SlugField(200)` | URL slug |
| `project.description` | `TextField` | Kısa açıklama |
| `project.content` | `TextField` | Detaylı içerik (Markdown) |
| `project.featured_image` | `ImageField` | Öne çıkan görsel |
| `project.category` | `FK → ProjectCategory` | Kategori |
| `project.github_url` | `URLField` | GitHub linki |
| `project.live_url` | `URLField` | Canlı demo linki |
| `project.technologies` | `CharField(500)` | Virgülle ayrılmış teknolojiler |
| `project.is_featured` | `BooleanField` | Öne çıkan proje mi? |
| `project.is_published` | `BooleanField` | Yayında mı? |
| `project.order` | `IntegerField` | Sıralama |
| `project.get_technologies_list()` | `method → list[str]` | Teknoloji listesi |

### 3.8 ProjectCategory

| Alan | Tip | Açıklama |
|------|-----|----------|
| `pcat.name` | `CharField(100)` | Kategori adı |
| `pcat.slug` | `SlugField(100)` | URL slug |
| `pcat.order` | `IntegerField` | Sıralama |

### 3.9 SocialMedia

| Alan | Tip | Açıklama |
|------|-----|----------|
| `sm.platform` | `CharField(50)` | Platform: `github`, `linkedin`, `twitter`, vb. |
| `sm.link` | `URLField(254)` | Profil URL'si |
| `sm.icon` | `CharField(254)` | Özel ikon HTML (boşsa platform varsayılanı) |
| `sm.order` | `IntegerField` | Sıralama |
| `sm.get_icon()` | `method → str` | FA6 ikon HTML'i döndürür |
| `sm.get_platform_display()` | `method → str` | Platform görüntü adı (ör: "GitHub") |

### 3.10 Document

| Alan | Tip | Açıklama |
|------|-----|----------|
| `doc.slug` | `SlugField(254)` | URL slug (redirect için) |
| `doc.button_text` | `CharField(254)` | Navbar'daki buton metni (ör: "CV") |
| `doc.file` | `FileField` | Yüklenmiş dosya |
| `doc.order` | `IntegerField` | Sıralama |

### 3.11 Message (Contact)

| Alan | Tip | Açıklama |
|------|-----|----------|
| `msg.name` | `CharField(254)` | Gönderen adı |
| `msg.email` | `EmailField(254)` | Gönderen e-posta |
| `msg.subject` | `CharField(254)` | Konu |
| `msg.message` | `TextField` | Mesaj içeriği |

---

## 4. Admin'de Oluşturulması Gereken Kayıtlar

### GeneralSetting (11 kayıt)

| # | Name (tam olarak bu şekilde) | Değer |
|---|------------------------------|-------|
| 1 | `site_title` | `Can Akyıldırım` |
| 2 | `site_keywords` | `software developer, python, django, ...` |
| 3 | `site_description` | `Personal portfolio and blog of Can Akyıldırım` |
| 4 | `home_banner_name` | `Can Akyıldırım` |
| 5 | `home_banner_title` | `Software Developer` |
| 6 | `home_banner_description` | `Building modern web applications...` |
| 7 | `about_myself_welcome` | `Welcome text for the about section...` |
| 8 | `about_myself_footer` | `Short bio text for footer and author cards...` |
| 9 | `contact_email` | `akyildirimcan@gmail.com` |
| 10 | `contact_phone` | `+90 (552) 256 14 05` |
| 11 | `contact_location` | `Eskişehir, Turkey` |

### ImageSetting (3 kayıt)

| # | Name (tam olarak bu şekilde) | Dosya |
|---|------------------------------|-------|
| 1 | `header_logo` | Site logosu (PNG/SVG) |
| 2 | `home_banner_image` | Ana sayfa hero resmi |
| 3 | `site_favicon` | Favicon (PNG, 32x32 veya 64x64) |

---

## 5. Template Blokları

`layout.html` tarafından sağlanan override edilebilir bloklar:

| Blok | Açıklama | Varsayılan |
|------|----------|------------|
| `{% block title %}` | Sayfa başlığı | `{{ site_title }}` |
| `{% block meta_keywords %}` | SEO anahtar kelimeler | `{{ site_keywords }}` |
| `{% block meta_description %}` | SEO açıklama | `{{ site_description }}` |
| `{% block meta_author %}` | Yazar meta etiketi | `Can AKYILDIRIM` |
| `{% block extra_head %}` | Ek `<head>` içeriği | boş |
| `{% block banner_area %}` | Sayfa banner'ı | boş |
| `{% block content %}` | Ana içerik | boş |
| `{% block extra_scripts %}` | Ek JavaScript | boş |
