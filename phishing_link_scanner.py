import re
import requests
import whois
import tldextract
from urllib.parse import urlparse
from colorama import init, Fore, Style

init(autoreset=True)

suspicious_keywords = ['login', 'update', 'verify', 'security', 'account', 'webscr', 'confirm']

def is_shortened_url(url):
    short_domains = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'buff.ly']
    parsed = urlparse(url)
    return parsed.netloc in short_domains

def contains_ip(url):
    ip_pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}"
    return re.match(ip_pattern, url) is not None

def get_domain_age(domain):
    try:
        domain_info = whois.whois(domain)
        if domain_info.creation_date:
            return domain_info.creation_date
    except:
        return None
    return None

def scan_url(url):
    print(f"\n🔍 Scanning URL: {url}")
    risk_score = 0

    for word in suspicious_keywords:
        if word in url.lower():
            print(Fore.YELLOW + f"⚠️ Suspicious keyword found: {word}")
            risk_score += 1

    if len(url) > 75:
        print(Fore.YELLOW + "⚠️ URL is too long.")
        risk_score += 1

    if contains_ip(url):
        print(Fore.YELLOW + "⚠️ URL contains an IP address instead of domain.")
        risk_score += 1

    if "@" in url:
        print(Fore.YELLOW + "⚠️ URL contains '@' symbol.")
        risk_score += 1

    if "-" in urlparse(url).netloc:
        print(Fore.YELLOW + "⚠️ Domain contains hyphen ('-').")
        risk_score += 1

    if is_shortened_url(url):
        print(Fore.YELLOW + "⚠️ URL uses a known shortening service.")
        risk_score += 1

    ext = tldextract.extract(url)
    domain = ext.domain + '.' + ext.suffix
    age = get_domain_age(domain)
    if age is None:
        print(Fore.YELLOW + "⚠️ Unable to verify domain age.")
        risk_score += 1
    else:
        print(Fore.GREEN + f"✅ Domain creation date: {age}")

    print()  # for clean spacing

    if risk_score >= 4:
        print(Fore.RED + Style.BRIGHT + "🚨 HIGH RISK: This link may be a phishing URL!")
    elif 2 <= risk_score < 4:
        print(Fore.YELLOW + Style.BRIGHT + "⚠️ MODERATE RISK: Be cautious!")
    else:
        print(Fore.GREEN + "✅ LOW RISK: URL seems okay (but always double-check manually).")

if __name__ == "__main__":
    test_url = input("🔗 Enter URL to scan: ")
    scan_url(test_url)
