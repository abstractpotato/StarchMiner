from modules.database import Database

database = Database("blockchain")
database.execute('CREATE TABLE blockchain (id int, data text)')

def get_block_count():
    query = 'SELECT COUNT(*) FROM blockchain'
    return database.execute(query)
    
def get_block(block_id):
    query = 'SELECT * FROM blockchain WHERE id=?'
    return database.execute(query, (block_id,))
    
def add_block(block):
    block_id = block["block_id"]
    data = dumps(block, separators=(',', ':'))
    query = 'INSERT INTO blockchain VALUES (?,?)'
    database.execute(query, (block_id, data))