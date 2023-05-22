import re
import requests
from bs4 import BeautifulSoup

def check_link(url, link):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    pattern = re.compile(link)
    match = re.search(pattern, str(soup))

    if match:
        return True
    else:
        return False

if __name__ == '__main__':

    # These are the links to check if they exist within the (url) repo:
    l1 = 'github.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts'
    l2 = 'github.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/controller'

    links = [l1, l2]

    # GitHub repo URLs
    urls = ['https://github.com/osmosis-labs/osmosis/blob/main/app/app.go', # Osmosis
    'https://github.com/cosmos/gaia/blob/main/app/app.go', # Gaia
    'https://github.com/scrtlabs/SecretNetwork/blob/master/app/app.go', # Secret
    'https://github.com/ovrclk/akash/blob/master/app/app.go', # Akash
    'https://github.com/axelarnetwork/axelar-core/blob/main/app/app.go', # Axelar
    'https://github.com/ixofoundation/ixo-blockchain/blob/main/app/app.go', # IXO
    'https://github.com/CosmosContracts/juno/blob/main/app/app.go', # Juno
    'https://github.com/Kava-Labs/kava/blob/master/app/app.go', # Kava
    'https://github.com/Team-Kujira/core/blob/master/app/app.go', # Kujira
    'https://github.com/OmniFlix/omniflixhub/blob/main/app/app.go', # OmniFlix
    'https://github.com/persistenceOne/persistenceCore/blob/main/app/app.go', # Persistence
    'https://github.com/provenance-io/provenance/blob/main/app/app.go', # Provenance
    'https://github.com/regen-network/regen-ledger/blob/main/app/app.go', #Regen
    'https://github.com/rizon-world/rizon/blob/master/app/app.go', # Rizon
    'https://github.com/sentinel-official/hub/blob/development/app.go', # Sen
    'https://github.com/ShentuChain/shentu/blob/master/app/app.go', # Shentu
    'https://github.com/Sifchain/sifnode/blob/master/app/app.go', # Sifchain
    'https://github.com/PeggyJV/sommelier/blob/main/app/app.go', # Sommelier
    'https://github.com/stafihub/stafihub/blob/main/app/app.go', # Stafihub
    'https://github.com/public-awesome/stargaze/blob/main/app/app.go', # Stargaze
    'https://github.com/iov-one/starnamed/blob/master/app/app.go', # Starname
    'https://github.com/Stride-Labs/stride/blob/main/app/app.go', # Stride
    'https://github.com/TERITORI/teritori-chain/blob/main/app/app.go', # Teritori
    'https://github.com/confio/tgrade/blob/main/app/app.go', # Tgrade
    'https://github.com/umee-network/umee/blob/main/app/app.go', # Umee
    'https://github.com/xpladev/xpla/blob/main/app/app.go', # XPLA
    'https://github.com/bandprotocol/chain/blob/master/app/app.go', # Band
    'https://github.com/BitCannaGlobal/bcna/blob/main/app/app.go', # BitCanna
    'https://github.com/bitsongofficial/go-bitsong/blob/main/app/app.go', # BitSong
    'https://github.com/cerberus-zone/cerberus/blob/release/v2.0.1/app/app.go', # Cerberus
    'https://github.com/comdex-official/comdex/blob/development/app/app.go', # Comdex
    'https://github.com/crescent-network/crescent/blob/main/app/app.go', # Crescent
    'https://github.com/crypto-org-chain/chain-main/blob/master/app/app.go', # Crypto.org
    'https://github.com/desmos-labs/desmos/blob/master/app/app.go', # Desmos
    'https://github.com/e-money/em-ledger/blob/develop/app.go', # Emoney
    'https://github.com/evmos/evmos/blob/main/app/app.go', # Evmos
    'https://github.com/Gravity-Bridge/Gravity-Bridge/blob/main/module/app/app.go', # Gravity bridge
    'https://github.com/irisnet/irishub/blob/master/app/app.go'] # Iris Hub

    print('checking for controller submodule'.upper())
    for url in urls:
        print(f'checking if LINK: <{l1}> is in URL: {url}: {check_link(url, l1)}')
    print()

    print('checking for 27-interchain-accounts'.upper())
    for url in urls:
        print(f'checking if LINK: <{l2}> is in URL: {url}: {check_link(url, l2)}')
    print()
    print('DONE')
