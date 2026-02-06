import requests, json, time, random
from hashlib import sha256

class Miner:

    def __init__(self):
        self.host = "https://api.starch.one"
        self.company_id = ""
        self.miner_ids = []
        self.color = ""
        self.last_hash = ""

    def get_last_hash(self):
        try:
            data = json.loads(requests.get(f"{self.host}/blockchain/last_hash").text)
            return data["hash"]
        except Exception as e:
            print(e)
            return ""

    def get_company_miner_ids(self):
        try:
            data = json.loads(requests.get(f"{self.host}/teams/{self.company_id}/members").text)
            return data["members"]
        except Exception as e:
            print(e)
            return []

    def update_company_miner_ids(self):
        if self.company_id == "":
            return
        self.miner_ids = self.get_company_miner_ids()

    def solve(self, previous_hash, miner_id, color):
        string = f'{previous_hash} {miner_id} {color}'
        new_hash = sha256(string.encode()).hexdigest()
        return {"hash": new_hash, "miner_id": miner_id, "color": color}

    def get_color(self):
        if self.color != "":
            return self.color
        return f'#{random.randint(0, 0xFFFFF)}'

    def submit_blocks(self, blocks):
        print(blocks)
        try:
            data = {"blocks": blocks}
            print(json.loads(requests.post(f"{self.host}/submit_blocks", json=data).text))
        except Exception as e:
            print(e)

    def mine(self):
        self.update_company_miner_ids()
        last_hash = self.get_last_hash()
        if last_hash == "":
            return

        if self.last_hash == last_hash:
            return

        color = self.get_color()

        blocks = []
        for miner_id in self.miner_ids:
            blocks.append(self.solve(last_hash, miner_id, color))
        chunks = []
        for i in range(0, len(blocks), 100):
            chunks.append(blocks[i:i + 100])
        for chunk in chunks:
            self.submit_blocks(chunk)

        self.last_hash = last_hash
