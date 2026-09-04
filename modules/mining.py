import modules.starch_api as api
from modules.logging import log
from time import sleep
from random import randint
from hashlib import sha256
from json import loads

# helper functions =============================================================

def get_color():
    random_number = randint(0, 16777215)
    hex_number = str(hex(random_number))
    return '#' + hex_number[2:]

def solve(last_hash, miner_id, color="random"):
    if color == "random":
        color = get_color()
    string = f'{last_hash} {miner_id} {color}'
    new_hash = sha256(string.encode()).hexdigest()
    return {"hash": new_hash, "miner_id": miner_id, "color": color}

def get_company_miners(companies=[]):
    miners = []
    for x in companies:
        temp_miners = api.get_company_miners(x.upper())
        log(f"loading {len(temp_miners)} miners from '{x.upper()}'")
        miners = miners + temp_miners
    return miners

def get_mempool_attendance(mempool):
    miners = []
    for x in mempool:
        miners.append(x["miner_id"])
    return miners

def get_config_data(file_path):
    try:
        file = open(file_path, "r")
        config = loads(file.read())
        return config
    except Exception as e:
        log(f'config error: {e}', "error")
        return {}

# main functions ===============================================================

def mine(miners=[], companies=[]):
    miners = miners + get_company_miners(companies)
    last_hash = api.get_last_hash()
    mempool = api.get_mempool()
    attendance = get_mempool_attendance(mempool)
    
    blocks = []
    for miner in miners:
        if miner not in attendance:
            block = solve(last_hash, miner)
            log(f"block solved for '{miner}'", "success")
            blocks.append(block)
        else:
            log(f"block exists for '{miner}'")
    
    result = api.submit_blocks(blocks)
    if len(result) == 0:
        log(f"blocks submitted: {len(result)}")
    else:
        log(f"blocks submitted: {len(result)}", "success")
        
def mine_loop(miners=[], companies=[]):
    while True:
        try:
            last_timestamp = api.get_last_timestamp()
            status = api.get_blockchain_status()
            log(f"blockchain tip: {last_timestamp['block_id']}")
            log(f"blockchain halvings: {status['halving_count']}")
            log(f"blockchain progress: {status['progress']:,}/215,000")
            log(f"blockchain rewards: {status['rewards']:,} STRCH")
            
            mine(miners, companies)
            wait_time = last_timestamp["current_timestamp"] - last_timestamp["timestamp"] - 5
            if wait_time > 147:
                wait_time = 5
            log(f"waiting {wait_time}s for the next block...")
            sleep(wait_time)
        except Exception as e:
            log(f'Error: {e}', "error") 
    
def mine_config(file_path):
    while True:
        log(f"loading from '{file_path}'")
        config = get_config_data(file_path)
        miners = []
        companies = []
        if "miners" in config:
            miners = config["miners"]
        if "companies" in config:
            companies = config["companies"]

        try:
            last_timestamp = api.get_last_timestamp()
            status = api.get_blockchain_status()
            log(f"blockchain tip: {last_timestamp['block_id']}")
            log(f"blockchain halvings: {status['halving_count']}")
            log(f"blockchain progress: {status['progress']:,}/215,000")
            log(f"blockchain rewards: {status['rewards']:,} STRCH")
            
            mine(miners, companies)
            wait_time = last_timestamp["current_timestamp"] - last_timestamp["timestamp"] - 5
            if wait_time > 147:
                wait_time = 5
            log(f"waiting {wait_time}s for the next block...")
            sleep(wait_time)
        except Exception as e:
            log(f'Error: {e}', "error") 
    