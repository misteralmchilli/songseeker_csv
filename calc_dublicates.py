from create_csv import csv_to_rows, clean_title
import os, glob
import jellyfish #!pip install jellyfish
import numpy as np
import matplotlib.pyplot as plt

#either only a few characters of difference or fully enclosed title of orignal in another song
skip_false_friends = [" '54, '74, '90,", "soler sofia", "scatman's world"]

def clean_t(t):
    t = clean_title(t).strip().replace('feat.','(').replace('&','(')
    if t[0] == '(':
        t = t.split(')')[1]
    return (t.split('(')[0]).split('-')[0].strip()

def get_id_card(c):
    csp = c.split('.csv')
    return int((csp[0]+"-aaaa02").split('-aaaa')[1][1:].replace('a','')), int(csp[1])

#create distance bins from csv songseeker csv files
def calc_dublicates_distbin(csv_folder, max_dist = 3, skip_list = skip_false_friends):
    all_data = {}
    skip_list = [s.lower() for s in skip_list]
    for c in glob.glob(csv_folder+'/*.csv'):
        rows = csv_to_rows(c)
        print('Info: reading',c, 'with', len(rows), 'cards')
        key0 = os.path.basename(c)
        for r in rows:
            all_data[key0+r['Card#']] =clean_t(r['Artist'])+' '+clean_t(r['Title'])
    all_keys = sorted(all_data.keys())
    dist_bins = {}
    for i,k0 in enumerate(all_keys):
        v0 = all_data[k0].lower()
        if any([s in v0 for s in skip_list]):
             continue
        for j,k1 in enumerate(all_keys[i+1:]):
            v1 = all_data[k1].lower()
            if any([s in v1 for s in skip_list]):
              continue
            dist0 = int(jellyfish.levenshtein_distance(v0, v1)+0.5)
            min_dist = min(len(v0),len(v1))
            if v1 in v0 or v0 in v1:
                dist0 = 0
            if dist0 <= max_dist:
                if dist0 != 0 and min_dist <= dist0:
                    continue
                dist_bins.setdefault(dist0, []).append([all_data[k0], all_data[k1], k0, k1])
    return dist_bins

#returns two strings with markup tables containing summaries regarding all dublicates in the distance bins
def distbin_to_summary(dist_bins):
    dubl = [d for v in dist_bins.values() for d in v] #consolidate all dublicates
    sort_dubl = [(get_id_card(k[2])[0], get_id_card(k[3])[0], get_id_card(k[2])[1], get_id_card(k[3])[1], k[0]) for k in dubl]
    sort_dubl = [[r[1],r[0],r[3],r[2],r[4]] if r[0]>r[1] else r for r in sort_dubl]
    sort_dubl = list(sorted(sort_dubl, key=lambda x:(x[1], x[0], x[3], x[2])))
    summary, key_order = {}, []
    for k in sort_dubl:
        key0 = str(k[1])+'+'+str(k[0])
        addn = '#%i/#%i %s'%(k[3],k[2],k[4].strip())
        if not key0 in summary:
            key_order.append(key0)
            summary[key0] = addn
        else:
            summary[key0] += '; '+addn
    
    dubl_summary = '|Dublicates for hitster-de-aaaa*| List containing Card#/Card# Artist Title |\n|---|---|\n'
    for k in key_order:
        dubl_summary += '|'+k+'|'+ summary[k]+'|\n'

    editions = sorted(set([int(i) for k in key_order for i in k.split('+')]))
    dist_mat = np.zeros((len(editions), len(editions)), np.int32)
    for i in range(len(editions)):
        for j in range(i+1,len(editions)):
            s = summary.get('%i+%i'%(editions[i],editions[j]), '')
            dist_mat[j, i] = dist_mat[i,j] = s.count(';')+1 if len(s) > 0 else 0
    dist_summary = '| vs. |'+'|'.join(['%04i'%editions[j] for j in range(len(editions))])+'|\n|'+'|'.join('---' for j in range(len(editions)+1))+'|\n'
    for i in range(len(editions)):
        dist_summary+='|%04i:|'%editions[i]+'|'.join([str(dist_mat[i,j]) if i!=j else ' ' for j in range(len(editions))])+'|\n'
    return dubl_summary, dist_summary
    
# create histograms to show decade distribution
def calc_year_distr(csv_folder):
    bins = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030]
    colors = ['orangered', 'sienna', 'silver', 'teal', 'deeppink', 'blue', 'darkgreen']
    plt.rcParams["figure.figsize"] = (18, 3)
    for c in glob.glob(csv_folder+'/*.csv'):
        rows = csv_to_rows(c)
        cname = os.path.basename(c).replace('-de.csv','-de-aaaa0002.csv')[:-4]
        years_clipped = np.clip([int(r['Year']) for r in rows],1960,2029)
        years_clipped = np.clip([int(r['Year']) for r in rows],1960,2029)
        plt.figure()
        n, bins, patches = plt.hist(years_clipped,bins=bins)
        for i,p in enumerate(patches):
            p.set_fc(colors[i])
        xlabels = [str(int(b)) for b in bins]
        xlabels[0] += '<='
        plt.gca().set_xticks(bins)
        plt.gca().set_xticklabels(xlabels)
        plt.title(cname)
        plt.savefig(cname+'_hist.png')
        plt.close()