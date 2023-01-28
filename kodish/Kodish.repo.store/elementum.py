# Python 3 code
import urllib.request, urllib.parse, urllib.error
import zipfile
import os,xbmcvfs,shutil,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import sys
import re
import database


ADDON_ID      = 'Kodish.repo.store'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME    = REAL_SETTINGS.getAddonInfo('name')
ICON          = REAL_SETTINGS.getAddonInfo('icon')
FANART        = REAL_SETTINGS.getAddonInfo('fanart')


def elementum_android(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/android-pc/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)

def elementum_android_arm(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/android-arm/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)


def elementum_apple(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/apple/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)


def elementum_linux(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/linux-pc/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)

def elementum_linux_arm(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/linux-arm/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)

def elementum_windows(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "plugin.video.elementum"
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/win/plugin.video.elementum.zip'
    filezip2 = "plugin.video.elementum.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)

def elementum_dep(nome):

    param2 = nome
    zip_file = "special://home/media/"
    api_file  = os.path.join(xbmcvfs.translatePath(zip_file))
    filezip = re.sub('plugin://kodish.repo.store/', r'', param2)
    filezip2 = str(filezip.replace("?file=",""))
    tam = len(filezip2)
    filezip21 = "context.elementum"
    filezip22 = "script.elementum.burst"
    verifica_addon_instalado(filezip21)
    url = 'https://raw.githubusercontent.com/kodishmediacenter/elementum/main/0.1.87/dep.zip'
    filezip2 = "dep.zip" 
    print("baixando addon ....")
    os.chdir (api_file) 
    urllib.request.urlretrieve(url, ""+filezip2+"")
    exemploZIP = zipfile.ZipFile (""+filezip2+"")
    exemploZIP.extractall()
    exemploZIP.close()
    source = ""+api_file+"/"+filezip21+""
    source2 = ""+api_file+"/"+filezip22+""
    destination = "special://home/addons"
    destination2 = os.path.join(xbmcvfs.translatePath(destination))
    shutil.move(source, destination2)
    shutil.move(source2, destination2)
    dialog = xbmcgui.Dialog()
    dialog.ok('Kodish Store Azura DX', 'Addon Instalado com sucesso saia do Kodi apos instalar tudo do elementum para que possa ser ativado')
    database.insert_id(filezip21)
    database.insert_id(filezip22)

def verifica_addon_instalado(ids):
    tamz = len(ids)
    for a in ['special://home/addons/'+ids+'']:
        existe = xbmcvfs.translatePath(a)       
        if os.path.exists(existe)==True:
                dialog = xbmcgui.Dialog()
                dialog.ok('Kodish Store Azura DX', 'Addon Ja foi Instalado')
                break
      




def main_elementum():
    dialog = xbmcgui.Dialog()
    link = dialog.select('Kodish Store - Azura', ['Android PC','Android ARM','Apple','Linux','Linux ARM','Windows','Dependencias'])

    if link == 0:
        nome = ""
        elementum_android(nome)

    if link == 1:
        nome = ""
        elementum_android_arm(nome)

    if link == 2:
        nome = ""
        elementum_apple(nome)

    if link == 3:
        nome = ""
        elementum_linux(nome)

    if link == 4:
        nome = ""
        elementum_linux_arm(nome)

    if link == 5:
        nome = ""
        elementum_windows(nome)

    if link == 6:
        nome = ""
        elementum_dep(nome)
