Below is **ONE CLEAN SETUP GUIDE for BOTH TOOLS**
👉 **Hash Master (hash create/detect)**
👉 **JTR Pro (auto crack)**
👉 **PDF-type text**
👉 **step-wise • expert • Kali/Linux**

---

# **SETUP GUIDE: HASH MASTER + JTR PRO (KALI LINUX)**

## **Purpose**

This guide explains how to set up and use:

1. **Hash Master Tool** – create, detect, verify hashes
2. **JTR Pro Tool** – auto-detect hash, crack password, manage sessions

---

## **System Requirements**

* Kali Linux (recommended)
* Python 3.x
* John the Ripper (Jumbo version)
* Internet (for wordlists)

---

## **Step-1: Verify Kali Linux**

```bash
cat /etc/os-release
```

Expected:

```
NAME="Kali GNU/Linux"
```

---

## **Step-2: Update System**

```bash
sudo apt update && sudo apt upgrade -y
```

---

## **Step-3: Install Required Tools**

### Install Python

```bash
python3 --version
```

If missing:

```bash
sudo apt install python3 -y
```

### Install John the Ripper

```bash
sudo apt install john -y
```

Verify:

```bash
john --version
```

---

## **Step-4: Check Wordlist**

```bash
ls /usr/share/wordlists/rockyou.txt
```

If compressed:

```bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
```

---

## **Step-5: Setup Hash Master Tool**

### Create file

```bash
nano hash_master.py
```

➡ Paste **Hash Master script**

### Make executable

```bash
chmod +x hash_master.py
```

### Test run

```bash
./hash_master.py
```

Expected menu:

```
1. Create hashes from text
2. Detect hash type
3. Verify hash
4. Hash a file
5. Export hash for John
0. Exit
```

---

## **Step-6: Setup JTR Pro Tool**

### Create file

```bash
nano jtr_pro.py
```

➡ Paste **JTR Pro script**

### Make executable

```bash
chmod +x jtr_pro.py
```

### Test run

```bash
./jtr_pro.py
```

Expected banner:

```
JTR PRO – AUTO HASH DETECT & PASSWORD CRACK FRAMEWORK
```

---

## **Step-7: End-to-End Demo Workflow**

### 1️⃣ Create hash

```bash
./hash_master.py
```

Option → `1`
Text → `test123`

---

### 2️⃣ Export hash for JTR

Option → `5`
File created:

```bash
hash_jtr.txt
```

---

### 3️⃣ Crack using JTR Pro

```bash
./jtr_pro.py
```

Enter file:

```
hash_jtr.txt
```

Select:

```
2  (Dictionary attack)
```

---

### 4️⃣ Show cracked password

```
8  (Show cracked passwords)
```

Output:

```
test123
```

---

## **Directory Structure (Recommended)**

```
/hash_lab/
 ├── hash_master.py
 ├── jtr_pro.py
 ├── hash_jtr.txt
 ├── jtr_pro.log
```

---

## **Common Errors & Fix**

### John not found

```bash
sudo apt install john
```

### Permission denied

```bash
chmod +x *.py
```

### No crack result

* Try rules
* Try mask
* Password may be strong

---

## **Viva / Interview Lines**

* Hash Master handles creation & detection
* JTR Pro handles cracking & session control
* Hash cracking = comparison, not decryption
* Weak passwords break first

---

## **Conclusion**

This setup provides a complete **hash → detect → crack** workflow on Kali Linux using professional, automated tools suitable for labs, exams, and security practice.

---

If you want:

* **Final merged PDF**
* **Cover page + index**
* **Screenshots placeholders**
* **Advanced attack chaining**

Say **next** ✅
