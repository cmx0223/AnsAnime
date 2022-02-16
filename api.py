"""
/v1/search?str=Eva
/v1/download?list={}
"""

import threading

import requests
from lxml import etree
import fastapi

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/63.0.3239.132 Safari/537.36"}


def search(str):
    search_result = []
    timer = [0]
    url = 'https://mikanani.me/Home/Search?searchstr=' + str
    data = requests.get(url, headers=headers, ).content.decode()
    # print(data)
    html = etree.HTML(data)
    preprocess = html.xpath('//*[@id="sk-container"]/div[2]/table/tbody/tr')
    '''
    <tr class="js-search-results-row" data-itemindex="2" style="">
                            <td>
                                <a href="/Home/Episode/f7eddde43b67498547b711f34e74da4db5df4c5f" target="_blank" class="magnet-link-wrap">[&#x96EA;&#x98D8;&#x5DE5;&#x4F5C;&#x5BA4;][&#x65B0;&#x798F;&#x97F3;&#x6218;&#x58EB;&#x5267;&#x573A;&#x7248;3.0&#x2B;1.0 THRICE UPON A TIME / &#x30B7;&#x30F3;&#x30FB;&#x30A8;&#x30F4;&#x30A1;&#x30F3;&#x30B2;&#x30EA;&#x30AA;&#x30F3;&#x5267;&#x573A;&#x7248; / Evangelion: 3.0&#x2B;1.0 Thrice Upon a Time][1920x816][&#x7B80;&#x4F53;&#x5185;&#x5D4C;]</a>
                                <a data-clipboard-text="magnet:?xt=urn:btih:f7eddde43b67498547b711f34e74da4db5df4c5f&amp;tr=http%3a%2f%2ft.nyaatracker.com%2fannounce&amp;tr=http%3a%2f%2ftracker.kamigami.org%3a2710%2fannounce&amp;tr=http%3a%2f%2fshare.camoe.cn%3a8080%2fannounce&amp;tr=http%3a%2f%2fopentracker.acgnx.se%2fannounce&amp;tr=http%3a%2f%2fanidex.moe%3a6969%2fannounce&amp;tr=http%3a%2f%2ft.acg.rip%3a6699%2fannounce&amp;tr=https%3a%2f%2ftr.bangumi.moe%3a9696%2fannounce&amp;tr=udp%3a%2f%2ftr.bangumi.moe%3a6969%2fannounce&amp;tr=http%3a%2f%2fopen.acgtracker.com%3a1096%2fannounce&amp;tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce" class="js-magnet magnet-link">[复制磁连]</a>
                            </td>
                            <td>3.9GB</td>
                            <td>2021/09/11 22:08</td>
                            <td>
                                <a href="/Download/20210911/f7eddde43b67498547b711f34e74da4db5df4c5f.torrent">
                                    <img src="/images/download_icon_blue.svg" style="margin-left: 2px;width: 20px;height:15px;">
                                </a>
                            </td>
                        </tr>
    '''

    for item in preprocess:
        # timer = item.xpath('./@data-itemindex')
        title = item.xpath('./td[1]/a[1]/text()')
        mag = item.xpath('./td[1]/a[2]/@data-clipboard-text')
        size = item.xpath('./td[2]/text()')
        time = item.xpath('./td[3]/text()')
        # https://mikanani.me/Download/20121117/44a7e3dff27413193f88ce7d79087e4f445a0402.torrent
        torrent_url = item.xpath('./td[4]/a/@href')
        torrent_url[0] = 'https://mikanani.me' + torrent_url[0]
        information = []
        search_result.append([])
        information = information + title + mag + size + time + torrent_url + timer
        search_result[int(timer[0])].append(information)
        timer[0] += 1
    return search_result


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


# print(search('eva')[5][0])
