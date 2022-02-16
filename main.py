# https://mikanani.me/Home/Bangumi/2578
# https://mikanani.me/RSS/Bangumi?bangumiId=2578&subgroupid=574
# https://mikanani.me/RSS/Bangumi?bangumiId=2578&subgroupid=577

# https://mikanani.me/Home/Search?searchstr=Eva
# //*[@id="sk-container"]/div[2]/table/tbody
import threading

import requests
from lxml import etree
import fastapi


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()
