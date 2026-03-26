# Network Scanner

A Python-based network scanning tool that scans a target network using `nmap`, parses results, and stores structured output in CSV and JSON formats.

---

## 🚀 Features

* Network discovery using `nmap -sn`
* **Port scanning** (customizable / full range)
* **Service detection** using `nmap -P`
* IP validation using `ipaddress`
* CLI interface using `argparse`
* Execution of system commands using `subprocess`
* Structured output generation:

  * CSV
  * JSON
* Dynamic file naming based on target network
* Centralized logging system
* Clean modular architecture (`scanner.py`, `utils.py`, `logger.py`)

---

## 🛠️ Technologies Used

* Python 3
* subprocess
* ipaddress
* argparse
* logging
* csv
* json
* os
* Nmap

---

## 📁 Project Structure

```
network_scanner/
├── scanner.py
├── utils.py
├── logger.py
├── logs/
├── results/
```

---

## ▶️ Usage

```bash
python3 scanner.py --target 192.168.56.0/24 --output results.json
```

---

## 🧠 Notes

* `nmap` must be installed on the system
* Output files are automatically generated using the target network (e.g. `192.168.56.0_24.csv`)
* Logs are currently stored in a single file inside the `logs/` directory
* Script uses system-level scanning, so results depend on network permissions and environment
* Some scans may require elevated privileges (`sudo`) for full accuracy

---

## 📌 TODO (Future Improvements)

* [ ] Package as installable CLI tool (`pip install`)
* [ ] Add per-scan log files instead of a single shared log
* [ ] Increase automation by automatically scanning network when a change is detected
* [ ] Add OS detection (`nmap -O`)
* [ ] Add banner grabbing for deeper service analysis
* [ ] Improve error handling and edge case coverage
* [ ] Add colored terminal output for better readability
* [ ] Add configuration file support (YAML/JSON)
* [ ] Add multithreading for faster scans
* [ ] Add export to additional formats (XML, HTML)
* [ ] Add unit and integration tests
* [ ] Add Docker support for portability

---

## 💡 Summary

This project demonstrates practical use of:

* system command automation
* network scanning concepts
* data parsing and structuring
* logging and CLI design

Built as part of hands-on learning in Python, Bash, and networking.
