from address_name_system import ans

my_ans_client = ans("password", port=7776)


ip_address = my_ans_client.ip("86e9a2454e2d2bd12f56ef37e39d026608013e72", "mystrongencrypt_key")

print(ip_address)

my_ans_client.close()