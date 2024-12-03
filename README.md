# Backdoor - Python Reverse Shell

This repository contains a Python-based backdoor designed to establish a reverse shell connection from a victim machine to an attacker-controlled machine. The project is intended for educational purposes and controlled penetration testing only.

---

## Features
- Simple setup and execution.
- Configurable IP and port variables for flexibility.
- Two scripts:  
  - `listener.py`: Listens for incoming connections on the attacker's machine.  
  - `exploit.py`: Initiates the connection from the victim's machine.

---

## Usage

### 1. Modify Configuration
Edit the IP address and port variables in both **`exploit.py`** and **`listener.py`** to match your environment.

### 2. Execute the Scripts
Run the scripts on their respective machines:

#### Attacker's Machine:
Start the listener to wait for the incoming connection:
```bash
python3 listener.py
