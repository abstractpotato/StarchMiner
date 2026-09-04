import modules.starch_api as api
from modules.mining import mine_loop, mine_config

def start_help():
    print("-------------------------------------------------------------------")
    print("# can use 's' instead of start")
    print("start <companies or miners> -> starts miners and companies")
    print("start <*.json>              -> starts from config file")
    
def start_cmd(cmd):
    if len(cmd) == 0:
        print("- no ids in command -")
        start_help()
        return
    
    if ".json" in cmd[0]:
        mine_config(cmd[0])
        return
    
    miners = []
    companies = []
    for x in cmd:
        if len(x) == 8:
            miners.append(x.upper())
        if len(x) == 6:
            companies.append(x.upper())
            
    mine_loop(miners=miners, companies=companies)
        