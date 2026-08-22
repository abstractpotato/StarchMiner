import os, random, requests, json, datetime, time
from hashlib import sha256

host = "https://api.starch.one"
version = "beta v2.0"

print('\033[33m')

def clear_console():
    # return
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def fix_line(text):
    while len(text) < 41:
        text += " "
    text += "│"
    print(text)

def print_head(is_closed=True):
    clear_console()
    print(" ┌───────────────────────────────────────┐")
    fix_line(f" │ Starch Industries Miner - {version}")
    fix_line(" │ Created By: @abstractpotato")
    if is_closed:
        print(" └───────────────────────────────────────┘")

def print_status(data):
    print()
    print_head(False)
    print(" ├────────────┬──────────────────────────┤")
    fix_line(f" │ Miner ID   │ {data['miner_id']}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ Running    │ {data['hash'][0:10]}...{data['hash'][-10:]}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ Start Time │ {data['start_time'].strftime('%m/%d/%Y-%H:%M:%S')}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ Runtime    │ {data['running_time']}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ Attendance │ {data['attendance']}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ Balance    │ {data['balance']}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ Blocks     │ {data['blocks']}")
    print(" ├────────────┼──────────────────────────┤")
    fix_line(f" │ New Blocks │ {data['new_blocks']}")
    print(" └────────────┴──────────────────────────┘")

def print_err():
    print_head(False)
    print(" ├────────────┬──────────────────────────┤")
    fix_line(" │ Error      │ Network Issue")
    print(" └────────────┴──────────────────────────┘")

def get_miner_id():
    print_head()
    miner_id = input("> Enter Miner ID: ").upper()

    # Clean input
    if len(miner_id) != 8:
        print(f"Error: {miner_id} is an invalid Miner ID!")
        exit()
        return ""

    # Confirm the Miner ID is active
    try:
        r = requests.get(f"{host}/miners/{miner_id}")
        result = json.loads(r.text)
    
        if result == {}:
            print(f"Error: {miner_id} not found!")
            print("Make sure this Miner ID is activated before mining.")
            exit()
        return miner_id
    except Exception as e:
        print(e)
        exit()

def get_color():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    return '#' + hex_number[2:]

def solve(last_hash, miner_id):
    color = get_color()
    string = f'{last_hash} {miner_id} {color}'
    new_hash = sha256(string.encode()).hexdigest()
    block = {"hash": new_hash, "miner_id": miner_id, "color": color}
    return {"blocks": [block]}

def attempt(miner_id):
    result = json.loads(requests.get(f"{host}/blockchain/last_hash").text)
    s = solve(result["hash"], miner_id)
    result = json.loads(requests.post(f"{host}/submit_blocks", json=s).text)
    return result, s

def pending_block(miner_id):
    return json.loads(requests.get(f"{host}/pending_blocks/{miner_id}").text)
    
def miner_snapshot(miner_id):
    return json.loads(requests.get(f"{host}/miners/{miner_id}").text)
    
def mine(miner_id):
    start_time = datetime.datetime.now()
    block_count = 0
    current_block = {}
    miner = {}
    data = {}
    data["miner_id"] = miner_id
    data["start_time"] = start_time
    data["new_blocks"] = 0
    
    while True:
        try:
            current_time = datetime.datetime.now()
            data["running_time"] = str(current_time - start_time)[:-7]
            
            pending = pending_block(miner_id)
            
            if miner == {}:
                miner = miner_snapshot(miner_id)
                
                data["attendance"] = f'{len(miner["attendance"])}/588'
                
                if "blocks" in data:
                    if data["blocks"] < miner["blocks"]:
                        data["new_blocks"] = miner["blocks"] - data["blocks"]
                data["blocks"] = miner["blocks"]
                
                data["balance"] = f'{miner["balance"]:,}'
            
            if pending == {}:
                miner = miner_snapshot(miner_id)
                
                data["attendance"] = f'{len(miner["attendance"])}/588'
                
                if "blocks" in data:
                    if data["blocks"] < miner["blocks"]:
                        data["new_blocks"] = miner["blocks"] - data["blocks"]
                data["blocks"] = miner["blocks"]
                
                data["balance"] = f'{miner["balance"]:,}'
                  
                data["hash"] = attempt(miner_id)[1]["blocks"][0]["hash"]
            else:
                data["hash"] = pending["hash"]
                
            print_status(data)

        except Exception as e:
            print(e)
            print_err()
        time.sleep(1)

miner_id = get_miner_id()
mine(miner_id)
