import argparse
from . import danfossclient

def main():
    parser = argparse.ArgumentParser("pydanfossair")
    parser.add_argument("--host", action="store")

    args = parser.parse_args()

    client = danfossclient.DanfossClient(args.host)

    result = client.read_all()

    for key in result.keys():
        print("{0}: {1}".format(key, result.get(key)))

if __name__ == "__main__":
    main()
