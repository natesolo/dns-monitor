# Analyzes DNS activity and assigns a risk score

from collections import defaultdict
from utils import calculate_entropy
from config import * 

# Stores how many times each domain is queried
domain_counts = defaultdict(int)

def analyze_domain(domain):
    print(f"DNS query observed: {domain}")

    # Analyze a single DNS query and determine if it's suspicious 

    score = 0
    domain = domain.lower()

    # Tracks the frequency of domain queries
    domain_counts[domain] += 1

    # Checks for excessive querying
    if domain_counts[domain] > QUERY_THRESHOLD:
        score += 15

    # Check domain entropy
    entropy = calculate_entropy(domain)
    if entropy > ENTROPY_THRESHOLD:
        score += 20

    # Check for suspicious TLDs
    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            score += 10

    # If a score exceeds alert threshold, raise alert
    if score >= ALERT_SCORE:
        generate_alert(domain, score, entropy)

def generate_alert(domain, score, entropy):
    #Write alert details to a log file

    alert_message = (
        f"[ALERT] Suspicious DNS activity detected\n"
        f"Domain: {domain}\n"
        f"Score: {score}\n"
        f"Entropy: {entropy:.2f}\n\n"
    )

    # Print alert to console
    print(alert_message)

    # Append alert to file
    with open("alerts.log", "a") as f:
        f.write(alert_message)

