import requests

Proxy_url = 'http:127.0.0.1:5000/random'
import jsonpath
from config import IMG_PATH
import os
from hashlib import md5
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import Pool

headers = {
    'Cookie': 'wluuid=WLGEUST-E0E1E813-A403-DE4D-670A-410559C3E017; ssoflag=0; lang=zh; _ga=GA1.2.2008638349.1565969446; _gid=GA1.2.267122258.1565969446; log_web_id=5085242245; wlsource=tc_pc_home_search; webp_enabled=1; __utma=115147160.2008638349.1565969446.1565969480.1565969480.1; __utmz=115147160.1565969480.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=115147160.13.10.1565969480; PHPSESSID=kkeou8rgn9ca4dv31hcj2a61de; _gat=1',
    'Host': 'tuchong.com',
    'Referer': 'https://tuchong.com/tags/%E7%BE%8E%E5%A5%B3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}


def get_page(url, num):
    params = {
        'page': num,
        'count': 20,
        'order': 'weekly'
    }
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        try:
            response = requests.get(Proxy_url)
            proxy = response.text
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
            res = requests.get(url, headers=headers, params=params, proxies=proxies)
            if res.status_code == 200:
                return res.json()
        except ConnectionError as e:
            print(e.args)


def get_img_info(res):
    post_list = jsonpath.jsonpath(res, '$.postList.*')
    for i in post_list:
        url = jsonpath.jsonpath(i, 'url')
        site_id = jsonpath.jsonpath(i, 'site_id')
        images = jsonpath.jsonpath(i, 'images.*')
        img_list = []
        for img in images:
            img_id = jsonpath.jsonpath(img, 'img_id')
            img_list.append(img_id)
        list = {
            'site_id': site_id,
            'url': url,
            'img_list': img_list
        }
        yield list

def save_img(url,img_path):
    try:
        resp = requests.get(url)
        if resp.status_code==200:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e)

def get_img_url(url, site_id, img_list):
    image_url='http://photo.tuchong.com/{}/f/{}.jpg'
    img_path = os.path.join(IMG_PATH, site_id[0])
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    for i in img_list:
        url=image_url.format(site_id[0],i[0])
        print(url)
        save_img(url,img_path)

def main(num):
    url = 'https://tuchong.com/rest/tags/%E7%BE%8E%E5%A5%B3/posts?'
    res = get_page(url, num)
    g_obj = get_img_info(res)
    for img in g_obj:
        get_img_url(img['url'][0], img['site_id'], img['img_list'])

if __name__ == '__main__':
    # pool = ThreadPoolExecutor(max_workers=20)
    # for i in range(1,11):
    #     s=pool.submit(main, i)
    #     print(s.result())
    # pool.shutdown()
    pool = Pool()
    groups =range(1,11)
    pool.map(main,groups)
    pool.close()
    pool.join()