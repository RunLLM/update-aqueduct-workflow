import argparse
import requests
import subprocess
import sys

def get_server_version(server_address: str, api_key: str, use_https: bool) -> str:
    protocol = "https" if use_https else "http"
    address = "%s://%s/api/version" % (protocol, server_address)

    r = requests.get(address, headers={"api-key": api_key})
    if r.ok:
        return r.json()['version']
    else:
        print(r.json()['error'])
        sys.exit(1)

def install(version: str) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", ("aqueduct-sdk==%s" % version)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server_address", required=True)
    parser.add_argument("-a", "--api_key", required=True)
    args = parser.parse_args()

    try:
        version = get_server_version(args.server_address, args.api_key, use_https=True)
    except:
        version = get_server_version(args.server_address, args.api_key, use_https=False)

    print("Installing Aqueduct SDK version %s" % version)
    install(version)