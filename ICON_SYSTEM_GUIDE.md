# 🎨 Icon System Guide

## 🎯 Overview

Uygulama artık modern bir icon sistemi kullanıyor:
- ✅ **SocialMedia**: Dropdown ile platform seçimi (otomatik icon)
- ✅ **Skill**: Otomatik icon (skill adına göre)
- ✅ **Font Awesome 6**: 2000+ modern icon
- ✅ **Devicon**: 150+ programlama dili/teknoloji logosu
- ✅ **Django Unfold**: Modern admin panel teması

---

## 🔗 SocialMedia - Platform Seçimi

### Admin Panelinde Kullanım

1. **Admin paneline git**: `/admin/core/socialmedia/`
2. **Add Social Media** butonuna tıkla
3. **Platform dropdown'dan seç**:
   - GitHub
   - LinkedIn
   - Twitter / X
   - Instagram
   - Kaggle
   - HackerRank
   - Email
   - vs.
4. **Link** gir (örn: `https://github.com/canakyildiri`)
5. **Save** et

**Icon otomatik gelir!** ✅

### Desteklenen Platformlar

| Platform | Icon | Örnek Link |
|----------|------|------------|
| GitHub | <i class="fa-brands fa-github"></i> | https://github.com/username |
| LinkedIn | <i class="fa-brands fa-linkedin"></i> | https://linkedin.com/in/username |
| Twitter/X | <i class="fa-brands fa-x-twitter"></i> | https://twitter.com/username |
| Instagram | <i class="fa-brands fa-instagram"></i> | https://instagram.com/username |
| Facebook | <i class="fa-brands fa-facebook"></i> | https://facebook.com/username |
| YouTube | <i class="fa-brands fa-youtube"></i> | https://youtube.com/@username |
| Medium | <i class="fa-brands fa-medium"></i> | https://medium.com/@username |
| Dev.to | <i class="fa-brands fa-dev"></i> | https://dev.to/username |
| Kaggle | <i class="fa-brands fa-kaggle"></i> | https://kaggle.com/username |
| HackerRank | <i class="fa-brands fa-hackerrank"></i> | https://hackerrank.com/username |
| LeetCode | <i class="fa-solid fa-code"></i> | https://leetcode.com/username |
| CodePen | <i class="fa-brands fa-codepen"></i> | https://codepen.io/username |
| Stack Overflow | <i class="fa-brands fa-stack-overflow"></i> | https://stackoverflow.com/users/xxx |
| Reddit | <i class="fa-brands fa-reddit"></i> | https://reddit.com/u/username |
| Discord | <i class="fa-brands fa-discord"></i> | discord.gg/invite |
| Telegram | <i class="fa-brands fa-telegram"></i> | t.me/username |
| WhatsApp | <i class="fa-brands fa-whatsapp"></i> | wa.me/phone |
| Email | <i class="fa-solid fa-envelope"></i> | mailto:email@example.com |
| Website | <i class="fa-solid fa-globe"></i> | https://yourwebsite.com |
| Other | <i class="fa-solid fa-link"></i> | Any URL |

### Custom Icon (Opsiyonel)

Eğer platforma özel icon istemiyorsanız:
1. **Custom Icon** alanına manuel icon kodu girin
2. Örnek: `<i class="fa-solid fa-heart"></i>`
3. Bu custom icon, platform icon'unu override eder

---

## 💻 Skills - Otomatik Icon

### Admin Panelinde Kullanım

1. **Admin paneline git**: `/admin/core/skill/`
2. **Add Skill** butonuna tıkla
3. **Name** gir (örn: `Python`, `Django`, `Docker`)
4. **Percentage** seç (0-100)
5. **Skill Type** seç (Backend/Frontend/DevOps/Other)
6. **Save** et

**Icon otomatik belirlenir!** ✅

### Desteklenen Teknolojiler

#### Backend
| Skill Name | Icon | Library |
|------------|------|---------|
| Python | 🐍 Python logo | Devicon |
| Django | Django logo | Devicon |
| Flask | Flask logo | Devicon |
| FastAPI | FastAPI logo | Devicon |
| Java | ☕ Java logo | Devicon |
| Spring | Spring logo | Devicon |
| Node.js | Node.js logo | Devicon |
| Express | Express logo | Devicon |
| PHP | PHP logo | Devicon |
| Laravel | Laravel logo | Devicon |
| Ruby | Ruby logo | Devicon |
| Rails | Rails logo | Devicon |
| Go | Go logo | Devicon |
| Rust | Rust logo | Devicon |
| C# | C# logo | Devicon |
| .NET | .NET logo | Devicon |

#### Frontend
| Skill Name | Icon | Library |
|------------|------|---------|
| HTML / HTML5 | HTML5 logo | Devicon |
| CSS / CSS3 | CSS3 logo | Devicon |
| JavaScript | JS logo | Devicon |
| TypeScript | TS logo | Devicon |
| React | React logo | Devicon |
| Vue / Vue.js | Vue logo | Devicon |
| Angular | Angular logo | Devicon |
| Svelte | Svelte logo | Devicon |
| Bootstrap | Bootstrap logo | Devicon |
| Tailwind | Tailwind logo | Devicon |
| jQuery | jQuery logo | Devicon |
| Sass | Sass logo | Devicon |
| Webpack | Webpack logo | Devicon |

#### Databases
| Skill Name | Icon | Library |
|------------|------|---------|
| PostgreSQL / Postgres | PostgreSQL logo | Devicon |
| MySQL | MySQL logo | Devicon |
| MongoDB | MongoDB logo | Devicon |
| Redis | Redis logo | Devicon |
| SQLite | SQLite logo | Devicon |
| MariaDB | MySQL logo | Devicon |
| Oracle | Oracle logo | Devicon |

#### DevOps & Tools
| Skill Name | Icon | Library |
|------------|------|---------|
| Docker | Docker logo | Devicon |
| Kubernetes | K8s logo | Devicon |
| Git | Git logo | Devicon |
| GitHub | GitHub logo | Devicon |
| GitLab | GitLab logo | Devicon |
| Jenkins | Jenkins logo | Devicon |
| Nginx | Nginx logo | Devicon |
| Apache | Apache logo | Devicon |
| Linux | Linux logo | Devicon |
| Ubuntu | Ubuntu logo | Devicon |
| AWS | AWS logo | Devicon |
| Azure | Azure logo | Devicon |
| GCP | GCP logo | Devicon |
| Terraform | Terraform logo | Devicon |
| Ansible | Ansible logo | Devicon |

#### Other
| Skill Name | Icon | Library |
|------------|------|---------|
| GraphQL | GraphQL logo | Devicon |
| REST API / API | 🔌 Plug icon | Font Awesome |
| VSCode | VSCode logo | Devicon |
| Vim | Vim logo | Devicon |
| pytest | pytest logo | Devicon |
| Jest | Jest logo | Devicon |

### Fallback Icon

Eğer skill adı listede yoksa:
- **Default icon**: `<i class="fa-solid fa-code"></i>` (kod ikonu)

### Case-Insensitive Matching

Skill isimleri büyük/küçük harf duyarsız:
- ✅ `python` = `Python` = `PYTHON` → Hepsi Python logosu

---

## 🎨 Icon Kütüphaneleri

### 1. Font Awesome 6
- **URL**: https://fontawesome.com
- **Version**: 6.5.1
- **Icons**: 2000+
- **Kullanım**: `<i class="fa-solid fa-heart"></i>`
- **Kategoriler**: solid, regular, brands

### 2. Devicon
- **URL**: https://devicon.dev
- **Version**: 2.16.0
- **Icons**: 150+ programlama dili/framework
- **Kullanım**: `<i class="devicon-python-plain colored"></i>`
- **Renk**: `colored` (renkli), `plain` (tek renk)

### 3. Linericon (Legacy)
- **Kullanım**: Mevcut custom iconlar için
- **Yeni projeler için**: Font Awesome kullanın

---

## 🖼️ Admin Panel - Django Unfold

### Modern Tema

Django Unfold modern, kullanıcı dostu bir admin teması:

**Özellikler**:
- ✅ Modern, responsive tasarım
- ✅ Dark mode desteği
- ✅ Daha iyi form layout
- ✅ Gelişmiş filtreleme
- ✅ Inline editing
- ✅ Breadcrumb navigation

**Erişim**: `http://localhost/admin/`

---

## 📝 Kullanım Örnekleri

### Örnek 1: GitHub Profili Ekle

```
Admin > Core > Social Media > Add Social Media
Platform: GitHub
Link: https://github.com/canakyildiri
Order: 0
Save
```

Sonuç:
- ✅ GitHub icon otomatik gelir
- ✅ Banner'da ve footer'da görünür
- ✅ Hover'da "GitHub" tooltip gösterir

### Örnek 2: Python Skill Ekle

```
Admin > Core > Skills > Add Skill
Name: Python
Percentage: 95
Skill Type: Backend
Order: 0
Save
```

Sonuç:
- ✅ Python logosu (🐍) otomatik gelir
- ✅ Home page'de Backend section'da görünür
- ✅ Progress bar %95 dolu

### Örnek 3: Custom Platform Ekle

```
Admin > Core > Social Media > Add Social Media
Platform: Other
Link: https://custom-platform.com/profile
Custom Icon: <i class="fa-solid fa-rocket"></i>
Order: 10
Save
```

Sonuç:
- ✅ Roket icon kullanılır
- ✅ Herhangi bir platform için kullanılabilir

---

## 🔧 Technical Details

### Model Metotları

#### SocialMedia.get_icon()
```python
def get_icon(self):
    """Return icon HTML - custom icon or platform default"""
    if self.icon:
        return self.icon
    return self.PLATFORM_ICONS.get(self.platform, self.PLATFORM_ICONS['other'])
```

#### Skill.get_icon()
```python
def get_icon(self):
    """Return icon HTML based on skill name (case-insensitive)"""
    skill_lower = self.name.lower().strip()
    return self.SKILL_ICONS.get(skill_lower, '<i class="fa-solid fa-code"></i>')
```

### Template Kullanımı

```django
{# SocialMedia #}
{% for social in social_medias %}
    <a href="{{ social.link }}" title="{{ social.get_platform_display }}">
        {{ social.get_icon|safe }}
    </a>
{% endfor %}

{# Skill (gelecekte eklenebilir) #}
{% for skill in skills %}
    {{ skill.get_icon|safe }} {{ skill.name }}: {{ skill.percentage }}%
{% endfor %}
```

---

## 🆕 Yeni Platform/Skill Ekleme

### Yeni Platform Eklemek

1. `core/models.py` dosyasını aç
2. `SocialMedia.PLATFORM_CHOICES` listesine ekle:
```python
('platform_key', 'Platform Display Name'),
```
3. `SocialMedia.PLATFORM_ICONS` dict'ine ekle:
```python
'platform_key': '<i class="fa-brands fa-platform"></i>',
```
4. Migration oluştur: `makemigrations`
5. Migrate et: `migrate`

### Yeni Skill Icon Eklemek

1. `core/models.py` dosyasını aç
2. `Skill.SKILL_ICONS` dict'ine ekle:
```python
'skill_name': '<i class="devicon-skill-plain colored"></i>',
```
3. Migration gerekmez (sadece kod değişikliği)
4. Restart: `docker-compose restart app`

---

## 🎯 Best Practices

### SocialMedia
- ✅ Order kullanarak sıralama yapın (0, 1, 2, 3...)
- ✅ Ana platformları önce ekleyin (GitHub, LinkedIn)
- ✅ Link'leri tam URL olarak girin (https:// ile)
- ✅ Email için: `mailto:your@email.com`

### Skills
- ✅ Popüler teknolojiler için tam isim kullanın ("Python" değil "Pythın")
- ✅ Order ile gruplandırın (Backend: 0-9, Frontend: 10-19, etc.)
- ✅ Percentage'i gerçekçi tutun (abartmayın)
- ✅ Skill Type doğru seçin (otomatik kategorileme için)

---

## 📊 Icon Availability Check

Bir icon'un mevcut olup olmadığını kontrol etmek için:

**Font Awesome**: https://fontawesome.com/search
**Devicon**: https://devicon.dev

Örnek:
- Python icon: https://devicon.dev → "python" ara
- GitHub icon: Font Awesome → "github" ara

---

## 🚀 Migration Summary

### Model Changes
1. ✅ `SocialMedia.platform` field eklendi (CharField with choices)
2. ✅ `SocialMedia.icon` help_text güncellendi
3. ✅ `SocialMedia.link` help_text eklendi
4. ✅ `SocialMedia.get_icon()` metodu eklendi
5. ✅ `Skill.get_icon()` metodu eklendi
6. ✅ `Skill.name` help_text güncellendi

### Template Changes
1. ✅ `index.html`: `social.icon` → `social.get_icon`
2. ✅ `footer.html`: `social.icon` → `social.get_icon`
3. ✅ `head.html`: Font Awesome 6 + Devicon CDN eklendi

### Admin Changes
1. ✅ Django Unfold tema eklendi
2. ✅ Modern admin interface aktif

---

**🎉 Artık admin panelinden kolayca icon ekleyebilirsiniz!**
