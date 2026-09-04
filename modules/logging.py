import datetime

version = "StarchMiner-v3.1"
colors = {
    "error": '\033[31m',
    "success": '\033[32m',
    "log": '\033[33m',
    "reset": '\033[0m'
}

def log(msg, status="log", condensed=False):
    log_color = colors[status]
    date = str(datetime.datetime.now()).split(".")[0]
    if condensed:
        print(f'{colors["reset"]}[{date}]{log_color}{msg}{colors["reset"]}')
        return
    
    print(f'{colors["reset"]}[{version}][{date}]{log_color}{msg}{colors["reset"]}')