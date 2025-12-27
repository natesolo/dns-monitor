# DNS Monitoring Tool (Python)

# Overview
This project is a Python-based DNS monitoring tool designed to detect suspicious DNS activity using behavioral indicators such as domain entropy, query frequency, and high risk domains.

The tool observes DNS queries and generates alerts when activity matches common indicators associated with malware command-and-control or domain generation algorithms (DGA).

## Features
- Passive DNS monitoring using packet capture
- Rule-based detection engine
- High-entropy domain detection
- Beaconing and frequency analysis
- Suspicious TLD identification
- Alert logging

## Architecture
DNS Traffic → Capture Engine → Detection Logic → Alerts

## Usage

### Test Mode (Recommended)
Test mode simulates DNS traffic and works on all operating systems.

```bash to run the code
python3 main.py

```force traffic using dig
examples:
dig google.com @8.8.8.8
dig reddit.com @8.8.8.8

