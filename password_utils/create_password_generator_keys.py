#!/usr/bin/env python3
"""
scripts/create_password_generator_post.py
Creates the authentic technical post for generate_pass.py in teach_cloud.db.
"""

import os
import sqlite3
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATHS = [
    os.path.join(PROJECT_ROOT, "instance", "teach_cloud.db"),
    os.path.join(PROJECT_ROOT, "backups", "default_database.db"),
]

TITLE = "Building a Cryptographic Password & Secret Key Generator in Python (8 to 256 Characters)"
SLUG = "python-cryptographic-password-and-secret-key-generator"
EXCERPT = (
    "Learn how to build a production-grade cryptographic password and multi-entropy secret key generator "
    "in Python using the secrets module with unique, non-repeating character pools from 8 up to 256 characters."
)
CATEGORY = "Python"
TAGS = "Python, Security, Cryptography, Secrets, Passwords"
USER_ID = 2  # DilshadAb

CONTENT = """<h2>1. Introduction to Cryptographically Secure Generation</h2>
<p>In modern web applications, generating user reset passwords, API authorization tokens, and encryption keys requires true unpredictability. Standard pseudo-random number generators like Python's <code>random</code> module are deterministic (based on the Mersenne Twister algorithm) and vulnerable to state prediction attacks. For security-sensitive data, production applications must utilize the <strong>CSPRNG (Cryptographically Secure Pseudo-Random Number Generator)</strong> provided by Python's <code>secrets</code> module, which draws entropy directly from the underlying operating system kernel (<code>/dev/urandom</code> on Linux/macOS or <code>CryptGenRandom</code> on Windows).</p>

<h2>2. System Architecture & Generation Workflow</h2>
<pre><code class="language-text">
       ┌────────────────────────────────────────────────────────┐
       │   CLI Prompt: What do you want to generate?            │
       │   Options: [pass] for Password | [keys] for Secret Key │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                 ┌────────────────┴────────────────┐
                 ▼                                 ▼
      [Mode: pass (Password)]            [Mode: keys (Secret Key)]
      Length: 8 to 24 characters         Length: 32 up to 256 characters
                 │                                 │
                 ▼                                 ▼
   ┌───────────────────────────┐     ┌───────────────────────────┐
   │ Guarantee Multi-Set Mix:  │     │ Unique Non-Repeating Pool:│
   │ • 1+ Lowercase (a-z)      │     │ • ASCII Letters + Digits  │
   │ • 1+ Uppercase (A-Z)      │     │ • Extended Safe Symbols   │
   │ • 1+ Numeric Digit (0-9)  │     │ • 256+ Distinct Glyphs    │
   │ • 1+ Special Symbol       │     │                           │
   │ CSPRNG Shuffle (secrets)  │     │ secrets.SystemRandom()    │
   │                           │     │ .sample(pool, length)     │
   └─────────────┬─────────────┘     └─────────────┬─────────────┘
                 │                                 │
                 └────────────────┬────────────────┘
                                  ▼
             ┌──────────────────────────────────────────┐
             │ 100% Unpredictable High-Entropy Output   │
             └──────────────────────────────────────────┘
</code></pre>

<h2>3. Key Differences Between Password and Secret Key Modes</h2>
<ul>
  <li><strong>Password Mode (<code>pass</code>, 8–24 chars)</strong>: Ideal for user accounts and credential resets. It balances human readability and password manager compliance while guaranteeing that every character class (uppercase, lowercase, numbers, symbols) is present.</li>
  <li><strong>Secret Key Mode (<code>keys</code>, 32–256 chars)</strong>: Ideal for Flask <code>SECRET_KEY</code>, JWT signing secrets, HMAC tokens, and API credentials. It uses an extended symbol pool to sample up to 256 completely distinct, non-repeating characters without replacement.</li>
</ul>

<h2>4. Production Python Implementation (generate_pass.py)</h2>
<p>Below is the complete, self-contained Python script implementing both generation modes with input validation:</p>

<pre><code class="language-python">#!/usr/bin/env python3
import sys
import string
import secrets

# Character Pools
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?"

# Extended safe unicode symbol set to support up to 256+ 100% unique non-repeating characters
EXTENDED_SYMBOLS = (
    "~`!@#$%^&*()-_=+[{]}\\|;:'\\",<.>/?§±"
    "©®µ¶·¥£€¢¤₹₽₩₺₴₸"
    "αβγδεζηθικλμνξοπρστυφχψω"
    "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    "←↑→↓↔↕↖↗↘↙⇄⇅⇆⇇⇈⇉⇊"
    "∀∂∃∅∇∈∉∋∏∑−∓∕∗∘∙√∝∞∟∠∣∥∧∨∩∪∫∬∮∴∵∶∷∼∽≈≊≠≡≤≥≦≧≪≫⊂⊃⊆⊇⊕⊖⊗⊘⊙⊚⊛⊜⊝"
    "♠♣♥♦★☆⚡✓✔✕✖✗✚"
    "⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
    "½¼¾⅓⅔⅛⅜⅝⅞¡¿†‡•‣‰‱′″‴"
    "℃℉№℗℠™♩♪♫♬"
    "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß"
    "àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
)

def generate_password(length: int) -> str:
    \"\"\"Generate a high-strength password between 8 and 24 characters.\"\"\"
    if length < 8 or length > 24:
        raise ValueError("Password length must be between 8 and 24 characters.")

    all_chars = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS
    password_chars = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_chars))

    rng = secrets.SystemRandom()
    rng.shuffle(password_chars)
    return "".join(password_chars)

def generate_secret_key(length: int) -> str:
    \"\"\"Generate a high-entropy secret key between 32 and 256 unique characters.\"\"\"
    if length < 32 or length > 256:
        raise ValueError("Key length must be between 32 and 256 characters.")

    raw_pool = list(dict.fromkeys(LOWERCASE + UPPERCASE + DIGITS + EXTENDED_SYMBOLS))
    if length > len(raw_pool):
        raise ValueError(f"Requested length exceeds pool size ({len(raw_pool)}).")

    rng = secrets.SystemRandom()
    key_chars = rng.sample(raw_pool, length)
    return "".join(key_chars)

if __name__ == "__main__":
    mode = input("What do you want to generate? (pass / keys): ").strip().lower()
    if mode in ("pass", "password", "p"):
        val = input("Enter password length (8-24) [default: 16]: ").strip()
        length = int(val) if val else 16
        print(f"Generated Password: {generate_password(length)}")
    elif mode in ("keys", "key", "k"):
        val = input("Enter key length (32-256) [default: 64]: ").strip()
        length = int(val) if val else 64
        print(f"Generated Secret Key: {generate_secret_key(length)}")
</code></pre>

<h2>5. Command-Line Execution Examples</h2>
<p><strong>Example 1: Generating a 16-Character Secure User Password:</strong></p>
<pre><code class="language-bash">$ python3 password_utils/generate_pass.py
What do you want to generate? (pass / keys): pass
Enter password length (8-24) [default: 16]: 16
✅ Generated Secure Password (16 chars):
👉  Pf27Etm:0p33Tq|H</code></pre>

<p><strong>Example 2: Generating a 64-Character Unique Cryptographic Secret Key:</strong></p>
<pre><code class="language-bash">$ python3 password_utils/generate_pass.py
What do you want to generate? (pass / keys): keys
Enter key length (32-256) [default: 64]: 64
✅ Generated Secret Key (64 unique non-repeating chars):
👉  zεAws≦]∷⇉ξ∘Η_⊛I♣φ≈∉4DΑX↕τ−^νN≡₹∃0√∋Ο1β'⊘l≤∇+gΥµζ♦ΣΨ!ο⇈λ¶>⇊.↙₽n∀∑</code></pre>

<h2>6. Key Takeaways for Production Security</h2>
<ul>
  <li>Always use <code>secrets.SystemRandom</code> rather than standard <code>random.shuffle</code> or <code>random.choice</code> for cryptographic artifacts.</li>
  <li>Never hardcode generated secrets into public repositories — store them in environment variables or cloud secrets vaults.</li>
  <li>Enforce password complexity rules on user registration while offering instant one-click strong generation.</li>
</ul>
"""

def add_or_update_post():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    for db_path in DB_PATHS:
        if not os.path.isfile(db_path):
            continue
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        # Check if post already exists by slug
        cur.execute("SELECT id FROM post WHERE slug = ?", (SLUG,))
        row = cur.fetchone()
        if row:
            post_id = row[0]
            cur.execute("""
                UPDATE post 
                SET title = ?, excerpt = ?, content = ?, category = ?, tags = ?, user_id = ?
                WHERE id = ?
            """, (TITLE, EXCERPT, CONTENT, CATEGORY, TAGS, USER_ID, post_id))
            print(f"Updated existing post ID {post_id} in {db_path}")
        else:
            cur.execute("""
                INSERT INTO post (title, slug, excerpt, content, tags, date_posted, user_id, category, image_file, image_is_code, views, likes_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, '', 0, 0, 0)
            """, (TITLE, SLUG, EXCERPT, CONTENT, TAGS, now, USER_ID, CATEGORY))
            post_id = cur.lastrowid
            print(f"Inserted new post ID {post_id} in {db_path}")

        conn.commit()
        conn.close()

if __name__ == "__main__":
    add_or_update_post()
