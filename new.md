⚙️ SETUP GUIDE (TEXT – FINAL)
1️⃣ Install requirements
sudo apt update
sudo apt install john python3 -y
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

2️⃣ Setup tools
mkdir hash_lab
cd hash_lab
nano hash_master.py
nano jtr_pro.py
chmod +x *.py

3️⃣ Workflow (EXPERT)
Password
 → Hash Master (create + detect)
 → Export hash
 → JTR Pro (auto detect)
 → Dictionary → Rules → Mask → Brute
 → Show password

4️⃣ Live demo
./hash_master.py
# option 1 → create hash
# option 5 → export

./jtr_pro.py
# option 2 → crack
# option 8 → show

5️⃣ Directory structure
hash_lab/
 ├── hash_master.py
 ├── jtr_pro.py
 ├── hash_jtr.txt
 ├── jtr_pro.log