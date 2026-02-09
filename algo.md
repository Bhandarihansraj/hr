Below is **ONLY PRACTICAL CODE + USE**
👉 **no theory, no extra text**
👉 **Kali Linux + John the Ripper**

---

## 🔹 CREATE PASSWORD

```bash
echo -n "test123" > pass.txt
```

**Use:** sample password

---

## 🔹 MD5

```bash
md5sum pass.txt
```

**Use:** create MD5 hash

```bash
john --format=raw-md5 hash_md5.txt
john --show hash_md5.txt
```

**Use:** crack MD5

---

## 🔹 SHA1

```bash
sha1sum pass.txt
```

**Use:** create SHA1 hash

```bash
john --format=raw-sha1 hash_sha1.txt
john --show hash_sha1.txt
```

**Use:** crack SHA1

---

## 🔹 SHA256

```bash
sha256sum pass.txt
```

**Use:** create SHA256 hash

```bash
john --format=raw-sha256 hash_sha256.txt
john --show hash_sha256.txt
```

**Use:** crack SHA256

---

## 🔹 SHA512

```bash
sha512sum pass.txt
```

**Use:** create SHA512 hash

```bash
john --format=raw-sha512 hash_sha512.txt
john --show hash_sha512.txt
```

**Use:** crack SHA512

---

## 🔹 bcrypt

```bash
openssl passwd -bcrypt test123
```

**Use:** create bcrypt hash

```bash
john --format=bcrypt hash_bcrypt.txt
john --show hash_bcrypt.txt
```

**Use:** crack bcrypt

---

## 🔹 NTLM

```bash
echo -n "test123" | iconv -t UTF-16LE | md4sum
```

**Use:** create NTLM hash

```bash
john --format=NT hash_ntlm.txt
john --show hash_ntlm.txt
```

**Use:** crack NTLM

---

## 🔹 WORDLIST ATTACK (ALL)

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

**Use:** dictionary crack

---

## 🔹 RULES

```bash
john --wordlist=rockyou.txt --rules hash.txt
```

**Use:** smart mutations

---

## 🔹 MASK

```bash
john --mask=?l?l?l?d?d?d hash.txt
```

**Use:** pattern-based crack

---

## 🔹 BRUTE FORCE

```bash
john --incremental hash.txt
```

**Use:** full brute force

---

## 🔹 SESSION

```bash
john --session=test hash.txt
john --restore=test
```

**Use:** pause/resume

---

## 🔹 SPEED

```bash
john --fork=4 hash.txt
john --status
```

**Use:** multi-core + progress

---

## 🔹 LINUX PASSWORD FILE (LAB VM)

```bash
sudo unshadow /etc/passwd /etc/shadow > crack.txt
john crack.txt
```

**Use:** system audit

---

## 🔹 FORMAT LIST

```bash
john --list=formats
```

**Use:** supported algorithms

---

If you want **same thing as PDF** or **Hashcat GPU version**, say **next**.

Below is **DEMO: create hashes for ALL main hash algorithms (Kali/Linux)**
👉 **ONLY commands**
👉 **step-wise**
👉 **copy-paste ready**

---

## 1️⃣ Create test password

```bash
echo -n "test123" > pass.txt
```

---

## 2️⃣ WEAK / OLD HASHES

### MD5

```bash
md5sum pass.txt
```

### SHA1

```bash
sha1sum pass.txt
```

---

## 3️⃣ MODERN SHA FAMILY

### SHA224

```bash
sha224sum pass.txt
```

### SHA256

```bash
sha256sum pass.txt
```

### SHA384

```bash
sha384sum pass.txt
```

### SHA512

```bash
sha512sum pass.txt
```

---

## 4️⃣ PASSWORD HASHES (REAL SYSTEMS)

### bcrypt

```bash
openssl passwd -bcrypt test123
```

### SHA256-crypt

```bash
openssl passwd -6 test123
```

### SHA512-crypt

```bash
openssl passwd -6 -salt mysalt test123
```

---

## 5️⃣ WINDOWS HASHES

### NTLM

```bash
echo -n "test123" | iconv -t UTF-16LE | md4sum
```

---

## 6️⃣ HMAC (KEYED HASH)

### HMAC-SHA256

```bash
echo -n "test123" | openssl dgst -sha256 -hmac "secretkey"
```

### HMAC-SHA512

```bash
echo -n "test123" | openssl dgst -sha512 -hmac "secretkey"
```

---

## 7️⃣ OTHER HASHES

### RIPEMD-160

```bash
openssl dgst -ripemd160 pass.txt
```

### Whirlpool

```bash
openssl dgst -whirlpool pass.txt
```

---

## 8️⃣ SAVE ANY HASH (for cracking demo)

```bash
echo "HASH_VALUE_HERE" > hash.txt
```

---

## 9️⃣ VERIFY HASH (match test)

```bash
echo -n "test123" | sha256sum
```

---

## 🔟 ONE-LINE CHECK (ALL SHA)

```bash
openssl dgst -sha1 -sha256 -sha512 pass.txt
```

---

If you want next (say one):

* **same demo + crack with John**
* **hash → where used (OS, web, DB)**
* **college PDF practical**
* **hash vs encryption demo**

Just say **next** ✅
