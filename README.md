# Address Name System (ANS) for Naruno
ANS is a decentralized system that maps blockchain addresses to dynamic IPs, making it easy to access servers with changing IP addresses. With ANS, you can access your server by using your unique blockchain address instead of constantly searching for its changing IP address.

## Features
- Decentralized system
- Secure communication between nodes
- Fast and easy to use
- Maps blockchain addresses to dynamic IPs
- Uses encryption to protect sensitive information

## Installation
You can install ANS by cloning the GitHub repository:

```console
pip3 install address_name_system
```

## Usage

*If you want to use address_name_system you must to use Naruno. For now please checkout the [Baklava Testnet](https://naruno.org/baklava-testnet/).

Getting address of client and server:
```console
narunocli -pw
```

### Server
For accessing your dynamic IPs over blockchain you should create a address_name_system and giving trusted user addresses.

```python
from address_name_system import ans

my_ans_server = ans("MyNarunoPass")

my_ans_server.set_encrypt_key("mystrongencrypt_key")

my_ans_server.add_user("client_address")

my_ans_server.run()
```

also you can use in command line:
```console	
ans --password MyNarunoPass --encrypt_key "mystrongencrypt_key" --trusted_users ["client_address"] run
```

### Client
To use ANS, you can call the ans.ip function with your blockchain address as the parameter:

```python
from address_name_system import ans

my_ans_client = ans("MyNarunoPass")

ip_address = my_ans_client.ip("server_address", "mystrongencrypt_key")

print(ip_address)

my_ans_client.close()
```

also you can use in command line:
```console	
ans --password "MyNarunoPass" ip "server_address" "mystrongencrypt_key"
```


This will return the dynamic IP address associated with your blockchain address.

## Contributing
Contributions to ANS are welcome! If you have any suggestions or find a bug, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and create a pull request.

## License
ANS is released under the MPL-2.0 License.
