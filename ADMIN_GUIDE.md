# 🎯 Django Admin Panel Kullanım Rehberi

## 📍 Admin Paneline Erişim

1. **Superuser Oluşturma** (İlk kurulumda):
```bash
docker-compose exec web python manage.py createsuperuser
```
   - Username: `admin` (veya istediğiniz)
   - Email: `akyildirimcan@gmail.com`
   - Password: Güçlü bir şifre belirleyin

2. **Admin Paneline Giriş**:
   - URL: `http://localhost/admin/` veya `https://me.softdevcan.site/admin/`
   - Yukarıda belirlediğiniz kullanıcı adı ve şifreyle giriş yapın

---

## 🏠 Home Sayfası İçerikleri

### 1. **Banner (Üst Kısım) Ayarları**

#### 📸 Banner Resmi
**Model**: Image Settings
**Name**: `home_banner_image`

1. Admin'de `Core > Image settings` bölümüne gidin
2. "Add Image Setting" butonuna tıklayın
3. Alanları doldurun:
   - **Name**: `home_banner_image` (tam olarak böyle yazın)
   - **Description**: `Home page banner profile image`
   - **File**: Profilinizin fotoğrafını yükleyin (önerilen: 400x400px)
4. Save edin

#### 📝 Banner Metinleri
**Model**: General Settings
Aşağıdaki ayarları tek tek ekleyin:

| Name | Parameter Değeri | Description |
|------|------------------|-------------|
| `home_banner_name` | `Can Akyıldırım` | İsminiz |
| `home_banner_title` | `Backend Developer` | Meslek unvanınız |
| `home_banner_description` | `Scalable web applications with Django...` | Kendinizi tanıtan kısa açıklama |

**Not**: Name değerleri yukarıdaki gibi tam olarak yazılmalı (template'de bu isimlerle çağrılıyor)

---

### 2. **👤 Kişisel Bilgiler** (Template'de Hard-coded)

Template'de şu bilgiler direkt yazılı ([index.html:21-24](templates/index.html#L21-L24)):
- Doğum tarihi: `February 5, 1997`
- Telefon: `+90 (552) 256 14 05`
- Email: `akyildirimcan@gmail.com`
- Konum: `Eskişehir, Turkey`

**Değiştirmek için**: `templates/index.html` dosyasını düzenleyin.

---

### 3. **🔗 Sosyal Medya Linkleri**

**Model**: Social Media

Her sosyal medya hesabı için:
1. `Core > Social Media` bölümüne gidin
2. "Add Social Media" butonuna tıklayın
3. Alanları doldurun:
   - **Order**: Görünüm sırası (örn: 0, 1, 2...)
   - **Link**: Profil URL'iniz (örn: `https://github.com/canakyildiri`)
   - **Icon**: Font Awesome HTML kodu

**Icon Örnekleri** (Font Awesome SVG formatında):
```html
<!-- GitHub -->
<i class="fa-brands fa-github"></i>

<!-- LinkedIn -->
<i class="fa-brands fa-linkedin"></i>

<!-- Twitter/X -->
<i class="fa-brands fa-x-twitter"></i>

<!-- Email -->
<i class="fa-solid fa-envelope"></i>
```

**Örnek Kayıt**:
- Order: `0`
- Link: `https://github.com/canakyildiri`
- Icon: `<i class="fa-brands fa-github"></i>`

---

### 4. **💻 Yetenekler (Skills)**

**Model**: Skill
**Kategoriler**: Backend, Frontend, DevOps, Other

Her yetenek için:
1. `Core > Skills` bölümüne gidin
2. "Add Skill" butonuna tıklayın
3. Alanları doldurun:
   - **Order**: Görünüm sırası
   - **Name**: Teknoloji/dil adı (örn: `Python`, `Django`, `PostgreSQL`)
   - **Percentage**: Yeterlilik seviyesi (0-100 arası)
   - **Skill Type**: `Backend`, `Frontend`, `DevOps` veya `Other`

**Backend Örnekleri**:
- Python: 95%
- Django: 90%
- PostgreSQL: 85%
- Redis: 80%
- REST API: 90%

**Frontend Örnekleri**:
- HTML/CSS: 85%
- JavaScript: 80%
- Bootstrap: 85%

**DevOps Örnekleri**:
- Docker: 85%
- Nginx: 80%
- Git: 90%
- Linux: 85%

---

### 5. **💼 İş Deneyimleri**

**Model**: Experience

Her iş deneyimi için:
1. `Core > Experiences` bölümüne gidin
2. "Add Experience" butonuna tıklayın
3. Alanları doldurun:
   - **Company Name**: Şirket adı (örn: `ABC Tech`)
   - **Job Title**: Pozisyon (örn: `Backend Developer`)
   - **Job Location**: Lokasyon (örn: `Istanbul, Turkey`)
   - **Start Date**: Başlangıç tarihi (örn: `2023-01-15`)
   - **End Date**: Bitiş tarihi (boş bırakırsanız "Present" gösterir)

**Örnek Kayıt**:
```
Company Name: Freelance
Job Title: Backend Developer
Job Location: Remote
Start Date: 2024-01-01
End Date: (boş - halen çalışıyorum)
```

---

### 6. **🎓 Eğitim Bilgileri**

**Model**: Education

Her eğitim kaydı için:
1. `Core > Educations` bölümüne gidin
2. "Add Education" butonuna tıklayın
3. Alanları doldurun:
   - **School Name**: Okul/üniversite adı (örn: `Anadolu University`)
   - **Major**: Bölüm (örn: `Computer Science`)
   - **Department**: Fakülte/Departman (örn: `Engineering Faculty`)
   - **Start Date**: Başlangıç tarihi (örn: `2015-09-01`)
   - **End Date**: Mezuniyet tarihi (boş bırakırsanız "Present" gösterir)

**Örnek Kayıt**:
```
School Name: Anadolu University
Major: Computer Engineering
Department: Engineering Faculty
Start Date: 2015-09-01
End Date: 2020-06-30
```

---

### 7. **📄 Belgeler (CV vb.)**

**Model**: Document

CV veya sertifika dosyaları için:
1. `Core > Documents` bölümüne gidin
2. "Add Document" butonuna tıklayın
3. Alanları doldurun:
   - **Order**: Görünüm sırası
   - **Slug**: URL-friendly isim (örn: `cv`, `resume`)
   - **Button Text**: Buton üzerinde görünecek metin (örn: `Download CV`)
   - **File**: PDF dosyanızı yükleyin

**Örnek Kayıt**:
```
Order: 0
Slug: cv
Button Text: Download CV
File: can_akyildirim_cv.pdf
```

---

## 🎨 Portfolio (Projeler) Sayfası

### 8. **📁 Proje Kategorileri**

**Model**: Project Category

1. `Core > Project Categories` bölümüne gidin
2. Kategori ekleyin (örn: `Web Development`, `Mobile Apps`, `Data Science`)

### 9. **🚀 Projeler**

**Model**: Project

Her proje için:
1. `Core > Projects` bölümüne gidin
2. "Add Project" butonuna tıklayın
3. Alanları doldurun:
   - **Title**: Proje adı
   - **Slug**: URL-friendly isim (otomatik oluşur)
   - **Category**: Kategori seçin
   - **Description**: Kısa açıklama (özet)
   - **Content**: Detaylı açıklama (Markdown destekler!)
   - **Featured Image**: Proje görseli
   - **GitHub URL**: GitHub repo linki (opsiyonel)
   - **Live URL**: Canlı demo linki (opsiyonel)
   - **Technologies**: Kullanılan teknolojiler (virgülle ayrılmış, örn: `Django, PostgreSQL, Docker`)
   - **Is Featured**: Öne çıkan proje mi?
   - **Is Published**: Yayınlansın mı?
   - **Order**: Görünüm sırası

**Örnek Proje**:
```
Title: Portfolio Website
Category: Web Development
Description: Personal portfolio and blog built with Django
Content: ## Overview
This is my personal portfolio website...

Technologies: Django, PostgreSQL, Redis, Docker, Nginx
Is Featured: ✓
Is Published: ✓
Order: 0
```

---

## 📝 Blog Yönetimi

### 10. **Blog Kategorileri**

`Blog > Categories` bölümünden kategori ekleyin (örn: `Python`, `Django`, `DevOps`)

### 11. **Blog Etiketleri**

`Blog > Tags` bölümünden etiket ekleyin (örn: `tutorial`, `best-practices`)

### 12. **Blog Yazıları**

`Blog > Posts` bölümünden yazı ekleyin:
- **Markdown desteği** vardır
- Taslak olarak kaydedip sonra yayınlayabilirsiniz
- Featured image ekleyebilirsiniz

---

## 🎯 Hızlı Başlangıç Kontrol Listesi

- [ ] Superuser oluştur
- [ ] Admin paneline giriş yap
- [ ] Banner resmi ekle (`home_banner_image`)
- [ ] Banner metinlerini ekle (`home_banner_name`, `home_banner_title`, `home_banner_description`)
- [ ] En az 3 sosyal medya linki ekle
- [ ] Backend skills ekle (en az 5 tane)
- [ ] Frontend skills ekle (en az 3 tane)
- [ ] DevOps skills ekle (en az 3 tane)
- [ ] En az 1 iş deneyimi ekle
- [ ] En az 1 eğitim kaydı ekle
- [ ] CV dosyası yükle (opsiyonel)
- [ ] En az 1 proje kategorisi oluştur
- [ ] En az 1 proje ekle
- [ ] En az 1 blog kategorisi oluştur
- [ ] İlk blog yazını yaz

---

## 🔧 Önemli Notlar

1. **Name Değerleri**: GeneralSetting ve ImageSetting'lerde `name` alanı template'lerde kullanılıyor. Yukarıda belirtilen isimlerle tam eşleşmeli!

2. **Redis Cache**: İçerik değişikliklerinde cache otomatik temizlenir (signals sayesinde)

3. **Dosya Yükleme**: Resimler `media/image_settings/` ve `media/projects/` klasörlerine kaydedilir

4. **Markdown**: Blog ve proje içerikleri Markdown formatını destekler

5. **Template Değişiklikleri**: Kişisel bilgilerinizi (telefon, email) `templates/index.html` dosyasından düzenleyin

---

## 🆘 Sorun Giderme

**Admin paneli açılmıyor?**
```bash
# Servisleri kontrol edin
docker-compose ps

# Logları kontrol edin
docker-compose logs web
```

**Resim yüklenmiyor?**
- `media/` klasörünün yazma izinleri olduğundan emin olun
- Dosya boyutunu kontrol edin (çok büyük olmasın)

**Cache güncellenmiyor?**
```bash
# Redis'i yeniden başlatın
docker-compose restart redis
```

---

**Başarılar! 🚀**
