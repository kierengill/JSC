'''All websites tracked with their corresponding companies/descriptions'''

# 'wd1.myworkdayjobs.com', 'wd5.myworkdayjobs.com' career info for companies
# Snowflake has customer data
# Datadog has customer data
# Cloudflare has customer data
# Lacework has customer data
# Okta has customer data
# Monday has customer data
# Zendesk has customer data
# Atlassian has customer data
# Splunk has customer data
# Zoom has customer data
# Coupa has customer data
# Qualtrics has customer data

Careers = {'Snowflake Jobs': 'careers.snowflake.com',
    'Confluent Jobs': 'careers.confluent.io', 'Elastic Jobs': 'jobs.elastic.co',
    'Microsoft Jobs': 'careers.microsoft.com', 'Amazon Jobs': 'amazon.jobs',
    'Google Jobs': 'careers.google.com',
    'Redhat Jobs': 'careers-redhat.icims.com',
    'ServiceNow Jobs': 'careers.servicenow.com',
    'Unity Jobs': 'careers.unity.com',
    'Zoom Jobs': 'careers.zoom.us',
    'Paylocity Jobs': 'recruiting.paylocity.com',
    'Dynatrace Jobs': 'careers.dynatrace.com',
    'Tenable Jobs': 'careers.tenable.com', 'Coupa Jobs': 'careers.coupa.com',
    'CyberArk Jobs': 'careers.cyberark.com',
    'Appian Jobs': 'careers.appian.com', 'JFrog Jobs': 'join.jfrog.com',
    'VMWare Jobs': 'careers.vmware.com', 'Instacart Jobs': 'instacart.careers',
    'Roblox Jobs': 'careers.roblox.com', 'PayPal Jobs': 'careers.pypl.com',
    'AirBnB Jobs': 'careers.airbnb.com',
    'Palo Alto Networks Jobs': 'jobs.paloaltonetworks.com',
    'Box Jobs': 'careers.box.com'}

DatabasesAndStorage = {'Snowflake': 'snowflakecomputing.com',
    'MongoDB Atlas': 'cloud.mongodb.com', 'MongoDB Realm': 'realm.mongodb.com',
    'MongoDB Charts': 'charts.mongodb.com', 'Elastic': 'cloud.elastic.co',
    'Azure Portal': 'portal.azure.com', 'Azure Dev': 'dev.azure.com',
    'Azure Signup': 'signup.azure.com',
    'Microsoft Login': 'login.microsoftonline.com',
    'Amazon AWS': 'aws.amazon.com', 'Google Cloud': 'cloud.google.com',
    'Google Console': 'console.cloud.google.com',
    'Oracle Cloud': 'cloud.oracle.com',
    'Oracle Signup': 'signup.cloud.oracle.com',
    'Adobe Login': 'account.adobe.com',
    'Adobe Cloud': 'creativecloud.adobe.com',
    'YugabyteDB': 'cloud.yugabyte.com', 'CockroachDB': 'cockroachlabs.cloud',
    'Databricks': 'cloud.databricks.com',
    'Confluent': 'confluent.cloud', 'Confluent Login': 'login.confluent.io',
    'Dropbox': 'dropbox.com', 'Box': 'app.box.com'}

Security = {'Datadog': 'app.datadoghq.com', 'Redhat': 'access.redhat.com',
    'Crowdstrike': 'falcon.crowdstrike.com',
    'Palo Alto Networks': 'login.paloaltonetworks.com',
    'Cloudflare Dashboard': 'dash.cloudflare.com',
    'Cloudflare Access': 'cloudflareaccess.com',
    'Cloudflare Pages': 'pages.dev', 'Lacework': 'lacework.net',
    'Snyk': 'app.snyk.io', 'Okta': 'okta.com', 'Zscaler': 'zscaler.net',
    'VMWare': 'customerconnect.vmware.com', 'CyberArk': 'docs.cyberark.com',
    'SentinelOne': 'sentinelone.net',
    'PingIdentity': 'connect.pingidentity.com', 'Tenable': 'cloud.tenable.com',
    'Rapid7': 'insight.rapid7.com', 'Qualys': 'qualysguard.qualys.com',
    'Wiz': 'app.wiz.io'} 

Management = {'Salesforce': 'my.salesforce.com',
    'Salesforce Login': 'login.salesforce.com', 'Hubspot': 'app.hubspot.com',
    'Monday': 'auth.monday.com', 'Zendesk': 'zendesk.com',
    'Workday': 'workday.com', 'Workday Login': 'resourcecenter.workday.com',
    'Docusign': 'app.docusign.com', 'ZoomInfo': 'app.zoominfo.com',
    'Qualtrics': 'qualtrics.com', 'Smartsheet': 'app.smartsheet.com',
    'Airtable': 'airtable.com', 'Notion': 'notion.so',
    'Procore': 'app.procore.com', 'Asana': 'app.asana.com',
    'Braze': 'dashboard.braze.com', 'Anaplan': 'app.anaplan.com',
    'Appian': 'appiancloud.com', 'Hashicorp': 'cloud.hashicorp.com'}

IntelligenceAndAnalytics = {'NewRelic': 'one.newrelic.com',
    'Dynatrace': 'sso.dynatrace.com', 'Atlassian': 'atlassian.net',
    'Atlassian Login': 'id.atlassian.com',
    'Atlassian Jira': 'jira.atlassian.com', 'ServiceNow': 'service-now.com',
    'Splunk': 'splunkcloud.com', 'Splunk Login': 'login.splunk.com',
    'Alteryx': 'alteryx.com', 'Labelbox': 'app.labelbox.com',
    'Scale': 'dashboard.scale.com', 'Similarweb': 'pro.similarweb.com'}

DevopsVR3DEngineering = {'Autodesk': 'accounts.autodesk.com',
    'Unity': 'unity.com', 'DataRobot': 'datarobot.com',
    'UiPath': 'cloud.uipath.com', 'Matterport': 'my.matterport.com',
    'Roblox': 'roblox.com', 'JFrog': 'my.jfrog.com',
    'LaunchDarkly': 'app.launchdarkly.com', 'GitLab': 'gitlab.com'}

Communications = {'Zoom': 'zoom.us', 'RingCentral': 'login.ringcentral.com',
    'Twilio': 'console.twilio.com', 'Twilio Flex': 'flex.twilio.com',
    'Twilio SendGrid': 'app.sendgrid.com', 'Five9': 'app.five9.com',
    '8x8': 'sso.8x8.com', 'Discord': 'discord.com'}

MoneyAndPayments = {'Shopify': 'accounts.shopify.com',
    'Shopify CDN': 'cdn.shopify.com', 'Paycom': 'paycomonline.net',
    'Paylocity': 'access.paylocity.com', 'Avalara': 'identity.avalara.com',
    'Coupa': 'coupahost.com', 'Stripe': 'dashboard.stripe.com',
    'Orca': 'orca.so', 'PayPal Checkout': 'checkout.paypal.com',
    'PayPal Business': 'business.paypal.com', 'Coinbase': 'coinbase.com',
    'Coinbase Pro': 'pro.coinbase.com', 'Grab': 'grab.com',
    'Grab Food': 'food.grab.com', 'Instacart': 'instacart.com',
    'Credit Karma': 'creditkarma.com', 'Mailchimp': 'admin.mailchimp.com',
    'QuickBooks': 'qbo.intuit.com', 'TurboTax': 'myturbotax.intuit.com',
    'Mint': 'mint.intuit.com', 'Upstart': 'upstart.com'}

eCommerce = {'Amazon': 'amazon.com', 'Carvana': 'carvana.com',
    'Chewy': 'chewy.com', 'Etsy': 'etsy.com', 'Farfetch': 'farfetch.com',
    'Peloton': 'onepeloton.com', 'RealReal': 'therealreal.com',
    'Poshmark': 'poshmark.com', 'Revolve': 'revolve.com',
    'Wayfair': 'wayfair.com', 'eBay': 'ebay.com'}

Retail = {'AE': 'ae.com', 'Abercrombie': 'abercrombie.com', 'Gap': 'gap.com',
    'Old Navy': 'oldnavy.com', 'Macys': 'macys.com',
    'Nordstrom': 'nordstrom.com', 'Coach': 'coach.com', 'Jared': 'jared.com',
    'Zales': 'zales.com', 'Kay': 'kay.com', 'Michael Kors': 'michaelkors.com',
    'RH': 'rh.com', 'West Elm': 'westelm.com',
    'Pottery Barn': 'potterybarn.com', 'Lowes': 'lowes.com',
    'Home Depot': 'homedepot.com', 'Academy': 'academy.com',
    'BestBuy': 'bestbuy.com', 'Dicks Sporting Goods': 'dickssportinggoods.com',
    'Leslies': 'lesliespool.com', 'Target': 'target.com',
    'Walmart': 'walmart.com', 'Ulta': 'ulta.com',
    'Sally Beauty': 'sallybeauty.com', 'Whirlpool': 'whirlpool.com',
    'Carmax': 'carmax.com'}

Homes = {'KB Home': 'kbhome.com', 'Lennar': 'lennar.com',
    'DR Horton': 'drhorton.com', 'Pulte': 'pulte.com',
    'Sherwin Williams': 'sherwin-williams.com',
    'Benjamin Moore': 'benjaminmoore.com'}

Travel = {'Expedia': 'expedia.com', 'VRBO': 'vrbo.com',
    'Booking': 'booking.com', 'Priceline': 'priceline.com',
    'Trip': 'trip.com', 'Hertz': 'hertz.com', 'Avis': 'avis.com',
    'Delta': 'delta.com', 'United Airlines': 'united.com',
    'American Airlines': 'aa.com', 'Carnival': 'carnival.com',
    'Norwegian': 'ncl.com', 'Royal Caribbean': 'royalcaribbean.com',
    'AirBnB': 'airbnb.com'}

Delivery = {'Doordash': 'doordash.com', 'Instacart': 'instacart.com',
    'Grubhub': 'grubhub.com', 'Seamless': 'seamless.com',
    'GoPuff': 'gopuff.com', 'Gorillas': 'gorillas.io'}

categories = {'Careers': Careers, 'Databases-Storage': DatabasesAndStorage,
    'Security': Security, 'Management': Management, 'Delivery': Delivery,
    'Intelligence-Analytics': IntelligenceAndAnalytics,
    'Devops-3DVR-Engineering': DevopsVR3DEngineering,
    'Communications': Communications, 'Money-Payments': MoneyAndPayments,
    'Travel': Travel, 'eCommerce': eCommerce, 'Homes': Homes, 'Retail': Retail}

