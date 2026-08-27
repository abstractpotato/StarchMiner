import modules.starch_api as api
from modules.mining import mine_loop

def miner_help():
    print("-------------------------------------------------------------------")
    print("# can use 'm' instead of miner")
    print("miner mine <miner_ids>  -> mine with these ids")
    print("miner <miner_id>        -> print miner miner snapshot")
    
def miner_cmd(cmd):
    if len(cmd) == 0:
        print("- no miner command chosen -")
        miner_help()
        return
    
    if len(cmd[0]) == 8:
        snapshot = api.get_miner_snapshot(cmd[0])
        # print(snapshot)
        if "name" in snapshot["profile"]:
            print(f'name: {snapshot["profile"]["name"]}')
            print(f'about me: {snapshot["profile"]["description"]}')
        print(f'daily chance: {round((1/snapshot["online"])*588*100, 4)}%')
        print(f'blocks: {snapshot["blocks"]:,}')
        print(f'balance: {snapshot["balance"]:,}')
        print(f'attendance: {len(snapshot["attendance"])}/588')
        print(f'company: {snapshot["team"]}')
        
    if cmd[0] == "mine":
        mine_loop(miners=cmd[1:])
        
    