import requests
import csv

urls = ['https://github.com/osmosis-labs/osmosis/blob/main/go.mod',
        'https://github.com/scrtlabs/SecretNetwork/blob/master/go.mod',
        'https://github.com/Stride-Labs/stride/blob/v5.1.1/go.mod',
        'https://github.com/cosmos/gaia/blob/main/go.mod',
        'https://github.com/akash-network/node/blob/master/go.mod',
        'https://github.com/axelarnetwork/axelar-core/blob/main/go.mod',
        'https://github.com/ixofoundation/ixo-blockchain/blob/main/go.mod',
        'https://github.com/CosmosContracts/juno/blob/main/go.mod',
        'https://github.com/Kava-Labs/kava/blob/master/go.mod',
        'https://github.com/Team-Kujira/core/blob/master/go.mod',
        'https://github.com/OmniFlix/omniflixhub/blob/main/go.mod',
        'https://github.com/persistenceOne/persistenceCore/blob/main/go.mod',
        'https://github.com/provenance-io/provenance/blob/main/go.mod',
        'https://github.com/regen-network/regen-ledger/blob/main/go.mod',
        'https://github.com/rizon-world/rizon/blob/master/go.mod',
        'https://github.com/sentinel-official/hub/blob/development/go.mod',
        'https://github.com/shentufoundation/shentu/blob/master/go.mod',
        'https://github.com/Sifchain/sifnode/blob/master/go.mod',
        'https://github.com/PeggyJV/sommelier/blob/main/go.mod',
        'https://github.com/stafihub/stafihub/blob/main/go.mod',
        'https://github.com/public-awesome/stargaze/blob/main/go.mod',
        'https://github.com/iov-one/starnamed/blob/master/go.mod',
        'https://github.com/TERITORI/teritori-chain/blob/main/go.mod',
        'https://github.com/confio/tgrade/blob/main/go.mod',
        'https://github.com/umee-network/umee/blob/main/go.mod',
        'https://github.com/xpladev/xpla/blob/main/go.mod',
        'https://github.com/bandprotocol/chain/blob/master/go.mod',
        'https://github.com/BitCannaGlobal/bcna/blob/main/go.mod',
        'https://github.com/bitsongofficial/go-bitsong/blob/main/go.mod',
        'https://github.com/cerberus-zone/cerberus/blob/release/v2.0.1/go.mod',
        'https://github.com/comdex-official/comdex/blob/development/go.mod',
        'https://github.com/crescent-network/crescent/blob/main/go.mod',
        'https://github.com/crypto-org-chain/chain-main/blob/master/go.mod',
        'https://github.com/desmos-labs/desmos/blob/master/go.mod',
        'https://github.com/e-money/em-ledger/blob/develop/go.mod',
        'https://github.com/evmos/evmos/blob/main/go.mod',
        'https://github.com/Gravity-Bridge/Gravity-Bridge/blob/main/module/go.mod',
        'https://github.com/irisnet/irishub/blob/master/go.mod',
        'https://github.com/mars-protocol/hub/blob/main/go.mod',
        'https://github.com/AssetMantle/modules/blob/master/go.mod',
        'https://github.com/ingenuity-build/quicksilver/blob/main/go.mod',
        'https://github.com/terra-money/core/blob/main/go.mod',
        'https://github.com/KiFoundation/hub/blob/master/go.mod',
        'https://github.com/medibloc/panacea-core/blob/main/go.mod',
        'https://github.com/Konstellation/kn-sdk/blob/master/go.mod',
        'https://github.com/fetchai/fetchd/blob/master/go.mod',
        'https://github.com/Canto-Network/Canto/blob/main/go.mod',
        'https://github.com/InjectiveLabs/sdk-go/blob/master/go.mod',
        'https://github.com/cybercongress/go-cyber/blob/main/go.mod',
        'https://github.com/ChihuahuaChain/chihuahua/blob/main/go.mod',
        'https://github.com/Agoric/agoric-sdk/blob/master/go.mod',
        'https://github.com/likecoin/likecoin-chain/blob/master/go.mod',
        'https://github.com/cheqd/cheqd-node/blob/main/go.mod',
        'https://github.com/commercionetwork/commercionetwork/blob/master/go.mod',
        'https://github.com/lum-network/chain/blob/master/go.mod',
        'https://github.com/CudoVentures/cudos-node/blob/cudos-master/go.mod',
        'https://github.com/Decentr-net/decentr/blob/master/go.mod',
        'https://github.com/vidulum/mainnet/blob/main/go.mod',
        'https://github.com/notional-labs/dig/blob/master/go.mod',
        'https://github.com/Altered-Carbon-DAO/alteredcarbon/blob/main/go.mod',
        'https://github.com/AIOZNetwork/ethermint/blob/fe02a4cd59d31654bb03241c4bdc9e7979f8de9a/go.mod#L15',
        'https://github.com/vincadian/arkh-blockchain/blob/master/go.mod',
        'https://github.com/bze-alphateam/bze/blob/main/go.mod',
        'https://github.com/ChronicNetwork/cht/blob/main/go.mod',
        'https://github.com/echelonfoundation/echelon/blob/main/go.mod',
        'https://github.com/FirmaChain/firmachain/blob/master/go.mod',
        'https://github.com/galaxynetwork/galaxy/blob/main/go.mod',
        'https://github.com/alpha-omega-labs/genesisd/blob/23d20d043bc08dc2cb7445583756d705e2a70c49/go.mod#L8',
        'https://github.com/IDEP-network/ion/blob/main/go.mod',
        'https://github.com/LambdaIM/lambdavm/blob/main/go.mod',
        'https://github.com/cryptonetD/lumenx/blob/main/go.mod',
        'https://github.com/memecosmos/meme/blob/main/go.mod',
       'https://github.com/ODIN-PROTOCOL/odin-core/blob/master/go.mod',
       'https://github.com/oraichain/orai/blob/master/go.mod',
       'https://github.com/pointnetwork/point-chain-ignition/blob/main/point/go.mod',
       'https://github.com/rebuschain/rebus.core/blob/master/go.mod',
       'https://github.com/bandprotocol/chain/blob/master/go.mod',
       'https://github.com/cybercongress/go-cyber/blob/fea852c950e8275e18aa5f715296b6ca4daed613/go.mod#L11',
       'https://github.com/strangelove-ventures/noble/blob/main/go.mod']


with open('ibc-go_versions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['chain', 'ibc-go_version'])
    
    for url in urls:
        response = requests.get(url)
        
        for line in response.text.splitlines():
            if "ibc-go" in line:
                parts = line.split(" ")
                version = parts[17].replace('class="pl-c1">', "").replace("</span></td>", "")
                
                url_name = url.split('/')[3:5]
                
                writer.writerow([url_name, version])
                break
