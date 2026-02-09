Below is **John the Ripper commands shown HERE with clear examples**
👉 short • practical • copy-paste ready

---

## 1️⃣ Basic Crack

```bash
john hash.txt
```

**Use:** start cracking hashes
**Example:** crack simple hashes in `hash.txt`

---

## 2️⃣ Help / Info

```bash
john --help
john --version
```

**Use:** options / version check

---

## 3️⃣ Show Cracked Passwords

```bash
john --show hash.txt
```

**Use:** display cracked passwords
**Output:** `user:password`

---

## 4️⃣ Specify Hash Type

```bash
john --list=formats
john --format=md5 hash.txt
```

**Use:** when auto-detect fails
**Example:** force MD5 cracking

---

## 5️⃣ Wordlist Attack

```bash
john --wordlist=rockyou.txt hash.txt
```

**Use:** dictionary attack
**Example:** common real-world passwords

---

## 6️⃣ Wordlist + Rules (Smart)

```bash
john --wordlist=rockyou.txt --rules hash.txt
```

**Use:** add mutations
**Example:** `admin` → `Admin@123`

---

## 7️⃣ Incremental (Brute Force)

```bash
john --incremental hash.txt
```

**Use:** full brute force
**Example:** unknown passwords

---

## 8️⃣ Numeric Only

```bash
john --incremental=Digits hash.txt
```

**Use:** PIN / numbers only
**Example:** `1234`, `987654`

---

## 9️⃣ Mask Attack (Fast & Targeted)

```bash
john --mask=?l?l?l?d hash.txt
```

**Use:** pattern-based
**Example:** `abc1`, `xyz9`

Common masks:

* `?l` = lowercase
* `?u` = uppercase
* `?d` = digit
* `?s` = symbol

---

## 🔟 Linux Password Files

```bash
unshadow /etc/passwd /etc/shadow > crack.txt
john crack.txt
```

**Use:** Linux password audit

---

## 1️⃣1️⃣ Session Save / Resume

```bash
john --session=test hash.txt
john --restore=test
```

**Use:** resume after stop

---

## 1️⃣2️⃣ Use CPU Cores

```bash
john --fork=4 hash.txt
```

**Use:** faster cracking (multi-core)

---

## 1️⃣3️⃣ Status Check

```bash
john --status
```

**Use:** see progress live

---

## 1️⃣4️⃣ User-Specific Crack

```bash
john --users=admin hash.txt
```

**Use:** target single user

---

## 1️⃣5️⃣ Combine Everything (Real-World)

```bash
john --format=sha256crypt \
--wordlist=rockyou.txt \
--rules \
--fork=4 \
hash.txt
```

**Use:** realistic audit workflow

---

### 🧠 Smart Order (remember)

**Identify hash → Wordlist → Rules → Mask → Incremental → Show**

If you want next:

* **Hash types explained with examples**
* **Why brute force feels “infinite”**
* **John vs Hashcat (real difference)**
* **Advanced rule writing (killer part)**

Say **next** 👍
