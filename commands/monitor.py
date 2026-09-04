import modules.starch_api as api
from modules.logging import log
from time import sleep

def monitor_help():
    print("-------------------------------------------------------------------")
    print("# can use 'mt' instead of start")
    print("monitor -> view the blockchain")
    # print("monitor <company_id> -> view the company activity")
    # print("monitor <miner_id>   -> view miner activity")
    
def log_block(tip):
    full_block = api.get_block(tip)
    
    string = ""
    string += f'[tip:{tip}|' 
    string += f'hash:{full_block["hash"][:4]}...{full_block["hash"][-4:]}|'
    string += f'miner:{full_block["miner_id"]}|'
    string += f'color:{full_block["color"]}|'
    string += f'online:{len(full_block["attendance"])}]'
    log(string)
    
def view_blockchain():
    tip = 0
    
    while True:
        try:
            block = api.get_last_block()
            if block["block_id"] != tip:
                tip = block["block_id"]
                log_block(tip)
        except Exception as e:
            log(f'Error {e}', "error")
        sleep(14.7)
        
def monitor_cmd(cmd):
    if len(cmd) == 0:
        view_blockchain()
        return
    