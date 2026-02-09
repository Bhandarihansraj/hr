#!/usr/bin/env python3
import os, subprocess, sys, time, shutil

SESSION="jtr_session"
LOG="jtr_pro.log"

def banner():
    print("="*70)
    print(" JTR PRO v2 | Auto Detect • Crack • Resume • Show ")
    print("="*70)

def run(cmd):
    print(f"[CMD] {cmd}")
    with open(LOG,"a") as f:
        f.write(f"[{time.ctime()}] {cmd}\n")
    subprocess.run(cmd,shell=True)

def menu():
    print("""
1. Smart auto crack
2. Dictionary (rockyou)
3. Dictionary + rules
4. Mask attack
5. Incremental brute
6. Resume session
7. Status
8. Show cracked
9. Clean session
0. Exit
""")

def main():
    if not shutil.which("john"):
        print("John not installed"); sys.exit()

    banner()
    hfile = input("Hash file: ").strip()
    if not os.path.exists(hfile):
        print("File not found"); sys.exit()

    print("[+] Auto detecting hash...")
    run(f"john {hfile}")

    while True:
        menu()
        c = input("Select: ").strip()

        if c == "1":
            run(f"john --session={SESSION} {hfile}")
        elif c == "2":
            run(f"john --session={SESSION} --wordlist=/usr/share/wordlists/rockyou.txt {hfile}")
        elif c == "3":
            run(f"john --session={SESSION} --wordlist=/usr/share/wordlists/rockyou.txt --rules {hfile}")
        elif c == "4":
            m = input("Mask: ")
            run(f"john --session={SESSION} --mask={m} {hfile}")
        elif c == "5":
            run(f"john --session={SESSION} --incremental {hfile}")
        elif c == "6":
            run(f"john --restore={SESSION}")
        elif c == "7":
            run("john --status")
        elif c == "8":
            run(f"john --show {hfile}")
        elif c == "9":
            if os.path.exists(f"{SESSION}.rec"):
                os.remove(f"{SESSION}.rec")
                print("Session cleaned")
        elif c == "0":
            sys.exit()

if __name__ == "__main__":
    main()
