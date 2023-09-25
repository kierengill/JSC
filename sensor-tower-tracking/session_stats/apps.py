'''All the apps tracked with their corresponding Sensor Tower IDs'''

iosTravel = {1456169098: 'Hertz', 308342527: 'Avis', 427916203: 'Expedia',
    367003839: 'Booking', 284971959: 'Hotels.com', 1245772818: 'VRBO',
    401626263: 'AirBnB', 336381998: 'Priceline', 382698565: 'American Airlines',
    388491656: 'Delta', 455004730: 'Marriott', 635150066: 'Hilton',
    681752345: 'Trip.com', 284876795: 'Trip Advisor', 925117977: 'Carnival',
    1260728016: 'Royal Caribbean', 1126094257: 'Norwegian', 368677368: 'Uber',
    529379082: 'Lyft'}
androidTravel = {'com.hertz.android.digital': 'Hertz',
    'com.avis.androidapp': 'Avis', 'com.expedia.bookings': 'Expedia',
    'booking-com-hotels-and-more': 'Booking.com',
    'com.hcom.android': 'Hotels.com', 'com.vrbo.android': 'VRBO',
    'com.airbnb.android': 'AirBnB',
    'com.priceline.android.negotiator': 'Priceline',
    'com.aa.android': 'American Airlines', 'com.delta.mobile.android': 'Delta',
    'com.marriott.mrt': 'Marriott', 'com.hilton.android.hhonors': 'Hilton',
    'ctrip.english': 'Trip.com', 'com.tripadvisor.tripadvisor': 'Trip Advisor',
    'com.carnival.android': 'Carnival',
    'com.rccl.royalcaribbean': 'Royal Caribbean', 'com.ncl.bge': 'Norwegian',
    'com.ubercab': 'Uber', 'me.lyft.android': 'Lyft'}

iosEcommerce = {297606951: 'Amazon', 571044395: 'Carmax', 1273426583: 'Carvana',
    353263352: 'Cars.com', 1494048038: 'Vroom', 1149449468: 'Chewy',
    477128284: 'Etsy', 906698760: 'Farfetch', 792750948: 'Peloton',
    587618103: 'RealReal', 470412147: 'Poshmark', 499725337: 'ThredUp',
    836767708: 'Wayfair', 282614216: 'eBay', 463624852: 'MercadoLibre',
    530621395: 'Wish', 1022579925: 'Stitch Fix', 938157117: '1stDibs',
    959841449: 'Shopee (Vietnam)', 1481812175: 'Shopee (Brazil)',
    959841443: 'Shopee (Indonesia)', 959841453: 'Shopee (Thailand)'}
androidEcommerce = {'com.amazon.mShop.android.shopping': 'Amazon',
    'com.carmax.carmax': 'Carmax', 'com.carvana.carvana': 'Carvana',
    'com.cars.android': 'Cars.com', 'com.vroom.app.android': 'Vroom',
    'com.chewy.android': 'Chewy', 'com.etsy.android': 'Etsy',
    'com.farfetch.farfetchshop': 'Farfetch',
    'com.onepeloton.callisto': 'Peloton', 'com.therealreal.app': 'RealReal',
    'com.poshmark.app': 'Poshmark', 'com.thredup.android': 'ThredUp',
    'com.wayfair.wayfair': 'Wayfair', 'com.ebay.mobile': 'eBay',
    'com.mercadolibre': 'MercadoLibre', 'com.contextlogic.wish': 'Wish',
    'com.stitchfix.stitchfix': 'Stitch Fix', 'com.shopee.br': 'Shopee (Brazil)',
    'com.shopee.id': 'Shopee (US)', 'com.shopee.vn': 'Shopee (Vietnam)'}

iosRetail = {467738064: 'AE + Aerie', 834465911: 'H&M',
    339041767: 'Abercrombie', 383915209: 'Hollister', 326347260: 'Gap',
    342792281: 'Old Navy', 341036067: 'Macys', 525536985: 'Bloomingdales',
    474349412: 'Nordstrom', 314855255: 'BestBuy',
    556653197: 'Dicks Sporting Goods', 1095459556: 'Nike', 1266591536: 'Adidas',
    297430070: 'Target', 338137227: 'Walmart'}
androidRetail = {'com.ae.ae': 'AE + Aerie', 'com.hm.goe': 'H&M',
    'com.abercrombie.abercrombie': 'Abercrombie',
    'com.abercrombie.hollister': 'Hollister',
    'com.gap.mobile.oldnavy': 'Old Navy', 'com.macys.android': 'Macys',
    'com.nordstrom.app': 'Nordstrom', 'com.bestbuy.android': 'BestBuy',
    'dsgui.android': 'Dicks Sporting Goods', 'com.nike.omega': 'Nike',
    'com.adidas.app': 'Adidas', 'com.target.ui': 'Target',
    'com.walmart.android': 'Walmart'}

iosUSFintech = {351727428: 'Venmo', 711923939: 'Cash App', 283646709: 'PayPal',
    1260755201: 'Zelle', 836215269: 'Chime', 1115120118: 'Klarna',
    1191985736: 'Sofi', 1193801909: 'Dave', 967040652: 'Affirm',
    1223471316: 'Shop (Shopify)', 1517676784: 'Varo', 883324671: 'Acorns',
    674258465: 'Remitly', 980353334: 'Bill.com', 957868548: 'LendingTree',
    584606479: 'QuickBooks Accounting', 938003185: 'Robinhood'}
androidUSFintech = {'com.venmo': 'Venmo', 'com.squareup.cash': 'Cash App',
    'com.paypal.android.p2pmobile': 'PayPal', 'com.zellepay.zelle': 'Zelle',
    'com.onedebit.chime': 'Chime', 'com.myklarnamobile': 'Klarna',
    'com.sofi.mobile': 'Sofi', 'com.dave': 'Dave',
    'com.affirm.central': 'Affirm', 'com.shopify.arrive': 'Shop (Shopify)',
    'com.varomoney.bank': 'Varo', 'com.acorns.android': 'Acorns',
    'com.remitly.androidapp': 'Remitly', 'com.bdc.bill': 'Bill.com',
    'com.ltmoneycenter_android.PROD': 'LendingTree',
    'com.intuit.quickbooks': 'QuickBooks Accounting',
    'com.robinhood.android': 'Robinhood'}

iosCrypto = {886427730: 'Coinbase', 1278383455: 'Coinbase Wallet',
    1438144202: 'Metamask', 1408914447: 'Gemini', 1095564685: 'FTX',
    1262148500: 'Crypto.com', 1414384820: 'Exodus', 1361671700: 'Ledger',
    1481947260: 'Kraken'}
androidCrypto = {'com.coinbase.android': 'Coinbase',
    'org.toshi': 'Coinbase Wallet', 'io.metamask': 'Metamask',
    'com.gemini.android.app': 'Gemini', 'com.blockfolio.blockfolio': 'FTX',
    'co.mona.android': 'Crypto.com', 'exodusmovement.exodus': 'Exodus',
    'com.ledger.live': 'Ledger', 'com.kraken.invest.app': 'Kraken'}

iosBankingApps = {298867247: 'Chase', 284847138: 'Bank of America',
    311548709: 'Wells Fargo', 301724680: 'Citi', 303113127: 'PNC',
    407558537: 'Capital One'}
androidBankingApps = {'com.chase.sig.android': 'Chase',
    'com.infonow.bofa': 'Bank of America',
    'com.wf.wellsfargomobile': 'Wells Fargo', 'com.citi.citimobile': 'Citi',
    'com.pnc.ecommerce.mobile': 'PNC', 'com.konylabs.capitalone': 'Capital One'}

iosInternationalFintech = {932493382: 'Revolut', 612261027: 'Wise',
    814456780: 'Nubank', 473941634: 'Paytm', 1052238659: 'Monzo',
    956857223: 'N26', 875855935: 'WorldRemit', 424716908: 'Western Union'}
androidInternationalFintech = {'com.revolut.revolut': 'Revolut',
    'com.transferwise.android': 'Wise', 'com.nu.production': 'Nubank',
    'net.one97.paytm': 'Paytm', 'co.uk.getmondo': 'Monzo',
    'de.number26.android': 'N26', 'com.worldremit.android': 'WorldRemit',
    'com.westernunion.android.mtapp': 'Western Union'}

iosMusic = {324684580: 'Spotify', 510855668: 'Amazon Music',
    1108187390: 'Apple Music', 292738169: 'Deezer',
    1017492454: 'YouTube Music'}
androidMusic = {'com.spotify.music': 'Spotify',
    'com.amazon.mp3': 'Amazon Music', 'com.apple.android.music': 'Apple Music',
    'deezer.android.app': 'Deezer',
    'com.google.android.apps.youtube.music': 'YouTube Music'}

iosVideoStreaming = {1498327873: 'Discovery+', 971265422: 'HBO Max',
    363590051: 'Netflix', 376510438: 'Hulu',
    545519333: 'Amazon Prime Video', 1446075923: 'Disney+',
    1193350206: 'YouTube TV'}
androidVideoStreaming = {'com.discovery.discoveryplus.mobile': 'Discovery+',
    'com.hbo.hbonow': 'HBO Max',
    'com.netflix.mediaclient': 'Netflix', 'com.hulu.plus': 'Hulu',
    'com.amazon.avod.thirdpartyclient': 'Amazon Prime Video',
    'com.disney.disneyplus': 'Disney+',
    'com.google.android.apps.youtube.unplugged': 'YouTube TV'}

iosSocialMedia = {284882215: 'Facebook', 389801252: 'Instagram',
    835599320: 'TikTok', 333903271: 'Twitter',
    429047995: 'Pinterest', 544007664: 'YouTube', 310633997: 'WhatsApp',
    447188370: 'Snapchat', 1064216828: 'Reddit', 288429040: 'LinkedIn',
    1459645446: 'BeReal', 985746746: 'Discord', 392796698: 'GroupMe'}
androidSocialMedia = {'com.facebook.katana': 'Facebook',
    'com.instagram.android': 'Instagram', 'com.zhiliaoapp.musically': 'TikTok',
    'com.twitter.android': 'Twitter', 'com.pinterest': 'Pinterest',
    'com.google.android.youtube': 'YouTube', 'com.whatsapp': 'WhatsApp',
    'com.snapchat.android': 'Snapchat', 'com.reddit.frontpage': 'Reddit',
    'com.linkedin.android': 'LinkedIn', 'com.bereal.ft': 'BeReal',
    'com.discord': 'Discord', 'com.groupme.android': 'GroupMe'}

iosDelivery = {545599256: 'Instacart', 719972451: 'DoorDash',
    1058959277: 'UberEats', 381840917: 'Seamless', 302920553: 'Grubhub',
    722804810: 'Gopuff', 1510225647: 'Gorillas', 995280265: 'Getir',
    1561652691: 'Jokr', 970107419: 'HelloFresh', 976642810: 'Blue Apron'}
androidDelivery = {'com.instacart.client': 'Instacart',
    'com.dd.doordash': 'DoorDash', 'com.ubercab.eats': 'UberEats',
    'com.seamlessweb.android.view': 'Seamless',
    'com.grubhub.android': 'Grubhub', 'com.main.gopuff': 'Gopuff',
    'com.eddress.getgoodys': 'Gorillas', 'com.getir': 'Getir',
    'com.jokr.delivery': 'Jokr', 'com.hellofresh.androidapp': 'HelloFresh',
    'com.blueapron.blueapron.release': 'Blue Apron'}

iosFood = {331177714: 'Starbucks', 327228455: 'Chipotle',
    922103212: 'McDonalds', 436491861: 'Dominos', 692365393: 'Panera',
    497387361: 'Taco Bell', 317279545: 'Shake Shack'}
androidFood = {'com.starbucks.mobilecard': 'Starbucks',
    'com.chipotle.ordering': 'Chipotle', 'com.mcdonalds.mobileapp': 'McDonalds',
    'com.Dominos': 'Dominos', 'com.panera.bread': 'Panera',
    'com.tacobell.ordering': 'Taco Bell',
    'com.shakeshack.android': 'Shake Shack'}

iosRealEstate = {310738695: 'Zillow', 327962480: 'Redfin',
    336698281: 'Realtor.com', 692766504: 'Compass',
    319836632: 'Apartments.com', 660363289: 'StreetEasy'}
androidRealEstate = {'com.zillow.android.zillowmap': 'Zillow',
    'com.redfin.android': 'Redfin', 'com.move.realtor': 'Realtor.com',
    'com.compass.compass': 'Compass',
    'com.apartments.mobile.android': 'Apartments.com',
    'com.zillow.android.streeteasy': 'StreetEasy'}

iosSportsGambling = {1413721906: 'Fanduel Sportsbook & Casino',
    1375031369: 'DraftKings Sportsbook & Casino',
    1430875409: 'BetMGM Sportsbook',
    1247519638: 'BetMGM Online Casino', 1413099571: 'Caesars Sportsbook',
    1474416533: 'Barstool Sportsbook & Casino', 519684662: 'bet365',
    710535379: 'DraftKings Fantasy Sports', 599664106: 'Fanduel Fantasy Sports'}
androidSportsGambling = {'com.fanduel.sportsbook': 'Fanduel Sportsbook & Casino',
    'com.draftkings.sportsbook': 'DraftKings Sportsbook & Casino',
    'com.playmgm.nj.sports': 'BetMGM Sportsbook',
    'com.playmgmcasino.nj': 'BetMGM Online Casino',
    'com.williamhill.us.nj.sports': 'Caesars Sportsbook',
    'com.png.sportsbook.google': 'Barstool Sportsbook & Casino',
    'com.bet365Wrapper.Bet365_Application': 'bet365',
    'com.draftkings.dknativermgGP': 'DraftKings Fantasy Sports',
    'com.fanduel.android.self': 'Fanduel Fantasy Sports'}

iosSoftware = {489969512: 'Asana', 1290128888: 'Monday', 618783545: 'Slack',
    546505307: 'Zoom', 1113153706: 'Microsoft Teams'}
androidSoftware = {'com.asana.app': 'Asana', 'com.monday.monday': 'Monday',
    'com.Slack': 'Slack', 'us.zoom.videomeetings': 'Zoom',
    'com.microsoft.teams': 'Microsoft Teams'}

iosGaming = {1300146617: 'Free Fire Rampage', 1480516829: 'Free Fire Max',
    431946152: 'Roblox', 1287282214: 'Call of Duty Mobile',
    1117841866: 'Empires & Puzzles (Zynga)', 354902315: 'Zynga Poker',
    694876905: 'Hit It Rich (Zynga)', 1196764367: 'Words with Friends (Zynga)',
    887947640: 'CSR Drag Racing (Zynga)', 553834731: 'Candy Crush (King)',
    850417475: 'Candy Crush Soda (King)', 608206510: 'Farm Heroes (King)',
    1095254858: 'Bubble Witch (King)', 572821456: 'Pet Rescue (King)'}
androidGaming = {'com.dts.freefireth': 'Free Fire Rampage',
    'com.dts.freefiremax': 'Free Fire Max',
    'com.roblox.client': 'Roblox',
    'com.activision.callofduty.shooter': 'Call of Duty Mobile',
    'com.smallgiantgames.empires': 'Empires & Puzzles (Zynga)',
    'com.zynga.livepoker': 'Zynga Poker',
    'com.zynga.hititrich': 'Hit It Rich (Zynga)',
    'com.zynga.words3': 'Words with Friends (Zynga)',
    'com.naturalmotion.customstreetracer2': 'CSR Drag Racing (Zynga)',
    'com.king.candycrushsaga': 'Candy Crush (King)',
    'com.king.candycrushsodasaga': 'Candy Crush Soda (King)',
    'com.king.farmheroessaga': 'Farm Heroes (King)',
    'com.king.bubblewitch3': 'Bubble Witch (King)',
    'com.king.petrescuesaga': 'Pet Rescue (King)'}


iosLists = [iosTravel, iosEcommerce,
    iosRetail,iosUSFintech,
    iosCrypto, iosBankingApps, iosInternationalFintech, iosMusic,
    iosVideoStreaming, iosSocialMedia, iosDelivery, iosFood,
    iosRealEstate, iosSportsGambling, iosSoftware, iosGaming]
androidLists = [androidTravel, androidEcommerce,
    androidRetail, androidUSFintech,
    androidCrypto, androidBankingApps, androidInternationalFintech, androidMusic,
    androidVideoStreaming, androidSocialMedia, androidDelivery, androidFood,
    androidRealEstate, androidSportsGambling, androidSoftware, androidGaming]
categories = ['Travel', 'Ecommerce', 'Retail', 'US Fintech', 'Crypto', 'Banking', 'International Fintech',
    'Music', 'Video Streaming', 'Social Media', 'Delivery', 'Food', 'Real Estate', 'Sports Gambling',
    'Software', 'Gaming']

