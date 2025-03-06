# Phishing Site Detector

[![GitHub stars](https://img.shields.io/github/stars/Hamim-PT/Phishing-Site-Detector?style=social)](https://github.com/Hamim-PT/Phishing-Site-Detector/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Hamim-PT/Phishing-Site-Detector?style=social)](https://github.com/Hamim-PT/Phishing-Site-Detector/network)
[![GitHub license](https://img.shields.io/github/license/Hamim-PT/Phishing-Site-Detector)](https://github.com/Hamim-PT/Phishing-Site-Detector/blob/main/LICENSE)

## 📌 About
The **Phishing Site Detector** is a Python-based tool that helps users identify potential phishing websites by analyzing key indicators such as:
- Suspicious URL patterns
- HTTPS security
- Domain age
- Blacklist status (Google Safe Browsing API)

This project features a **Graphical User Interface (GUI)** built with **Tkinter** for easy interaction.

## 🚀 Features
✅ Detects phishing indicators in URLs
✅ Checks if the site uses HTTPS
✅ Analyzes domain age to detect newly created sites
✅ Uses Google Safe Browsing API for blacklist status
✅ Provides a **simple GUI** for ease of use

## 🛠️ Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Install Dependencies
```bash
pip install requests whois tkinter
```

### Clone the Repository
```bash
git clone https://github.com/Hamim-PT/Phishing-Site-Detector.git
cd Phishing-Site-Detector
```

## 🎯 Usage
Run the script with:
```bash
python phishing_detector.py
```

### Steps:
1. Enter the URL you want to check.
2. Click the "Check" button.
3. View the analysis results.

## 📌 API Configuration
This tool uses **Google Safe Browsing API** to check blacklisted URLs. To set up your API key:
1. Obtain a free API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Replace `api_key` in `check_blacklist(url)` with your own API key.

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Added a new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📞 Contact
- **GitHub:** [@Hamim-PT](https://github.com/Hamim-PT)
- **LinkedIn:** [Hamim-PT](https://www.linkedin.com/in/hamim-pt/)

---
⭐ **If you find this project useful, please give it a star!** ⭐

