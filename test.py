from address_name_system import ans

my_ans_server = ans("password")

my_ans_server.set_encrypt_key("mystrongencrypt_key")

my_ans_server.add_user("55de207a538855b4da2d60325e8afadc3b3caa04")

my_ans_server.run()