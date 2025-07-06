# 🧨 Ransomware Simulator (Educational Project)

This is an **educational simulation of a ransomware attack**, built using Python. It demonstrates how ransomware typically encrypts files and leaves a ransom note demanding payment — **without causing any real damage**.

---

## 🔐 What It Does

- Scans a target folder for common file types (e.g., `.txt`, `.docx`)
- Encrypts the content using XOR cipher
- Deletes original files
- Generates a ransom note (`README.txt`) with a fake warning message

---

## 🎥 Demo Video

▶️ [Click to Watch Ransomware Simulator in Action](https://drive.google.com/file/d/1FtLpk2YpAL9QsXELrB1u86dzzBjybJFJ/view?usp=drive_link)

---

## 📸 Screenshots

### 1. Ransomware Execution Output
![Ransomware Output](ransom_note.png.png)

### 2. Generated Ransom Note
![Ransom Note](ransom_output1.png.png)

---

## ⚠️ Disclaimer

> 🚫 This project is strictly for **educational purposes only**.  
> ❌ It does not spread, infect, or harm any files outside of a demo folder.  
> 🔐 Do not use it for malicious activities under any circumstances.

---

## 🛠️ Technologies Used

- Python 3
- File I/O operations
- XOR encryption (for demo)
- Terminal-based simulation

---

## 👨‍💻 Author

**Soham Pramod Tayade**  
RISE Internship – Cybersecurity Domain  
GitHub: [@Dozkiller04](https://github.com/Dozkiller04)

---


## 📦 How to Run

```bash
# Clone the repo
git clone https://github.com/Dozkiller04/Ransomware-Simulator.git
cd Ransomware-Simulator

# Run the simulator (BE CAREFUL – use test folder only)
python ransomware.py
