import requests
import re
import whois
import datetime
import tkinter as tk
from tkinter import messagebox

# List of suspicious keywords commonly used in phishing URLs
suspicious_keywords = ["login", "secure", "bank", "update", "verify", "account", "webscr", "paypal", "ebay", "amazon"]

# Function to check if the URL contains suspicious patterns
def check_url_patterns(url):
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True
    return False

# Function to check if the URL uses HTTPS
def check_https(url):
    return url.startswith("https://")

# Function to check domain age
def check_domain_age(url):
    try:
        domain_info = whois.whois(url)
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):  # Some domains return a list
            creation_date = creation_date[0]
        age = (datetime.datetime.now() - creation_date).days
        return age
    except:
        return -1  # Unable to fetch WHOIS info

# Function to check if the URL is blacklisted (Google Safe Browsing API)
def check_blacklist(url):
    api_key = "Enter Your API key"
    safe_browsing_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    payload = {
        "client": {
            "clientId": "yourCompany",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(safe_browsing_url, json=payload)
    return response.json() != {}

# Main function to check phishing indicators
def is_phishing(url):
    results = {
        "Suspicious Patterns": check_url_patterns(url),
        "HTTPS Secure": check_https(url),
        "Domain Age (Days)": check_domain_age(url),
        "Blacklisted": check_blacklist(url)
    }
    
    # Print results
    result_text = "\n🔍 **Phishing Site Detection Results:**\n"
    for key, value in results.items():
        result_text += f"{key}: {value}\n"

    # Final decision
    if results["Suspicious Patterns"] or results["Blacklisted"] or (results["Domain Age (Days)"] < 30):
        result_text += "\n⚠️ **WARNING: This site might be a phishing site! Proceed with caution.**"
    else:
        result_text += "\n✅ **This site appears to be safe.**"
    
    return result_text

# GUI Application
class PhishingDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Site Detector")
        
        self.label = tk.Label(root, text="Enter URL to check:")
        self.label.pack(pady=10)
        
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="Check", command=self.check_url)
        self.check_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", justify=tk.LEFT)
        self.result_label.pack(pady=10)
    
    def check_url(self):
        url = self.url_entry.get()
        if url:
            result = is_phishing(url)
            self.result_label.config(text=result)
        else:
            messagebox.showwarning("Input Error", "Please enter a URL to check.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingDetectorApp(root)
    root.mainloop()
