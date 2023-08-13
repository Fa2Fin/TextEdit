import webbrowser
from os import system as go


def open_mwt_program():
    path = 'start R:\PROG\$Link\$IDM\MWT'
    go(path)


def open_rl():
    path = 'start R:\PROG\$Link\$IDM\RL_new'
    go(path)


def open_gdff_program():
    path = 'start R:\PROG\$Link\$IDM\GDFF_alpha'
    go(path)


def siebel_ie_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab('https://sso.siebel.mts.ru/')


def vrm_ie_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab('https://bpm.mts.ru/')


def mail_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab('https://e-mail.mts.ru/')


def help_desk_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab('https://helpdesk.mts.ru/default.aspx')


def suz_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab(
        'https://sso.suz.mts.ru')


def allplus_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab('https://allplus.mts.ru/')


def virt_men_open():
    webbrowser.get(using='windows-default').open_new_tab(
        'https://login.mts.ru/amserver/UI/Login?org=staff&service=staff&goto=https%3A%2F%2Fihelper.mts.ru%2Fncih')


def puls_open():
    webbrowser.open('https://newportal.mts.ru/Pages/AllNews.aspx', new=2)


def shared_mail_open():
    webbrowser.register('Chrome', None,
                        webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
    webbrowser.get(using='Chrome').open_new_tab('https://e-mail.mts.ru/owa/gosz_corporate@mts.ru/')


def foris_msk_open():
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Internet Explorer\iexplore.exe'))
    webbrowser.get(using='Chrome').open_new_tab('http://clust-crm.frsmsk.mts.ru/telcrm/gui/#')


def foris_sz_open():
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Internet Explorer\iexplore.exe'))
    webbrowser.get(using='Chrome').open_new_tab('http://clust-crm.frsnw.mts.ru/telcrm/gui/#')


def foris_sib_open():
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Internet Explorer\iexplore.exe'))
    webbrowser.get(using='Chrome').open_new_tab('http://clust-crm.frssib.mts.ru/telcrm/gui/#')


def foris_ug_open():
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Internet Explorer\iexplore.exe'))
    webbrowser.get(using='Chrome').open_new_tab('http://clust-crm.frsug.mts.ru/telcrm/gui/#')


def foris_pv_open():
    webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Internet Explorer\iexplore.exe'))
    webbrowser.get(using='Chrome').open_new_tab('http://clust-crm.frspv.mts.ru/telcrm/gui/#')


def collection_open():
    webbrowser.get(using='Chrome').open_new_tab(
        'https://citrixmsk2.msk.mts.ru')


def reports_msk_open():
    webbrowser.get(using='windows-default').open_new_tab('http://f-clust-reports.frsmsk.mts.ru/report/')


def reports_sz_open():
    webbrowser.get(using='windows-default').open_new_tab('http://f-clust-reports.frsnw.mts.ru/report/')


def reports_sib_open():
    webbrowser.get(using='windows-default').open_new_tab('http://f-clust-reports.frspv.mts.ru/report/')


def reports_ug_open():
    webbrowser.get(using='windows-default').open_new_tab('http://f-clust-reports.frssib.mts.ru/report/')


def reports_pv_open():
    webbrowser.get(using='windows-default').open_new_tab('http://f-clust-reports.frsug.mts.ru/report/')
