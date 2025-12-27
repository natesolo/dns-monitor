# Entry point for the DNS monitoring tool

from detector import analyze_domain
from test_data import TEST_DOMAINS
import time

def main():
    print("Running DNS monitor in TEST MODE...")

    for domain in TEST_DOMAINS:
        analyze_domain(domain)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
