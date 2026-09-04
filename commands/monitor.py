import modules.starch_api as api
from modules.logging import log
from time import sleep

def monitor_help():
    print("-------------------------------------------------------------------")
    print("# can use 'mt' instead of start")
    print("monitor -> view the blockchain")
    # print("monitor <company_id> -> view the company activity")
    # print("monitor <miner_id>   -> view miner activity")
    
def view_blockchain():
    last_hash = ""
    
    while True:
        try:
            block = api.get_last_block()
            if last_hash != block["hash"]:
                last_hash = block["hash"]
                log(block)
        except Exception as e:
            log(f'Error {e}', "error")
        sleep(14.7)
        
def monitor_cmd(cmd):
    if len(cmd) == 0:
        view_blockchain()
        return
    