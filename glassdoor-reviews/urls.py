'''All companies tracked with their corresponding Glassdoor reviews link'''

links = {
    '8x8': 'https://www.glassdoor.com/Reviews/8x8-Reviews-E4045.htm',
    'Discord': 'https://www.glassdoor.com/Reviews/Discord-Reviews-E910317.htm',
    'Five9': 'https://www.glassdoor.com/Reviews/Five9-Reviews-E433188.htm',
    'RingCentral': 'https://www.glassdoor.com/Reviews/RingCentral-Reviews-E197577.htm',
    'Twilio': 'https://www.glassdoor.com/Reviews/Twilio-Reviews-E410790.htm',
    'Zoom': 'https://www.glassdoor.com/Reviews/Zoom-Video-Communications-Reviews-E924644.htm',
    'Box': 'https://www.glassdoor.com/Reviews/Box-Reviews-E254092.htm',
    'CockroachDB': 'https://www.glassdoor.com/Reviews/Cockroach-Labs-Reviews-E1168502.htm',
    'Confluent': 'https://www.glassdoor.com/Reviews/Confluent-Reviews-E1048428.htm',
    'Databricks': 'https://www.glassdoor.com/Reviews/Databricks-Reviews-E954734.htm',
    'Dropbox': 'https://www.glassdoor.com/Reviews/Dropbox-Reviews-E415350.htm',
    'Elastic': 'https://www.glassdoor.com/Reviews/Elastic-Reviews-E751551.htm',
    'MongoDB': 'https://www.glassdoor.com/Reviews/MongoDB-Reviews-E433703.htm',
    'Snowflake': 'https://www.glassdoor.com/Reviews/Snowflake-Reviews-E928471.htm',
    'YugaByteDB': 'https://www.glassdoor.com/Reviews/YugaByte-Reviews-E2427869.htm',
    'Autodesk': 'https://www.glassdoor.com/Reviews/Autodesk-Reviews-E1155.htm',
    'DataRobot': 'https://www.glassdoor.com/Reviews/DataRobot-Reviews-E911432.htm',
    'GitLab': 'https://www.glassdoor.com/Reviews/GitLab-Reviews-E1296544.htm',
    'JFrog': 'https://www.glassdoor.com/Reviews/JFrog-Reviews-E553835.htm',
    'LaunchDarkly': 'https://www.glassdoor.com/Reviews/LaunchDarkly-Reviews-E1897319.htm',
    'Matterport': 'https://www.glassdoor.com/Reviews/Matterport-Reviews-E700767.htm',
    'Roblox': 'https://www.glassdoor.com/Reviews/Roblox-Reviews-E242265.htm',
    'UiPath': 'https://www.glassdoor.com/Reviews/UiPath-Reviews-E1102519.htm',
    'Unity': 'https://www.glassdoor.com/Reviews/Unity-Reviews-E455854.htm',
    'Adobe': 'https://www.glassdoor.com/Reviews/Adobe-Reviews-E1090.htm',
    'Alteryx': 'https://www.glassdoor.com/Reviews/Alteryx-Reviews-E351220.htm',
    'Atlassian': 'https://www.glassdoor.com/Reviews/Atlassian-Reviews-E115699.htm',
    'Dynatrace': 'https://www.glassdoor.com/Reviews/Dynatrace-Reviews-E309684.htm',
    'Labelbox': 'https://www.glassdoor.com/Reviews/Labelbox-Reviews-E2014427.htm',
    'New Relic': 'https://www.glassdoor.com/Reviews/New-Relic-Reviews-E461657.htm',
    'Scale': 'https://www.glassdoor.com/Reviews/Scale-Reviews-E1656849.htm',
    'ServiceNow': 'https://www.glassdoor.com/Reviews/ServiceNow-Reviews-E403326.htm',
    'Splunk': 'https://www.glassdoor.com/Reviews/Splunk-Reviews-E117313.htm',
    'Airtable': 'https://www.glassdoor.com/Reviews/Airtable-Reviews-E1863415.htm',
    'Anaplan': 'https://www.glassdoor.com/Reviews/Anaplan-Reviews-E695685.htm',
    'Appian': 'https://www.glassdoor.com/Reviews/Appian-Reviews-E27819.htm',
    'Asana': 'https://www.glassdoor.com/Reviews/Asana-Reviews-E567443.htm',
    'Braze': 'https://www.glassdoor.com/Reviews/Braze-Reviews-E1879400.htm',
    'DocuSign': 'https://www.glassdoor.com/Reviews/DocuSign-Reviews-E307604.htm',
    'HashiCorp': 'https://www.glassdoor.com/Reviews/HashiCorp-Reviews-E1359860.htm',
    'HubSpot': 'https://www.glassdoor.com/Reviews/HubSpot-Reviews-E227605.htm',
    'Monday': 'https://www.glassdoor.com/Reviews/monday-com-Reviews-E725019.htm',
    'Notion': 'https://www.glassdoor.com/Reviews/Notion-Labs-Reviews-E3304926.htm',
    'Procore': 'https://www.glassdoor.com/Reviews/Procore-Technologies-Reviews-E691343.htm',
    'Qualtrics': 'https://www.glassdoor.com/Reviews/Qualtrics-Reviews-E323717.htm',
    'Smartsheet': 'https://www.glassdoor.com/Reviews/Smartsheet-Reviews-E438753.htm',
    'ZoomInfo': 'https://www.glassdoor.com/Reviews/ZoomInfo-Reviews-E22253.htm',
    'Avalara': 'https://www.glassdoor.com/Reviews/Avalara-Reviews-E116638.htm',
    'Coinbase': 'https://www.glassdoor.com/Reviews/Coinbase-Reviews-E779622.htm',
    'Coupa': 'https://www.glassdoor.com/Reviews/Coupa-Software-Inc-Reviews-E217718.htm',
    'PayPal': 'https://www.glassdoor.com/Reviews/PayPal-Reviews-E9848.htm',
    'Paycom': 'https://www.glassdoor.com/Reviews/Paycom-Reviews-E136736.htm',
    'Paylocity': 'https://www.glassdoor.com/Reviews/Paylocity-Reviews-E29987.htm',
    'Shopify': 'https://www.glassdoor.com/Reviews/Shopify-Reviews-E675933.htm',
    'Workday': 'https://www.glassdoor.com/Reviews/Workday-Reviews-E197851.htm',
    'Zendesk': 'https://www.glassdoor.com/Reviews/Zendesk-Reviews-E360923.htm',
    'Stripe': 'https://www.glassdoor.com/Reviews/Stripe-Reviews-E671932.htm',
    'Cloudflare': 'https://www.glassdoor.com/Reviews/Cloudflare-Reviews-E430862.htm',
    'CrowdStrike': 'https://www.glassdoor.com/Reviews/CrowdStrike-Reviews-E795976.htm',
    'CyberArk': 'https://www.glassdoor.com/Reviews/CyberArk-Reviews-E30042.htm',
    'Datadog': 'https://www.glassdoor.com/Reviews/Datadog-Reviews-E762009.htm',
    'Lacework': 'https://www.glassdoor.com/Reviews/Lacework-Reviews-E1373969.htm',
    'SentinelOne': 'https://www.glassdoor.com/Reviews/SentinelOne-Reviews-E1361978.htm',
    'Snyk': 'https://www.glassdoor.com/Reviews/Snyk-Reviews-E2094989.htm',
    'Tenable': 'https://www.glassdoor.com/Reviews/Tenable-Reviews-E17494.htm',
    'VMware': 'https://www.glassdoor.com/Reviews/VMware-Reviews-E12830.htm',
    'Wiz': 'https://www.glassdoor.com/Reviews/Wiz-Reviews-E5304442.htm',
    'Orca Security': 'https://www.glassdoor.com/Reviews/Orca-Security-Reviews-E4711715.htm',
    'Aqua Security': 'https://www.glassdoor.com/Reviews/Aqua-Security-Software-Reviews-E1785939.htm',
    'Zscaler': 'https://www.glassdoor.com/Reviews/Zscaler-Reviews-E359434.htm',
    'Acorns': 'https://www.glassdoor.com/Reviews/Acorns-Reviews-E971931.htm',
    'Affirm': 'https://www.glassdoor.com/Reviews/Affirm-Reviews-E823564.htm',
    'Bill.com': 'https://www.glassdoor.com/Reviews/Bill-com-Reviews-E801594.htm',
    'Block': 'https://www.glassdoor.com/Reviews/Block-Reviews-E422050.htm',
    'Chime': 'https://www.glassdoor.com/Reviews/Chime-Reviews-E1493686.htm',
    'Dave': 'https://www.glassdoor.com/Reviews/Dave-Reviews-E1847431.htm',
    'Klarna': 'https://www.glassdoor.com/Reviews/Klarna-Reviews-E389854.htm',
    'LendingTree': 'https://www.glassdoor.com/Reviews/LendingTree-Reviews-E11154.htm',
    'Remitly': 'https://www.glassdoor.com/Reviews/Remitly-Reviews-E1044836.htm',
    'Robinhood': 'https://www.glassdoor.com/Reviews/Robinhood-Reviews-E1167765.htm',
    'SoFi': 'https://www.glassdoor.com/Reviews/SoFi-Reviews-E779979.htm',
    'ConsenSys': 'https://www.glassdoor.com/Reviews/ConsenSys-Reviews-E1613426.htm',
    'Crypto.com': 'https://www.glassdoor.com/Reviews/Crypto-com-Reviews-E1984553.htm',
    'Exodus': 'https://www.glassdoor.com/Reviews/Exodus-Reviews-E3395584.htm',
    'Gemini': 'https://www.glassdoor.com/Reviews/Gemini-Reviews-E1400858.htm',
    'Kraken': 'https://www.glassdoor.com/Reviews/Kraken-Digital-Asset-Exchange-Reviews-E938667.htm',
    'Ledger': 'https://www.glassdoor.com/Reviews/Ledger-Reviews-E1674523.htm',
    'Binance': 'https://www.glassdoor.com/Reviews/Binance-Reviews-E1816824.htm',
    'Spotify': 'https://www.glassdoor.com/Reviews/Spotify-Reviews-E408251.htm',
    'Deezer': 'https://www.glassdoor.com/Reviews/Deezer-Reviews-E786653.htm',
    'Splice': 'https://www.glassdoor.com/Reviews/Splice-Reviews-E910323.htm',
    'Hulu': 'https://www.glassdoor.com/Reviews/Hulu-Reviews-E43242.htm',
    'Netflix': 'https://www.glassdoor.com/Reviews/Netflix-Reviews-E11891.htm',
    'Meta': 'https://www.glassdoor.com/Reviews/Meta-Reviews-E40772.htm',
    'Snap': 'https://www.glassdoor.com/Reviews/Snap-Reviews-E671946.htm',
    'Twitter': 'https://www.glassdoor.com/Reviews/Twitter-Reviews-E100569.htm',
    'Red Hat': 'https://www.glassdoor.com/Reviews/Red-Hat-Reviews-E8868.htm',
    'TikTok': 'https://www.glassdoor.com/Reviews/TikTok-Reviews-E2230881.htm',
    'Reddit': 'https://www.glassdoor.com/Reviews/Reddit-Reviews-E796358.htm',
    'Pinterest': 'https://www.glassdoor.com/Reviews/Pinterest-Reviews-E503467.htm',
    'Barstool': 'https://www.glassdoor.com/Reviews/Barstool-Sports-Reviews-E891717.htm',
    'DraftKings': 'https://www.glassdoor.com/Reviews/DraftKings-Reviews-E902154.htm',
    'Fanduel': 'https://www.glassdoor.com/Reviews/FanDuel-Reviews-E894936.htm',
    'Okta': 'https://www.glassdoor.com/Reviews/Okta-Reviews-E444756.htm',
    'Ping Identity': 'https://www.glassdoor.com/Reviews/Ping-Identity-Reviews-E380907.htm',
    'Qualys': 'https://www.glassdoor.com/Reviews/Qualys-Reviews-E30935.htm',
    'Rapid7': 'https://www.glassdoor.com/Reviews/Rapid7-Reviews-E243542.htm',
    'Palo Alto Networks': 'https://www.glassdoor.com/Reviews/Palo-Alto-Networks-Reviews-E115142.htm',
    'Nvidia': 'https://www.glassdoor.com/Reviews/NVIDIA-Reviews-E7633.htm',
    'WeWork': 'https://www.glassdoor.com/Reviews/WeWork-Reviews-E661275.htm',
    'Ranpak': 'https://www.glassdoor.com/Reviews/Ranpak-Reviews-E794701.htm',
    'Duolingo': 'https://www.glassdoor.com/Reviews/Duolingo-Reviews-E629348.htm',
    'Pegasystems': 'https://www.glassdoor.com/Reviews/Pegasystems-Reviews-E5936.htm',
    'Cardlytics': 'https://www.glassdoor.com/Reviews/Cardlytics-Reviews-E467229.htm',
    'Fortinet': 'https://www.glassdoor.com/Reviews/Fortinet-Reviews-E23128.htm',
    'Stoneco': 'https://www.glassdoor.com/Reviews/Stone-Reviews-E1093539.htm',
    'PagerDuty': 'https://www.glassdoor.com/Reviews/PagerDuty-Reviews-E704466.htm',
    'Squarespace': 'https://www.glassdoor.com/Reviews/Squarespace-Reviews-E466343.htm',
    'Wix': 'https://www.glassdoor.com/Reviews/Wix-Reviews-E391615.htm',
    'C3 AI': 'https://www.glassdoor.com/Reviews/C3-AI-Reviews-E312703.htm',
    'DigitalOcean': 'https://www.glassdoor.com/Reviews/DigitalOcean-Reviews-E823482.htm',
    'Bumble': 'https://www.glassdoor.com/Reviews/Bumble-Reviews-E1161959.htm',
    'Match': 'https://www.glassdoor.com/Reviews/Match-Reviews-E15905.htm',
    'AirBnB': 'https://www.glassdoor.com/Reviews/Airbnb-Reviews-E391850.htm',
    'Coupang': 'https://www.glassdoor.com/Reviews/Coupang-Reviews-E914956.htm',
    'Visa': 'https://www.glassdoor.com/Reviews/Visa-Inc-Reviews-E3035.htm',
    'Mastercard': 'https://www.glassdoor.com/Reviews/Mastercard-Reviews-E3677.htm',
    'Opendoor': 'https://www.glassdoor.com/Reviews/Opendoor-Reviews-E1021515.htm',
    'Zillow': 'https://www.glassdoor.com/Reviews/Zillow-Reviews-E40802.htm',
    'Redfin': 'https://www.glassdoor.com/Reviews/Redfin-Reviews-E150726.htm',
    'Palantir': 'https://www.glassdoor.com/Reviews/Palantir-Technologies-Reviews-E236375.htm',
    'Quantumscape': 'https://www.glassdoor.com/Reviews/Quantumscape-Reviews-E1349613.htm',
    'Intuit': 'https://www.glassdoor.com/Reviews/Intuit-Reviews-E2293.htm',
    'Instacart': 'https://www.glassdoor.com/Reviews/Instacart-Reviews-E714486.htm',
    'Grab': 'https://www.glassdoor.com/Reviews/Grab-Reviews-E958580.htm',
    'Uber': 'https://www.glassdoor.com/Reviews/Uber-Reviews-E575263.htm',
    'Lyft': 'https://www.glassdoor.com/Reviews/Lyft-Reviews-E700614.htm',
    'DoorDash': 'https://www.glassdoor.com/Reviews/DoorDash-Reviews-E813073.htm',
    'Gopuff': 'https://www.glassdoor.com/Reviews/Gopuff-Reviews-E926131.htm',
    'Grubhub': 'https://www.glassdoor.com/Reviews/Grubhub-Reviews-E419089.htm',
    'Gorillas': 'https://www.glassdoor.com/Reviews/Gorillas-Technologies-GmbH-Reviews-E3605925.htm',
    'Getir': 'https://www.glassdoor.com/Reviews/Getir-Reviews-E1257698.htm',
    'Jokr': 'https://www.glassdoor.com/Reviews/JOKR-Reviews-E5269238.htm',
    'HelloFresh': 'https://www.glassdoor.com/Reviews/HelloFresh-Reviews-E998728.htm',
    'Bandwidth': 'https://www.glassdoor.com/Reviews/Bandwidth-Reviews-E31205.htm',
    'Applovin': 'https://www.glassdoor.com/Reviews/AppLovin-Reviews-E576360.htm',
}

