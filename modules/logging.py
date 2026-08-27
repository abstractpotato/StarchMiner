import datetime

version = "StarchMiner-v3.0"
colors = {
    "error": '\033[31m',
    "success": '\033[32m',
    "log": '\033[33m',
    "reset": '\033[0m'
}

def log(msg, status="log"):
    log_color = colors[status]
    date = datetime.datetime.now()
    print(f'{colors["reset"]}[{version}][{date}] {log_color}{msg}{colors["reset"]}')