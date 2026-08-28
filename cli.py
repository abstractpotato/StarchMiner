from commands.miner import miner_cmd, miner_help
from commands.company import company_cmd, company_help
from commands.start import start_cmd, start_help
import sys

def help_cmd(cmd=[]):
    print("help -> help commands")
    print("h -> help commands")
    start_help()
    miner_help()
    company_help()

commands = {}
commands["h"] = help_cmd
commands["help"] = help_cmd
commands["s"] = start_cmd
commands["start"] = start_cmd
commands["m"] = miner_cmd
commands["miner"] = miner_cmd
commands["c"] = company_cmd
commands["company"] = company_cmd

cmd = sys.argv[1:]

if len(cmd) == 0:
    help_cmd()
    exit()

if cmd[0] in commands:
    commands[cmd[0]](cmd[1:])
    exit()
    
help_cmd()