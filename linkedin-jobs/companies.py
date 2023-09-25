'''All companies tracked with their corresponding LinkedIn ID'''

Communications = {'8x8': '8x8', 'Discord': 'discord', 'Five9': 'five9',
    'RingCentral': 'ringcentral', 'Twilio': 'twilio-inc-',
    'Zoom': 'zoom-video-communications'}

DatabasesAndStorage = {'Adobe': 'adobe', 'AWS': 'amazon-web-services',
    'Microsoft': 'microsoft',
    'Box': 'box', 'CockroachDB': 'cockroach-labs', 'Confluent': 'confluent',
    'Databricks': 'databricks', 'Dropbox': 'dropbox', 'Elastic': 'elastic-co',
    'Google': 'google', 'MongoDB': 'mongodbinc', 'Oracle': 'oracle',
    'Snowflake': 'snowflake-computing', 'YugabyteDB': 'yugabyte'}

Devops3DVRAndEngineering = {'Autodesk': 'autodesk', 'DataRobot': 'datarobot',
    'GitLab': 'gitlab-com', 'JFrog': 'jfrog-ltd',
    'LaunchDarkly': 'launchdarkly', 'Matterport': 'matterport',
    'Roblox': 'roblox', 'UiPath': 'uipath', 'Unity': 'unity'}

IntelligenceAndAnalytics = {'Alteryx': 'alteryx', 'Atlassian': 'atlassian',
    'Dynatrace': 'dynatrace', 'Labelbox': 'labelbox',
    'New Relic': 'new-relic-inc-', 'Scale': 'scaleai',
    'ServiceNow': 'servicenow', 'Splunk': 'splunk'}

Management = {'Airtable': 'airtable', 'Anaplan': 'anaplan',
    'Appian': 'appian-corporation', 'Asana': 'asana', 'Braze': 'braze',
    'Docusign': 'docusign', 'HashiCorp': 'hashicorp', 'Hubspot': 'hubspot',
    'Monday': 'mondaydotcom', 'Notion': 'notionhq',
    'Procore': 'procore-technologies', 'Qualtrics': 'qualtrics',
    'Salesforce': 'salesforce', 'Smartsheet': 'smartsheet-com',
    'Workday': 'workday', 'Zendesk': 'zendesk', 'ZoomInfo': 'zoominfo'}

MoneyAndPayments = {'Avalara': 'avalara', 'Block': 'joinblock',
    'Coupa': 'coupa-software', 'Grab': 'grabapp', 'Instacart': 'instacart',
    'PayPal': 'paypal', 'Paycom': 'paycom', 'Paylocity': 'paylocity',
    'Shopify': 'shopify', 'Stripe': 'stripe'}

Security = {'Cloudflare': 'cloudflare', 'Crowdstrike': 'crowdstrike',
    'CyberArk': 'cyber-ark-software', 'Datadog': 'datadog',
    'Lacework': 'lacework', 'Okta': 'okta-inc-',
    'Palo Alto Networks': 'palo-alto-networks', 'PingIdentity': 'ping-identity',
    'Qualys': 'qualys', 'Rapid7': 'rapid7', 'Redhat': 'red-hat',
    'SentinelOne': 'sentinelone', 'Snyk': 'snyk', 'Tenable': 'tenableinc',
    'VMWare': 'vmware', 'Wiz': 'wizsecurity', 'Zscaler': 'zscaler'}

Crypto = {'Coinbase': 'coinbase', 'Crypto.com': 'cryptocom',
    'Binance': 'binance', 'Bitcoin': 'bitcoin-kinetics', 'Ethereum': 'ethereum',
    'Cardano': 'cardano-foundation', 'Polkadot': 'polkadot-network',
    'Solana': 'solanalabs', 'IOHK': 'input-output-global',
    'Parity': 'paritytech', 'Web3 Foundation': 'web3foundation', 'FTX': 'ftx',
    'Gemini': 'geminitrust', 'Kraken': 'krakenfx', 'The Graph': 'thegraph',
    'Chainlink': 'chainlink-labs', 'Polygon': '0xpolygon', 'DFINITY': 'dfinity',
    'BlockFi': 'blockfi', 'Celsius': 'celsiusnetwork', 'Nexo': 'nexofinance',
    'Ripple': 'rippleofficial', 'Aave': 'aaveaave', 'Uniswap': 'uniswaporg',
    'Algorand': 'algorand', 'Avalanche': 'avalancheavax',
    'Ava Labs': 'avalabsofficial', 'Terra': 'terraform-labs',
    'Brave': 'brave-software', 'Arbitrum': 'offchain-labs-inc',
    'Optimism': 'oplabs', 'ConsenSys': 'consensys-software-inc',
    'OpenSea': 'opensea-io', 'Decentraland': 'decentralandorg',
    'Sandbox': 'thesandbox-game', 'Arweave': 'arweave',
    'Helium': 'heliumnetwork', 'Aleo': 'aleohq', 'Alchemy': 'alchemyinc',
    'Near Inc': 'near-inc-development',
    'Near Protocol': 'near-protocol-project', 'Filecoin': 'filecoin-foundation',
    'Protocol Labs': 'protocollabs', 'Storj': 'storj', 'Tether': 'tether',
    'Circle': 'circle-internet-financial', 'Bitfinex': 'bitfinex',
    'Yuga Labs': 'yuga-labs', 'Doodles': 'doodlesllc',
    'Axie Infinity': 'axieinfinity', 'Compound': 'compound-labs',
    'MakerDAO': 'makerdao', 'PancakeSwap': 'pancakeswap', 'IoTeX': 'iotex',
    'IOTA': 'iotafoundation', 'Dapper Labs': 'dapper-labs',
    'Flow': 'flow-blockchain'}

Semiconductors = {'Nvidia': 'nvidia', 'AMD': 'amd', 'Wolfspeed': 'wolfspeed',
    'Intel': 'intel-corporation', 'Broadcom': 'broadcom',
    'NXP': 'nxp-semiconductors', 'Onsemi': 'onsemi', 'Qualcomm': 'qualcomm',
    'Analog Devices': 'analog-devices', 'Cirrus': 'cirrus-logic',
    'Texas Instruments': 'texas-instruments', 'Teradyne': 'teradyne',
    'Microchip': 'microchip-technology', 'Qorvo': 'qorvo', 'KLA': 'klacorp',
    'Micron': 'micron-technology', 'Applied Materials': 'applied-materials',
    'Lam Research': 'lam-research', 'Marvell': 'marvell',
    'GlobalFoundries': 'globalfoundries', 'Ambarella': 'ambarella',
    'II-VI': 'ii-vi-incorporated'
    }

Fitness = {'Life Time': 'lifetimeinc', 'Planet Fitness': 'planet-fitness',
    'Crunch Fitness': 'crunch-fitness', 'Equinox': 'equinox',
    'iFIT': 'ifit---fitness-technology', 'Strava': 'strava-inc.',
    'WHOOP': 'whoop', 'Peloton': 'peloton-interactive-',
    'Tonal': 'tonal-strong', 'Mirror': 'getthemirror', 'Nike': 'nike',
    'Adidas': 'adidas'}

category_list = {'Communications': Communications,
    'Databases-Storage': DatabasesAndStorage,
    'Devops-3DVR-Engineering': Devops3DVRAndEngineering,
    'Intelligence-Analytics': IntelligenceAndAnalytics,
    'Management': Management, 'Money-Payments': MoneyAndPayments,
    'Security': Security, 'Crypto': Crypto,
    'Semiconductors': Semiconductors, 'Fitness': Fitness}

