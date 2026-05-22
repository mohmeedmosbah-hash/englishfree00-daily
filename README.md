# 📚 نظام تعلم الإنجليزية اليومي

نظام مؤتمت يرسل لك **10 كلمات إنجليزية يومياً** مع الترجمة والأمثلة عبر GitHub.

---

## ⚙️ خطوات الإعداد (مرة واحدة فقط)

### 1️⃣ أنشئ Repository جديد على GitHub
- اذهب إلى [github.com/new](https://github.com/new)
- اسمه: `english-daily`
- اجعله **Public** أو **Private** (كما تريد)

### 2️⃣ ارفع هذه الملفات
ارفع المجلد كاملاً داخل الـ Repository

### 3️⃣ أضف مفتاح Claude API
1. اذهب إلى: **Settings → Secrets and variables → Actions**
2. اضغط **New repository secret**
3. الاسم: `ANTHROPIC_API_KEY`
4. القيمة: مفتاح API من [console.anthropic.com](https://console.anthropic.com)

### 4️⃣ فعّل GitHub Actions
- اذهب إلى تبويب **Actions**
- اضغط **Enable Actions**

### 5️⃣ اختبر النظام يدوياً
- اذهب إلى **Actions → كلمات إنجليزية يومية**
- اضغط **Run workflow**
- انتظر دقيقة وستجد Issue جديد! 🎉

---

## 📱 استقبال الكلمات على هاتفك

### عبر تطبيق GitHub
1. حمّل تطبيق **GitHub** من Play Store
2. افتح الـ Repository
3. فعّل الإشعارات: **Watch → Issues**
4. ستصلك إشعار كل يوم بالكلمات الجديدة!

### عبر البريد الإلكتروني
GitHub يرسل تلقائياً إيميل عند كل Issue جديد إذا فعّلت الإشعارات.

---

## ⏰ توقيت الإرسال
كل يوم الساعة **8:00 صباحاً** (توقيت ليبيا / UTC+2)

---

## 🔧 تخصيص النظام

في ملف `.github/workflows/daily-english.yml` غيّر:
```
- cron: '0 6 * * *'   ← 8 صباحاً ليبيا
- cron: '0 5 * * *'   ← 7 صباحاً ليبيا
- cron: '0 8 * * *'   ← 10 صباحاً ليبيا
```

---

## 📊 مثال على الكلمات اليومية

```
### 1. Achieve
- 🇦🇪 المعنى: يحقق / ينجز
- 🗣️ النطق: /أَتْشيف/
- 📝 مثال: She achieved her goal.
- 🔄 ترجمة المثال: هي حققت هدفها.
```
