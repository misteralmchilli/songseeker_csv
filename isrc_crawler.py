from tqdm.auto import tqdm
import glob
import json
import time
import requests

#parse isrcsearch.ifpi.org search table results 
def extr_table_info(all_tbls):
    res = [[str(c.text) for c in line.find_elements(selenium_by.TAG_NAME, 'td')] for table in all_tbls for line in table.find_elements(selenium_by.TAG_NAME, 'tr')]
    return [{'isrc':r[-1], 'duration':r[-2], 'year':r[-3], 'version':r[-4], 'title':r[-5], 'author':r[-6]} for r in res if len(r) > 5 and not len(r[-3]) == 0]

#interact with isrcsearch.ifpi.org; first search directly by isrc; then using artist+titel
def crawl_isrc_entry(e, driver, rate_limit_sec=3.2, max_pages=9):
    isrc = str(e['card']['ISRC']).replace('-','')
    driver.get('https://isrcsearch.ifpi.org/')
    url0 = f"https://isrcsearch.ifpi.org/?tab=%22code%22&isrcCode=%22{isrc}%22"
    res_consolidate, dublic_isrc = [], set()
    for check_page in range(max_pages+1):
        if check_page < 2:
            driver.get(url0)
        time.sleep(rate_limit_sec)
        all_tbls = driver.find_elements(selenium_by.TAG_NAME, 'tbody')
        if len(all_tbls)>0:
            res0 = extr_table_info(all_tbls)
            new_isrc = set([r['isrc'] for r in res0])
            if len(new_isrc&dublic_isrc) > 0:
                res_consolidate += [r for r in res0 if r['isrc'] not in dublic_isrc]
                break
            res_consolidate += res0
            dublic_isrc |= new_isrc
        if len(res_consolidate)>0 and len(res0) < 5:
            break
        if check_page == 0: #switch to advanced search using title and artist
            #&version="album" might work sometimes?
            #pagestr = f"&currentPage={check_page+1}" if check_page > 0 else '' #not working without 
            artist = urllib.parse.quote_plus(e['card']['Artist'])
            title = urllib.parse.quote_plus(e['card']['Title'])
            url0 = f'https://isrcsearch.ifpi.org/?tab=%22advanced%22&artistName=%22%5C%22{artist}%5C%22%22&title=%22%5C%22{title}%5C%22%22&fileType=%22audio+files+only%22&itemsPerPage=100'
        else: #click on next page button; selecting page by url not possible/reliable
            num_pages = driver.find_elements(selenium_by.CLASS_NAME, 'v-pagination__list')
            if len(num_pages) > 0:
                max_pages = max([int(c) for c in str(num_pages[0].text).split() if c.isdigit()]+[0])
                if max_pages < check_page:
                    break
            next_buttons = driver.find_elements(selenium_by.CLASS_NAME, 'v-pagination__next')
            if len(next_buttons) != 1:
                break
            next_buttons = next_buttons[0].find_elements(selenium_by.TAG_NAME, 'button')
            if len(next_buttons) != 1:
                break
            driver.execute_script('arguments[0].click()', next_buttons[0])
    return res_consolidate

#limited infos but extensive database; good to fill some last remaining gaps
def add_isrc_info_deezer(extr_info, rate_limit_sec=1.5, add_red=False, verbose=True):
    for e in tqdm(extr_info):
        if 'isrc_red' in e or (not add_red and 'isrc' in e):
            continue
        try:
            oembed_url = f"https://api.deezer.com/2.0/track/isrc:{e['card']['ISRC']}"
            time.sleep(rate_limit_sec)
            response = requests.get(oembed_url)
            entry = response.json()
            keep_keys = ['title','isrc','duration','rank','release_date','artist','album','year']
            if not 'release_date' in entry:
                if verbose:
                    print("Empty for ",e['card']['ISRC'])
                continue
            entry['artist'] = entry.get('artist',{}).get('name','')
            entry['album'] = entry.get('album',{}).get('title','')
            entry['year'] = entry['release_date'][:4]
            e['isrc_red'] = [{k:v for k,v in entry.items() if k in keep_keys}]
        except:
            if verbose:
                print("Error for ",e['card']['ISRC'])

#slow webcrawl; only for special cases
def add_isrc_info_isrcsearch(extr_info, rate_limit_sec=3.2, add_red=False, verbose=True, max_pages=9):
    from selenium import webdriver # !pip install selenium
    from selenium.webdriver.common.by import By as selenium_by
    import urllib.parse
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    for e in tqdm(extr_info):
        if 'isrc_red' in e or (not add_red and 'isrc' in e):
            continue
        try:
            res_consolidate = crawl_isrc_entry(e, driver, rate_limit_sec, max_pages)
            if len(res_consolidate) > 0:
                e['isrc_red'] = res_consolidate
            elif verbose:
                print("Empty for ",e['card']['ISRC'])
        except:
            if verbose:
                print("Error for ",e['card']['ISRC'])
    driver.quit()

#finds most isrc; lots of valid information
def add_isrc_info_musicbrainz(extr_info, rate_limit_sec=1.25, verbose=True):
    import musicbrainzngs #!pip install musicbrainzngs
    musicbrainzngs.set_useragent("name", "0.1", "info@amail.com")
    musicbrainzngs.set_rate_limit(rate_limit_sec,1)
    for e in tqdm(extr_info):
        if 'isrc' in e:
            continue
        try:
            e['isrc'] = musicbrainzngs.get_recordings_by_isrc(e['card']['ISRC'].replace('-',''), ['artists', 'releases'])['isrc']['recording-list']
        except:
            if verbose:
                print("Error for ",e['card']['ISRC'])
