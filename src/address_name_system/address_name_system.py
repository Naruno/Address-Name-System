from urllib.request import urlopen
import re as r
from naruno.lib.encryption import encrypt, decrypt
from naruno.apps.remote_app import Integration

import pickle
import contextlib

import time
import fire

class ans:
    command_line = False
    def __init__(self, password, encrypt_key=None, trusted_users=[], self_ip_cache_time=3600, ip_cache_time=360, port=8000):
        self.encrypt_key = encrypt_key
        self.trusted_users = trusted_users
        self.integration = Integration("ANS", password=password, port=port)
        self.last_self_ip_time = 0
        self.self_ip_cache_time = self_ip_cache_time
        self.last_ip_time = []
        self.ip_cache_time = ip_cache_time
        self.self_the_ip = None

        self.load_cache()
    
    def self_self_the_ip_save(self):
        with open("self_the_ip.txt", "wb") as f:
            pickle.dump(self.self_the_ip, f)
    def self_self_the_ip_load(self):
        with open("self_the_ip.txt", "rb") as f:
            self.self_the_ip = pickle.load(f)

    def self_ip_cache_time_save(self):
        with open("self_ip_cache_time.txt", "wb") as f:
            pickle.dump(self.self_ip_cache_time, f)
    def self_ip_cache_time_load(self):
        with open("self_ip_cache_time.txt", "rb") as f:
            self.self_ip_cache_time = pickle.load(f)

    def last_ip_time_save(self):
        with open("last_ip_time.txt", "wb") as f:
            pickle.dump(self.last_ip_time, f)
    def last_ip_time_load(self):
        with open("last_ip_time.txt", "rb") as f:
            self.last_ip_time = pickle.load(f)

    def save_cache(self):
        self.self_self_the_ip_save()
        self.self_ip_cache_time_save()
        self.last_ip_time_save()

    def load_cache(self):
        with contextlib.suppress(Exception):
            self.self_self_the_ip_load()
            self.self_ip_cache_time_load()
            self.last_ip_time_load()
    
    @property
    def self_ip(self):
        if time.time() - self.last_self_ip_time > self.self_ip_cache_time:
            self.last_self_ip_time = time.time()
            self.self_the_ip = encrypt(r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(str(urlopen('http://checkip.dyndns.com/').read())).group(1), self.encrypt_key)
            self.save_cache()
            return self.self_the_ip
        else:
            return self.self_the_ip
    
    def ip(self, user, encrypt_key):
        for each in self.last_ip_time:
            if each[0] == user:
                if time.time() - each[2] < self.ip_cache_time:
                    if ans.command_line:
                        self.close()                    
                    return each[1]

        self.integration.send("yourip", "hi", user)

        while True:
            data = self.integration.get()
            if data != []:
                for each in data:
                    if each["fromUser"] == user:
                        the_ip = decrypt(each["data"]["app_data"], encrypt_key)
                        self.last_ip_time.append([user, the_ip , time.time()])
                        self.save_cache()
                        if ans.command_line:
                            self.close()
                        return the_ip
            time.sleep(5)


    def set_encrypt_key(self, encrypt_key):
        self.encrypt_key = encrypt_key
    
    def add_user(self, user):
        self.trusted_users.append(user)

    def run(self):
        while True:
            data = self.integration.get()
            if data != []:
                for each in data:
                    if each["fromUser"] in self.trusted_users:
                        self.integration.send("myip", self.self_ip, each["fromUser"])
            time.sleep(5)

    def close(self):
        self.integration.close()

def main():
    ans.command_line = True
    fire.Fire(ans)