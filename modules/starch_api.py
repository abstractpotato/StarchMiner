import requests, json

host = "https://api.starch.one"

def get_miner_snapshot(miner_id):
    r = requests.get(f"{host}/miners/{miner_id}")
    return json.loads(r.text)
    
def submit_blocks(blocks):
    data = {"blocks": blocks}
    r = requests.post(f"{host}/submit_blocks", json=data)
    return json.loads(r.text)
    
def get_mempool():
    r = requests.get(f"{host}/pending_blocks")
    return json.loads(r.text)["blocks"]

def get_last_block():
    r = requests.get(f"{host}/blockchain/last_block")
    return json.loads(r.text)

def get_block(block_id):
    r = requests.get(f"{host}/blockchain/id/{block_id}")
    return json.loads(r.text)

def get_last_hash():
    r = requests.get(f"{host}/blockchain/last_hash")
    return json.loads(r.text)["hash"]
    
def get_company_miners(company_id):
    r = requests.get(f"{host}/teams/{company_id}/members")
    return json.loads(r.text)["members"]
    
def get_blockchain_status():
    r = requests.get(f"{host}/blockchain/status")
    return json.loads(r.text)
    
def get_last_timestamp():
    r = requests.get(f"{host}/blockchain/last_timestamp")
    return json.loads(r.text)