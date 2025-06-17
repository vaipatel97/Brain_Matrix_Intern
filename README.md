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
   git clone https://github.com/vaipatel97/Brain_Matrix_Intern_Task1.git
   cd phishing-link-scanner
   ```
2. **Create a virtual environment (optional but recommended)**

  ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the scanner with:
  ```bash
      python phishing_link_scanner.py
  ```
  Then enter the URL when prompted:
  
  🔗 Enter URL to scan: http://secure-login.mybank.example.com/update

## 🧪 Example Output

🔍 Scanning URL: http://secure-login.mybank.example.com/update

⚠️ Suspicious keyword found: login

⚠️ Domain contains hyphen ('-')

⚠️ URL is too long.

⚠️ Unable to verify domain age.

🚨 HIGH RISK: This link may be a phishing URL!

## 🛠️ Future Improvements

GUI version with Tkinter or PyQt

Integration with VirusTotal or PhishTank API

Email and webpage link scanner

Export scan reports to PDF or HTML

## 📄 License

This project is licensed under the MIT License.

Feel free to use and modify it for educational and ethical hacking purposes.

## 🙏 Acknowledgements

Developed by Vaibhav Patel as a cybersecurity learning project.

Special thanks to the open-source Python community.










