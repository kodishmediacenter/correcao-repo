# Creditos ao Addon Oneplay pelo script 
# 
# Ultima versao 16/01/2021
# 
# by Oneplay Mod Kodish (26/09/2022)

import xbmc,xbmcvfs
import xbmcgui
import os
import sqlite3
import datetime

dir_database = xbmcvfs.translatePath("special://home/userdata/Database/")
db = os.path.join(dir_database, 'Addons33.db')
conn = sqlite3.connect(db)

def get_kversion():
	full_version_info = xbmc.getInfoLabel('System.BuildVersion')
	baseversion = full_version_info.split(".")
	intbase = int(baseversion[0])
	return  intbase
    

def delete_id(addon_id):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql = 'DELETE FROM installed WHERE addonID=?'
        cursor.execute(sql, (addon_id,))
        conn.commit()
        conn.close()
    except:
        pass
        
def insert_id(addon_id):
    try:
        now = datetime.datetime.now()
        installDate = now.strftime("%Y-%m-%d %H:%M:%S")
        value = 1
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql = 'INSERT INTO installed (addonID,enabled,installDate) VALUES(?,?,?)'
        cursor.execute(sql, (addon_id,value,installDate,))
        
        conn.commit()
        conn.close()
    except:
        pass
        
def update_id(addon_id):
    try:
        value = 1
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql = 'UPDATE installed SET enabled= ? WHERE addonID= ?'
        cursor.execute(sql, (value,addon_id,))
        conn.commit()
        conn.close()
    except:
        pass        


def enable_addon(addon_id):
    if get_kversion() >16.5:
        delete_id(addon_id)
        insert_id(addon_id)
        #update_id(addon_id)
        #xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
#checkintegrity13122019
