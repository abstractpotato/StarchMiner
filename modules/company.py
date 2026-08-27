from modules.mining import mine_loop, get_company_miners

def company_help():
    print("-------------------------------------------------------------------")
    print("# can use 'c' instead of company")
    print("company mine <company_ids> -> mine all members of these companies")
    
    
    
def company_cmd(cmd):
    if len(cmd) == 0:
        print("- no company command chosen -")
        company_help()
        return
        
    if cmd[0] == "mine":    
        mine_loop(companies=cmd[1:])