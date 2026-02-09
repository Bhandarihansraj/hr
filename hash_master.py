#!/usr/bin/env python3
import hashlib, hmac, crypt, os, sys

# =============================
# Banner
# =============================
def banner():
    print("=" * 70)
    try:
        with open("/etc/os-release") as f:
            osname = "Kali Linux" if "kali" in f.read().lower() else "Linux"
    except:
        osname = "Linux"
    print(f" HASH MASTER v2 | {osname} | Create • Detect • Verify ")
    print("=" * 70)

# =============================
# Hash Detection
# =============================
def detect_hash(h):
    h = h.strip()
    if h.startswith("$2"): return "bcrypt"
    if h.startswith("$6$"): return "SHA512-crypt"
    if h.startswith("$5$"): return "SHA256-crypt"
    l = len(h)
    return {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }.get(l, "Unknown")

# =============================
# Create Hashes
# =============================
def create_hashes(text):
    b = text.encode()
    return {
        "MD5": hashlib.md5(b).hexdigest(),
        "SHA1": hashlib.sha1(b).hexdigest(),
        "SHA256": hashlib.sha256(b).hexdigest(),
        "SHA512": hashlib.sha512(b).hexdigest(),
        "bcrypt": crypt.crypt(text, crypt.mksalt(crypt.METHOD_BLOWFISH)),
        "SHA512-crypt": crypt.crypt(text, crypt.mksalt(crypt.METHOD_SHA512)),
        "HMAC-SHA256": hmac.new(b"secretkey", b, hashlib.sha256).hexdigest()
    }

# =============================
# Verify Hash
# =============================
def verify(password, hashval):
    algo = detect_hash(hashval)
    p = password.encode()
    if algo == "MD5": return hashlib.md5(p).hexdigest() == hashval
    if algo == "SHA1": return hashlib.sha1(p).hexdigest() == hashval
    if algo == "SHA256": return hashlib.sha256(p).hexdigest() == hashval
    if algo == "SHA512": return hashlib.sha512(p).hexdigest() == hashval
    if algo in ["bcrypt","SHA512-crypt","SHA256-crypt"]:
        return crypt.crypt(password, hashval) == hashval
    return False

# =============================
# File Hashing
# =============================
def hash_file(path):
    algos = ["md5","sha1","sha256","sha512"]
    with open(path,"rb") as f:
        data = f.read()
    for a in algos:
        h = hashlib.new(a)
        h.update(data)
        print(f"{a.upper():8} : {h.hexdigest()}")

# =============================
# Menu
# =============================
def menu():
    print("""
1. Create hashes from text
2. Detect hash type
3. Verify hash
4. Hash a file
5. Export hash for JTR
0. Exit
""")

# =============================
# Main
# =============================
def main():
    banner()
    while True:
        menu()
        c = input("Select: ").strip()

        if c == "1":
            t = input("Text: ")
            for k,v in create_hashes(t).items():
                print(f"{k:14} : {v}")

        elif c == "2":
            h = input("Hash: ")
            print("Detected:", detect_hash(h))

        elif c == "3":
            p = input("Password: ")
            h = input("Hash: ")
            print("MATCH" if verify(p,h) else "NO MATCH")

        elif c == "4":
            f = input("File path: ")
            if os.path.exists(f): hash_file(f)
            else: print("File not found")

        elif c == "5":
            h = input("Hash: ")
            with open("hash_jtr.txt","w") as f:
                f.write(h+"\n")
            print("Saved → hash_jtr.txt")

        elif c == "0":
            sys.exit()

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
