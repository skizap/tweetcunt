#!/usr/bin/python

from tweetcap import tweetcap
from datetime import datetime
import dateutil.tz, sqlite3, sys, json, os, re
from twython import Twython, TwythonStreamer
from twython.exceptions import TwythonAuthError
import greenclock
import time
# CREATE TABLE CUNT(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# IS_CUNT INT NOT NULL,
# USER_ID TEXT NOT NULL,
# SCREEN_NAME TEXT NOT NULL
# );

consumer_key = 'JcJMiSpjtfP1cEPGDpZZp8X95'
consumer_secret = 'bDrR0O5YvfJw0rGiCEkW2chn629UUJkxeWQMB0JBGVjFH2yrAn'
access_token = '797788038852124672-A2EHtZNvq0XuwxCtfQxAH1JKxpQmhSL'
access_token_secret = 'BbRQltUQJsIoNCkteoNTLovytt3ZowtdU6HJn5j9JTigS'

db_path_default = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cunts.db')
db_path = os.getenv('DB', db_path_default)
con = sqlite3.connect(db_path, isolation_level=None)
rest = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
cur = con.cursor()

cunts =[
'39294671', #FuturesTrader71
'908709033753939969', #i_am_ict
'3162911248', #mcm_ct
'247857712', #PeterLBrandt
'345525945', #TicTocTick
'1152105936', #StockBoardAsset
'1039135882786353152', #hks55
'33973843', #PipCzar
'972678867713515520', #VolatilityQ
'18349074', #MrAaronKlein
'2484732544', #micahhyo
'810632344247812096', #trickmitch1
'498166332', #elitedaytraders
'373102216', #jasonbondpicks
'735588145', #kylewdennis
'1262364356', #TSXtrad3r
'96682182', #modern_rock
'565969885', #madaznfootballr
'2746667072', #AT09_Trader
'15971805', #Investorslive
'351065125', #HenrikZeberg
'254280603', #MarkYusko
'19469119', #Hithermann
'974604645606805506', #WBTrading
'50718597', #Tradersimon
'29139515', #RedbridgeCap
'39294671', #FuturesTrader71
'908709033753939969', #i_am_ict
'3162911248', #mcm_ct
'247857712', #PeterLBrandt
'345525945', #TicTocTick
'1152105936', #StockBoardAsset
'1039135882786353152', #hks55
'33973843', #PipCzar
'972678867713515520', #VolatilityQ
'18349074', #MrAaronKlein
'2484732544', #micahhyo
'810632344247812096', #trickmitch1
'498166332', #elitedaytraders
'373102216', #jasonbondpicks
'735588145', #kylewdennis
'1262364356', #TSXtrad3r
'96682182', #modern_rock
'565969885', #madaznfootballr
'2746667072', #AT09_Trader
'15971805', #Investorslive
'351065125', #HenrikZeberg
'254280603', #MarkYusko
'19469119', #Hithermann
'974604645606805506', #WBTrading
'50718597', #Tradersimon
'29139515', #RedbridgeCap
'29139515', #RedbridgeCap
'203652149', #Burns
'75355098', #uktrend
'582390700', #Asenna wealth
'40116454', #andrenstasi
'2595918914', #Tradeciety
'23002939', #thechartist
'21573737', #Tischendorf
'1677755504', #raynerteo
'878707905784164356', #volfix
'61168016', #atradestar
'853610834764976128', #konningkarell
'4274984422', #PeBe187
'2806294664', #optionsnipper
'1110655850752983041', #Prooptions_pub
'276714687', #CMEBob
'830422195952312320', #DedicationForex
'252584436', #owsi1968
'613213247', #hugh
'18284885', #dollarfire
'48505944', #macrohedged
'1013792319961788417', #MHDirectional
'2290450146', #earnmormoney
'45683950', #marchav
'210663231', #wmdx
'928116687735480320', #scarface
'887748030304329728', #crptodog
'1016272682', #profmoney
'20402945', #cnbc
'1114997597566046208', #fayalyceAjer
'3688307962', #DavidBelle
'156058889', #dante
'2776073116', #traderbran
'2446024556', #mayne
'975791130594955264', #techanal
'899558268795842561', #cred
'256245632', #mandi
'737827191925420032', #tradewithedge
'249768777', #fxmacro
'792376662553989120', #northherofx
'85389537', #GregaHorvatFX 
'281238704', #trading_jazz
'791540058', #amanada57a
'516063875', #odelys
'1010309295731245060', #_freedomTrader
'168888420', #Shaq48_Trading
'1009555608', #priceactionkim
'823964111704834049', #Alphadaytrader
'1079937853877112832', #shadownomics
'1061650783333040129', #SuperLuckeee
]



def who_is_a_cunt():
	print("Scanning for cunts")
	cur.execute('SELECT * from CUNT')
	rows=cur.fetchall()
	for cunt in rows:
		cunt[2]
		maybeCunt=rest.show_user(id=cunt[2])
		if(maybeCunt['protected'] != cunt[1]): #CUNT DETECTED
			print("Cunt spotted")
			rev=0 if cunt[1] else 1
			rev_string="unprotected" if rev else "protected"
			stat="User "+cunt[3]+" has moved account to "+rev_string
			print(stat)
			#rest.update_status(status=cunt[0]+' has '+ 'his/fer account')
			cur.execute('UPDATE CUNT set IS_CUNT=? WHERE ID=?',(rev, cunt[0]))
	#for r in row:
	return

def add_all():
	for cunt in cunts:
		cur_cunt=rest.show_user(id=cunt)
		user_id=cur_cunt['id']
		screen_name=cur_cunt['screen_name']
		if cur_cunt['protected']:
			prot=1
		else:
			prot=0
		cur.execute('INSERT INTO CUNT (IS_CUNT,USER_ID, SCREEN_NAME) VALUES (?,?,?)', (prot,user_id,screen_name))

#add_all()
#who_is_a_cunt()

scheduler = greenclock.Scheduler(logger_name='task_scheduler')
scheduler.schedule('task_1', greenclock.every_second(4), who_is_a_cunt)
scheduler.run_forever(start_at='once')