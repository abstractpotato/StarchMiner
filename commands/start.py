import modules.starch_api as api
from modules.mining import mine_loop

def start_help():
    print("-------------------------------------------------------------------")
    print("# can use 's' instead of start")
    print("start <company_ids (and or) miner_ids> -> starts miners and companies")
    
def start_cmd(cmd):
    if len(cmd) == 0:
        print("- no ids in command -")
        start_help()
        return
    
    miners = []
    companies = []
    for x in cmd:
        if len(x) == 8:
            miners.append(x.upper())
        if len(x) == 6:
            companies.append(x.upper())
            
    mine_loop(miners=miners, companies=companies)
        