<h1 align="center">🛰️ IP-TRACER PRO - ULTIMATE EDITION</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-orange?style=for-the-badge">
</p>

<p align="center">
  <b>A professional-grade OSINT tool for precise IP Geolocation and Network Port Analysis.</b><br>
  <i>Developed for cybersecurity enthusiasts and ethical hackers.</i>
</p>

---

### 🚀 Key Features
- [x] **Real-time IP Tracing:** Fetch Country, City, ISP, and Organization details.
- [x] **Integrated Port Scanner:** Scan common ports for vulnerability assessment.
- [x] **New Bold UI:** Aggressive red-themed terminal interface.
- [x] **Data Logging:** Automatically save scan results to `results.txt`.
- [x] **Optimized for Termux:** Lightweight and lightning-fast execution.

---

### 📥 Installation & Usage
```bash
# Update and install dependencies
pkg update && pkg upgrade -y
pkg install python git -y

# Clone the repository
git clone [https://github.com/dead-body-16/IP-Tracer.git](https://github.com/dead-body-16/IP-Tracer.git)

# Enter directory
cd IP-Tracer

# Install required library
pip install requests

# Run the tool
python trace.py