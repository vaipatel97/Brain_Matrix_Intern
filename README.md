# Brain_Matrix_Intern

# 🛡️ Phishing Link Scanner

A lightweight Python tool that scans URLs and identifies potential phishing threats based on common patterns and domain intelligence.

## 📌 Features

- Detects **suspicious keywords** in URLs like `login`, `verify`, `update`, etc.
- Checks for:
  - Presence of IP addresses
  - URL length
  - Use of shortened URLs
  - `@` symbol in URL
  - Hyphenated domains
  - Domain age using WHOIS
- Assigns **risk levels**: Low, Moderate, or High
- Color-coded terminal output (via `colorama`)

---

## 🧠 How It Works

The script analyzes the entered URL against multiple phishing indicators and gives a **risk score**. Based on this score, the tool classifies the URL as:

- ✅ **Low Risk**
- ⚠️ **Moderate Risk**
- 🚨 **High Risk**

---

## 💻 Technologies Used

- Python 3
- `requests`
- `tldextract`
- `whois`
- `colorama`

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vaipatel97/phishing-link-scanner.git
   cd phishing-link-scanner
