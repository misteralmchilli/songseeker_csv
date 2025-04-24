import unicodedata
from tqdm.auto import tqdm
import json
import csv
import hashlib
import time
import requests

#usage:
# extr_info = extract_playlist(playlist_link, cid, cid_secret)
# get_youtube_res(extr_info, trg_path='./youtube_data.json', top_x=10)
# yt_res = json.load(open('./youtube_data.json')) 
# create_songseeker_csv(yt_res, trg_csv_path = 'hitster-de-aaaa0025.csv')

#spotify playlists are mentioned here: https://www.giga.de/artikel/musik-partyspiel-hitster-liederlisten-von-spotify-auf-einen-blick--w3gqq3r7qx
#  'hitster':'https://open.spotify.com/playlist/26zIHVncgI9HmHlgYWwnDi'
#   'sommer':'https://open.spotify.com/playlist/15hZ0ez6sHYhTeCCshxJTN'
#  'bayern1':'https://open.spotify.com/playlist/2zWVMuxHcoLgThgaBhDzmK'
#    'bingo':'https://open.spotify.com/playlist/58y9xPPIRWd8tqlOaKoDOI'
# 'guilty_p':'https://open.spotify.com/playlist/2u0vgWYqU1TWVcDehJnZuN'
#cid&cid_secret for access to Spotify API: https://developer.spotify.com/
def extract_playlist(playlist_link, cid, cid_secret):
    import spotipy #!pip install spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    client_credentials_mgmt = SpotifyClientCredentials(client_id=cid, client_secret=cid_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_mgmt)
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    extr_info = []
    for i in range(4):
        old_num = len(extr_info)
        for track in sp.playlist_tracks(playlist_URI, offset=len(extr_info)) ["items"]:
            # To get track name
            track_name = track["track"]["name"]
            artist_name = track["track"]["artists"][0]["name"]
            album_name = track["track"]["album"]["name"]
            album_date = track["track"]["album"]['release_date']
            extr_info.append({'Card#':len(extr_info)+1, 'Artist':artist_name, 'Title':track_name, 'album':album_name,'album_date':album_date, 'Year':album_date[:4]})
        if  len(extr_info)-old_num < 8:
            break
    return extr_info

# find associated videos per search term. This is a slow process
# top_x number of search results; 5 or 10 give good results; saves result to json so experiments with get_best_url systematic can work
def get_youtube_res(extr_info, trg_path='./youtube_data.json', top_x=10):
    import yt_dlp #!pip install yt-dlp
    yt_res = []
    for m in tqdm(extr_info):
        term = 'music video '+m['Title']+' by '+m['Artist']+' from '+m.get('Year', m.get('album_date','0000')[:4])
        yt_res.append({'assoc':m,'searchterm':term})
        with yt_dlp.YoutubeDL({'ignore_errors':True, 'ignoreerrors':True, 'quiet':True}) as ytdl:
            try:
                entries = ytdl.sanitize_info(ytdl.extract_info(f"ytsearch{top_x}:{term}", download=False))['entries']
                filtered_cont = [{k:v for k,v in s.items() if k in keep_details} for s in entries if not s is None]
                yt_res[-1]['entries'] = filtered_cont
            except:
                pass
    json.dump(yt_res, open(trg_path,'wt'))

# convert emoticons and non-ascii chars.
# based on https://stackoverflow.com/questions/43797500/python-replace-unicode-emojis-with-ascii-characters
def de_emojify(s):
    ret = ""
    for c in s:
        try:
            c.encode("ascii")
            ret += c
        except UnicodeEncodeError:
            try:
                 ret += "[" + unicodedata.name(c) + "]"
            except ValueError:
                 ret += "[x]"
    return ret

def get_hashed_info(entry):
    important_info = str(entry['title']) + entry.get('uploader',str(entry.get('uploader_id')).replace('@',''))
    return hashlib.sha256(important_info.encode()).hexdigest()

# choose best-suiting source for music video; has some bugs/quirks still
# this uses text from all search results per entry to better estimate the true release date
def get_best_url(e_all, a):
    skip_live = not ' live ' in  a['Title'].lower()
    keys0, fnd_title_orig = ["title", "uploader_id"], a['Title'].split('Single')[0].split('- Live')[0].strip()
    acc_ind = ["(Official ", "VEVO", "@Official"]
    rej_ind, fnd_title = ['Remix','REMIX','remix'], fnd_title_orig #+(['Live'] if skip_live else [])
    for pass0 in range(4):
        best_matches = [e for e in e_all if any([any([i in e.get(k,'') for i in acc_ind]) for k in keys0 if k in e and not e[k] is None])]
        best_matches = [b for b in best_matches if not any([any([i in b.get(k,'') for i in rej_ind]) for k in keys0 if k in b and not b[k] is None])]
        if len(best_matches) > 0:
            if pass0 > 0:
                best_matches = sorted(best_matches, key=lambda x: x['view_count'])
            break
        if pass0 >= 1: # allow splitting of alternative versions
            fspl, idx_use = fnd_title_orig.split(')'), pass0-1
            if len(fspl) <= idx_use:
                break
            fnd_title = fspl[idx_use].lower().strip().replace('(', '- ')
            if len(fnd_title) < 10:
                break
        if pass0 == 1: #relax title capitalization
            for e in e_all:
                e['title_lower'] = de_emojify(e['title']).lower().replace('(', '- ')
            keys0 = ['title_lower']
        acc_ind = [fnd_title]
    if len(best_matches) == 0:    
        return {}
    chk_str = [b['description']+' ' +b['fulltitle'] for b in best_matches]
    chk_str0 = [b for b in chk_str if fnd_title.lower() in b.lower()]
    chk_str = de_emojify(" ".join(chk_str0 if len(chk_str0) > 0 else chk_str))
    min_year = min([int(y) for y in chk_str.replace(']',' ').replace('.',' ').split() if len(y)==4 and y.isdigit() and (y[:2]=='20' or y[:2]=='19')]+[int(a.get('album_date','3000')[:4])])
    return {'URL':'https://www.youtube.com/watch?v='+best_matches[0]['id'], 
            'Youtube-Title':de_emojify(best_matches[0]['title']).replace(',','_').replace('"',' ')[:80], 
            'Hashed Info':get_hashed_info(best_matches[0]),
            'Year':min_year}

def rows_to_songseeker_csv(rows, trg_csv_path):
    fieldnames = ['Card#', 'Artist', 'Title', 'URL', 'Hashed Info', 'Youtube-Title', 'Year']
    with open(trg_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            k_rem = set(list(row.keys())).difference(set(fieldnames))
            row_cp = dict(row)
            for k in k_rem:
                _ = row_cp.pop(k,None)
            writer.writerow(row_cp)

def csv_to_rows(src_csv_path):
    with open(src_csv_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        fieldnames = list(reader.fieldnames)
        return list([row for row in reader])

def get_correct_entry(row, yt_res):
    try:
        return [e for e in [r for r in yt_res if int(r['assoc']['Card#']) == int(row['Card#'])][0]['entries'] if e['id'] in row['URL']][0]
    except:
        return None

#fix missing 'Hashed Info' data
def add_missing_hash(rows, yt_res, use_csv_data=False):
    for row in tqdm(rows):
        if len(row.get('Hashed Info','')) > 0:
            continue
        entry = get_correct_entry(row, yt_res)
        if entry == None: #not from the cached youtube search results
            try:
                #based on original code from 
                #https://github.com/andygruber/songseeker-hitster-playlists/blob/main/verifyYoutubeLinks.py
                time.sleep(1.0)
                oembed_url = f"https://www.youtube.com/oembed?url={row['URL']}"
                response = requests.get(oembed_url)
                response.raise_for_status()  # Raises an error for bad responses
                entry = response.json()
                entry['uploader'] = entry['author_name']
            except:
                #cannot access online data
                if use_csv_data:#assume data from 
                    entry = {'title':row['Title'],'uploader':row['Artist']}
                else:
                    continue
        row['Hashed Info'] = get_hashed_info(entry)

#loaded youtube search results (which also include data from spotify list) -> csv
def create_songseeker_csv(yt_res, trg_csv_path = './hitster-de-aaaa0025.csv'):
    csv_res = []
    for r in yt_res:
        burl = get_best_url(r.get('entries',[]), r['assoc'])
        burl.update(r['assoc'])
        csv_res.append(burl)
    rows = sorted(csv_res,  key=lambda x: x['Card#'])
    rows_to_songseeker_csv(rows, trg_csv_path)