import ssl
import os
import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库
from urllib.request import urlretrieve

pics_path = 'pics'
# 下载图片存放路径
def init_path():
    if not os.path.exists(pics_path):
        print('path not exist')
        os.mkdir(pics_path)

# 下载图片
def download_pics(url, page_index):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
    # r = requests.get('https://movie.douban.com/top250', headers=header)

    # 传入URL
    # r = requests.get('https://www.csdn.net/')
    r = requests.get(url, headers=header)
    # 200 说明请求成功了
    print(f'url status: {r.status_code}')
 
    # 解析URL
    soup = BeautifulSoup(r.text, 'html.parser')
    # 通过article去查找内容
    content = soup.find('div', attrs = {'class': 'article'})
    # print(content)

    #再通过img去查找具体的内容
    images = content.find_all('img')
    # print(images)

    # 从具体内容里提取电影名和链接并放到列表里
    pic_link_list = [image['src'] for image in images]
    pic_name_list = [image['alt'] for image in images]
    # print(pic_name_list)
    # print(pic_link_list)

    # 遍历列表去下载电影海报
    # for name, link in zip(pic_name_list, pic_link_list):
    for i in range(0, len(pic_link_list)):
        # SSL: CERTIFICATE_VERIFY_FAILED
        ssl._create_default_https_context = ssl._create_unverified_context
        # 给图片加个序号：根据所在页数和页里的位置
        # index = page*25 + pic_name_list.index(name) + 1
        # 下载到本地
        # urlretrieve(link, f'{download_path}/{index}.{name}.jpg')
        name = pic_name_list[i]
        #给电影名字前面加个顺序号
        # print(f'./pics/{page_index*25 + i + 1}.{name}.jpg')
        urlretrieve(pic_link_list[i], f'./pics/{page_index*25 + i + 1}.{name}.jpg')

    print(f'download finished in {url}')


# Entry
def main():
    page_link_address = ['https://movie.douban.com/top250', ]
    for i in range(1, 10):
        page_link_address.append(f'https://movie.douban.com/top250?start={25*i}&filter=')

    # print(page_link_address)

    # 初始化存放路径
    init_path()

    # 循环下载10页的内容
    for i in range(len(page_link_address)):
        download_pics(page_link_address[i], i)

# 代码文件执行的入口
if __name__ == "__main__":
    main()