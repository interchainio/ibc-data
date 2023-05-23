import csv
import requests

chains = [
{
      "name": "8ball",
      "path": "/v1/mainnet/8ball"
    },
    {
      "name": "acrechain",
      "path": "/v1/mainnet/acrechain"
    },
    {
      "name": "agoric",
      "path": "/v1/mainnet/agoric"
    },
    {
      "name": "aioz",
      "path": "/v1/mainnet/aioz"
    },
    {
      "name": "akash",
      "path": "/v1/mainnet/akash"
    },
    {
      "name": "arkh",
      "path": "/v1/mainnet/arkh"
    },
    {
      "name": "assetmantle",
      "path": "/v1/mainnet/assetmantle"
    },
    {
      "name": "aura",
      "path": "/v1/mainnet/aura"
    },
    {
      "name": "axelar",
      "path": "/v1/mainnet/axelar"
    },
    {
      "name": "bandchain",
      "path": "/v1/mainnet/bandchain"
    },
    {
      "name": "beezee",
      "path": "/v1/mainnet/beezee"
    },
    {
      "name": "bitcanna",
      "path": "/v1/mainnet/bitcanna"
    },
    {
      "name": "bitsong",
      "path": "/v1/mainnet/bitsong"
    },
    {
      "name": "bluzelle",
      "path": "/v1/mainnet/bluzelle"
    },
    {
      "name": "bostrom",
      "path": "/v1/mainnet/bostrom"
    },
    {
      "name": "canto",
      "path": "/v1/mainnet/canto"
    },
    {
      "name": "carbon",
      "path": "/v1/mainnet/carbon"
    },
    {
      "name": "cerberus",
      "path": "/v1/mainnet/cerberus"
    },
    {
      "name": "chain4energy",
      "path": "/v1/mainnet/chain4energy"
    },
    {
      "name": "cheqd",
      "path": "/v1/mainnet/cheqd"
    },
    {
      "name": "chihuahua",
      "path": "/v1/mainnet/chihuahua"
    },
    {
      "name": "chimba",
      "path": "/v1/mainnet/chimba"
    },
    {
      "name": "chronicnetwork",
      "path": "/v1/mainnet/chronicnetwork"
    },
    {
      "name": "comdex",
      "path": "/v1/mainnet/comdex"
    },
    {
      "name": "commercionetwork",
      "path": "/v1/mainnet/commercionetwork"
    },
    {
      "name": "coreum",
      "path": "/v1/mainnet/coreum"
    },
    {
      "name": "cosmoshub",
      "path": "/v1/mainnet/cosmoshub"
    },
    {
      "name": "crescent",
      "path": "/v1/mainnet/crescent"
    },
    {
      "name": "cronos",
      "path": "/v1/mainnet/cronos"
    },
    {
      "name": "cryptoorgchain",
      "path": "/v1/mainnet/cryptoorgchain"
    },
    {
      "name": "cudos",
      "path": "/v1/mainnet/cudos"
    },
    {
      "name": "decentr",
      "path": "/v1/mainnet/decentr"
    },
    {
      "name": "desmos",
      "path": "/v1/mainnet/desmos"
    },
    {
      "name": "dig",
      "path": "/v1/mainnet/dig"
    },
    {
      "name": "dyson",
      "path": "/v1/mainnet/dyson"
    },
    {
      "name": "echelon",
      "path": "/v1/mainnet/echelon"
    },
    {
      "name": "emoney",
      "path": "/v1/mainnet/emoney"
    },
    {
      "name": "ethos",
      "path": "/v1/mainnet/ethos"
    },
    {
      "name": "evmos",
      "path": "/v1/mainnet/evmos"
    },
    {
      "name": "fetchhub",
      "path": "/v1/mainnet/fetchhub"
    },
    {
      "name": "firmachain",
      "path": "/v1/mainnet/firmachain"
    },
    {
      "name": "galaxy",
      "path": "/v1/mainnet/galaxy"
    },
    {
      "name": "genesisl1",
      "path": "/v1/mainnet/genesisl1"
    },
    {
      "name": "gitopia",
      "path": "/v1/mainnet/gitopia"
    },
    {
      "name": "gravitybridge",
      "path": "/v1/mainnet/gravitybridge"
    },
    {
      "name": "idep",
      "path": "/v1/mainnet/idep"
    },
    {
      "name": "impacthub",
      "path": "/v1/mainnet/impacthub"
    },
    {
      "name": "imversed",
      "path": "/v1/mainnet/imversed"
    },
    {
      "name": "injective",
      "path": "/v1/mainnet/injective"
    },
    {
      "name": "irisnet",
      "path": "/v1/mainnet/irisnet"
    },
    {
      "name": "jackal",
      "path": "/v1/mainnet/jackal"
    },
    {
      "name": "juno",
      "path": "/v1/mainnet/juno"
    },
    {
      "name": "kava",
      "path": "/v1/mainnet/kava"
    },
    {
      "name": "kichain",
      "path": "/v1/mainnet/kichain"
    },
    {
      "name": "konstellation",
      "path": "/v1/mainnet/konstellation"
    },
    {
      "name": "kujira",
      "path": "/v1/mainnet/kujira"
    },
    {
      "name": "kyve",
      "path": "/v1/mainnet/kyve"
    },
    {
      "name": "lambda",
      "path": "/v1/mainnet/lambda"
    },
    {
      "name": "likecoin",
      "path": "/v1/mainnet/likecoin"
    },
    {
      "name": "logos",
      "path": "/v1/mainnet/logos"
    },
    {
      "name": "loyal",
      "path": "/v1/mainnet/loyal"
    },
    {
      "name": "lumenx",
      "path": "/v1/mainnet/lumenx"
    },
    {
      "name": "lumnetwork",
      "path": "/v1/mainnet/lumnetwork"
    },
    {
      "name": "mars",
      "path": "/v1/mainnet/mars"
    },
    {
      "name": "mayachain",
      "path": "/v1/mainnet/mayachain"
    },
    {
      "name": "medasdigital",
      "path": "/v1/mainnet/medasdigital"
    },
    {
      "name": "meme",
      "path": "/v1/mainnet/meme"
    },
    {
      "name": "microtick",
      "path": "/v1/mainnet/microtick"
    },
    {
      "name": "migaloo",
      "path": "/v1/mainnet/migaloo"
    },
    {
      "name": "mises",
      "path": "/v1/mainnet/mises"
    },
    {
      "name": "mythos",
      "path": "/v1/mainnet/mythos"
    },
    {
      "name": "neutron",
      "path": "/v1/mainnet/neutron"
    },
    {
      "name": "noble",
      "path": "/v1/mainnet/noble"
    },
    {
      "name": "nois",
      "path": "/v1/mainnet/nois"
    },
    {
      "name": "nomic",
      "path": "/v1/mainnet/nomic"
    },
    {
      "name": "nyx",
      "path": "/v1/mainnet/nyx"
    },
    {
      "name": "octa",
      "path": "/v1/mainnet/octa"
    },
    {
      "name": "odin",
      "path": "/v1/mainnet/odin"
    },
    {
      "name": "okexchain",
      "path": "/v1/mainnet/okexchain"
    },
    {
      "name": "omniflixhub",
      "path": "/v1/mainnet/omniflixhub"
    },
    {
      "name": "onomy",
      "path": "/v1/mainnet/onomy"
    },
    {
      "name": "oraichain",
      "path": "/v1/mainnet/oraichain"
    },
    {
      "name": "osmosis",
      "path": "/v1/mainnet/osmosis"
    },
    {
      "name": "panacea",
      "path": "/v1/mainnet/panacea"
    },
    {
      "name": "passage",
      "path": "/v1/mainnet/passage"
    },
    {
      "name": "persistence",
      "path": "/v1/mainnet/persistence"
    },
    {
      "name": "planq",
      "path": "/v1/mainnet/planq"
    },
    {
      "name": "point",
      "path": "/v1/mainnet/point"
    },
    {
      "name": "provenance",
      "path": "/v1/mainnet/provenance"
    },
    {
      "name": "quasar",
      "path": "/v1/mainnet/quasar"
    },
    {
      "name": "quicksilver",
      "path": "/v1/mainnet/quicksilver"
    },
    {
      "name": "realio",
      "path": "/v1/mainnet/realio"
    },
    {
      "name": "rebus",
      "path": "/v1/mainnet/rebus"
    },
    {
      "name": "regen",
      "path": "/v1/mainnet/regen"
    },
    {
      "name": "rizon",
      "path": "/v1/mainnet/rizon"
    },
    {
      "name": "secretnetwork",
      "path": "/v1/mainnet/secretnetwork"
    },
    {
      "name": "sentinel",
      "path": "/v1/mainnet/sentinel"
    },
    {
      "name": "shareledger",
      "path": "/v1/mainnet/shareledger"
    },
    {
      "name": "shentu",
      "path": "/v1/mainnet/shentu"
    },
    {
      "name": "sifchain",
      "path": "/v1/mainnet/sifchain"
    },
    {
      "name": "sommelier",
      "path": "/v1/mainnet/sommelier"
    },
    {
      "name": "stafihub",
      "path": "/v1/mainnet/stafihub"
    },
    {
      "name": "stargaze",
      "path": "/v1/mainnet/stargaze"
    },
    {
      "name": "starname",
      "path": "/v1/mainnet/starname"
    },
    {
      "name": "stride",
      "path": "/v1/mainnet/stride"
    },
    {
      "name": "teritori",
      "path": "/v1/mainnet/teritori"
    },
    {
      "name": "terpnetwork",
      "path": "/v1/mainnet/terpnetwork"
    },
    {
      "name": "terra",
      "path": "/v1/mainnet/terra"
    },
    {
      "name": "terra2",
      "path": "/v1/mainnet/terra2"
    },
    {
      "name": "tgrade",
      "path": "/v1/mainnet/tgrade"
    },
    {
      "name": "thorchain",
      "path": "/v1/mainnet/thorchain"
    },
    {
      "name": "umee",
      "path": "/v1/mainnet/umee"
    },
    {
      "name": "unification",
      "path": "/v1/mainnet/unification"
    },
    {
      "name": "uptick",
      "path": "/v1/mainnet/uptick"
    },
    {
      "name": "vidulum",
      "path": "/v1/mainnet/vidulum"
    },
    {
      "name": "vincechain",
      "path": "/v1/mainnet/vincechain"
    },
    {
      "name": "xpla",
      "path": "/v1/mainnet/xpla"
    }
]

csv_file = "chain_data.csv"

# Open the CSV file in write mode
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Chain", "IBC Go Version", "Cosmos SDK Version", "CosmWasm Enabled", "CosmWasm Version"])

    # Iterate over the chains
    for chain in chains:
        url = f"https://chainregistry.xyz{chain['path']}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()

            codebase = data['result']['codebase']
            ibc_go_version = codebase.get('ibc_go_version')
            cosmos_sdk_version = codebase.get('cosmos_sdk_version')
            cosmwasm_enabled = codebase.get('cosmwasm_enabled')
            cosmwasm_version = codebase.get('cosmwasm_version')

            # Write the data row
            writer.writerow([
                chain["name"],
                ibc_go_version,
                cosmos_sdk_version,
                cosmwasm_enabled,
                cosmwasm_version
            ])

        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Error occurred while querying chain '{chain['name']}': {e}")

print("Data written to CSV file successfully.")
