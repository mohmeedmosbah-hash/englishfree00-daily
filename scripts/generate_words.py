import anthropic
import os
import requests
from datetime import datetime, timezone, timedelta

# ─── توليد الكلمات عبر Claude ───────────────────────────────────────────────

def generate_words():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = """أنت مدرّس لغة إنجليزية للمبتدئين العرب.

اختر 10 كلمات إنجليزية شائعة ومفيدة في الحياة اليومية (مستوى A2).
لكل كلمة اكتب بالتنسيق التالي حرفياً:

### {رقم}. {الكلمة}
- 🇦🇪 **المعنى:** {الترجمة العربية}
- 🗣️ **النطق:** /{النطق التقريبي بالأحرف العربية}/
- 📝 **مثال:** {جملة إنجليزية بسيطة}
- 🔄 **ترجمة المثال:** {ترجمة الجملة للعربية}

اجعل الكلمات متنوعة: أفعال، صفات، أسماء. لا تكرر كلمات من أيام سابقة."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2500,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


# ─── إنشاء Issue على GitHub ─────────────────────────────────────────────────

def create_github_issue(words_content):
    token   = os.environ["GITHUB_TOKEN"]
    repo    = os.environ["GITHUB_REPOSITORY"]

    # التاريخ بالتوقيت الليبي
    libya_tz = timezone(timedelta(hours=2))
    now      = datetime.now(libya_tz)
    date_str = now.strftime("%Y-%m-%d")

    days_ar = ["الاثنين","الثلاثاء","الأربعاء","الخميس","الجمعة","السبت","الأحد"]
    day_ar  = days_ar[now.weekday()]

    body = f"""## 🇬🇧 كلمات اليوم العشر — {day_ar} {date_str}

{words_content}

---

### 💡 نصائح لتثبيت الكلمات
- 🔁 كرر كل كلمة بصوت عالٍ **3 مرات**
- ✍️ اكتب جملة خاصة بك لكل كلمة
- 🃏 استخدم بطاقات (Flashcards) في تطبيق **Anki**
- 📅 راجع كلمات **الأمس** قبل البدء بكلمات اليوم

---
> 🎯 **هدفك:** 10 كلمات يومياً = 300 كلمة شهرياً = إنجليزية سلسة خلال 6 أشهر!
"""

    headers = {
        "Authorization": f"token {token}",
        "Accept":        "application/vnd.github.v3+json",
    }

    # إنشاء الـ labels إن لم تكن موجودة
    for label, color, desc in [
        ("daily-english", "0075ca", "كلمات إنجليزية يومية"),
        ("vocabulary",    "e4e669", "مفردات"),
    ]:
        requests.post(
            f"https://api.github.com/repos/{repo}/labels",
            headers=headers,
            json={"name": label, "color": color, "description": desc},
        )

    # إنشاء الـ Issue
    resp = requests.post(
        f"https://api.github.com/repos/{repo}/issues",
        headers=headers,
        json={
            "title":  f"📚 كلمات إنجليزية يومية — {date_str}",
            "body":   body,
            "labels": ["daily-english", "vocabulary"],
        },
    )

    if resp.status_code == 201:
        print(f"✅ Issue created successfully: {resp.json()['html_url']}")
    else:
        print(f"❌ Error {resp.status_code}: {resp.text}")
        raise SystemExit(1)


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🔄 Generating English words with Claude...")
    words = generate_words()
    print("✅ Words generated!\n")
    print(words)
    print("\n📝 Creating GitHub Issue...")
    create_github_issue(words)
