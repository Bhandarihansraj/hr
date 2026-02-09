

## 1️⃣ Create password


echo -n "test123" > pass.txt


## 2️⃣ Create hash (example MD5)


md5sum pass.txt > hash.txt


## 3️⃣ View hash file


cat hash.txt


## 4️⃣ List supported formats


john --list=formats


## 5️⃣ Auto-detect & crack

john hash.txt


## 6️⃣ Specify format (example)

```bash
john --format=raw-md5 hash.txt
```

---

## 7️⃣ Show cracked result

```bash
john --show hash.txt
```

---

## 8️⃣ Dictionary attack

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

---

## 9️⃣ Dictionary + rules

```bash
john --wordlist=rockyou.txt --rules hash.txt
```

---

## 🔟 Mask attack

```bash
john --mask=?l?l?l?d?d?d hash.txt
```

---

## 1️⃣1️⃣ Incremental (brute force)

```bash
john --incremental hash.txt
```

---

## 1️⃣2️⃣ Select user (if present)

```bash
john --users=user hash.txt
```

---

## 1️⃣3️⃣ Session save

```bash
john --session=job1 hash.txt
```

---

## 1️⃣4️⃣ Restore session

```bash
john --restore=job1
```

---

## 1️⃣5️⃣ Status

```bash
john --status
```

---

## 1️⃣6️⃣ Multi-CPU

h
john --fork=4 hash.txt




## 1️⃣7️⃣ Stop cracking


Ctrl + C


## 1️⃣8️⃣ Linux password file (lab VM)


sudo unshadow /etc/passwd /etc/shadow > crack.txt
john crack.txt
john --show crack.txt


## 1️⃣9️⃣ Help


john --help