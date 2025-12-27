# Thresholds and settings
# config.py
# Configuration file for detection thresholds and settings

# A list of suspicious domains abused by malware
SUSPICIOUS_TLDS = [".xyz", ".zip", ".mov", ".com", ".win"]

# Threshold for detecting DGA-style domains
ENTROPY_THRESHOLD = 3.8

# Number of DNS queries to the same domain before flagging
QUERY_THRESHOLD = 40

# Score required to trigger an alert
ALERT_SCORE = 40