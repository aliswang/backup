import os
import copy
import time
import csv
import numpy as np
from IPython.display import clear_output
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist
from scipy.stats import pearsonr
global _string
global _key_list
global _value_list
global dic

def rev_num(num):
    if(num == 0):
        return 0
    else:
        return num + rev_num(num - 1)
def count_inp(check_inp, inp):
    _=check_inp.keys()
    for i in list(check_inp.keys()):
        if(i in inp):
            try:
                count_inp(check_inp[i], inp)
            except:
                check_inp[i] += 1
def init_tree(check):
    out = {}
    tmp = {}
    check_list = copy.deepcopy(check)
    check_list_tmp = copy.deepcopy(check_list[0])
    check_list.append(check_list_tmp)
    for i in check_list: 
        while(i != []):
            if(i[0] not in list(tmp.keys())):
                if(len(i) == 1):
                    tmp[i[0]] = dict()
                    tmp[i[0]] = 0
                else:
                    tmp[i[0]] = dict()
            tmp = tmp[i[0]]
            i.remove(i[0])
        tmp = out
    return out
def transor_list_recursive(tmp):
    global _string
    global _key_list
    global _value_list
    c = tmp.keys()
    for i in list(tmp.keys()):
        _string += str(i) + ","
        try:
            transor_list_recursive(tmp[i])
        except:
            _key_list.append(_string.split(',')[:-1])
            _value_list.append(tmp[i])
            _string = ""
def dict_tree_tensor_list(dic_i, num=3, cut=20):
    global _string
    global _key_list
    global _value_list
    _string = ""
    _key_list = []
    _value_list = []
    out_dic = {}
    transor_list_recursive(dic_i)
    try:
        tmp = _key_list[0]
        out = [list(map(int,list(_key_list[0])))]
        for i in range(1, len(_key_list)):
            if(len(_key_list[i]) < num + 1):
                set_n = num + 1 - len(_key_list[i])
                _out_part = []
                _out_part.extend(tmp[:set_n])
                _out_part.extend(_key_list[i])
                out.append(list(map(int, _out_part)))
                tmp = _out_part
            else:
                out.append(list(map(int, _key_list[i])))
                tmp = _key_list[i]
        #out
        for j in range(len(_value_list)):
            if(_value_list[j] >= cut):
                if(tuple(out[j]) not in out_dic):
                    out_dic[tuple(out[j])] = list()
                    out_dic[tuple(out[j])] = _value_list[j]
                else:
                    out_dic[tuple(out[j])] += _value_list[j]
    except:
        pass
    return out_dic
def aprioriGen(Lk, k):
    retList = [] # 滿足條件的頻繁項集
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[: k-2]
            L2 = list(Lk[j])[: k-2]
            L1.sort()
            L2.sort()
            if L1 == L2 :
                retList.append(list(set(Lk[i]) | set(Lk[j])))
    return retList
def del_(dic, cut=20):
    q = list(dic.keys())
    for i in q:
        if(dic[i] < cut):
            del dic[i]
def count_fir(inp):
    global dic
    for i in inp:
        if((i,) not in dic):
            dic[(i,)] = list()
            dic[(i,)] = 1
        else:
            dic[(i,)] += 1
def apriori(cut, txt_name, out_file_name_, n=2):
    global _string
    global _key_list
    global _value_list
    global dic
    dic = {}
    _string = []
    _key_list = []
    _value_list = []
    time_total = time.time()
    with open(txt_name, 'r') as a: 
        len_txt = sum(1 for line in a)
    with open(txt_name, 'r') as a:
        for i in range(len_txt):
            b = list(map(int, a.readline().replace('\n','').split(',')))
            count_fir(b)
        del_(dic, cut)
    check_dic = {}
    num = 1
    while(True):
        with open(txt_name, 'r') as c:
            if(num == n):
                break
            tStart_c = time.time()
            a = list(dic.keys())
            t = []
            con = False
            for i in a:
                if(len(i)==num):
                    t.append(i)
            check=aprioriGen(t,num+1)
            if(check==[]):
                break
            check.sort()
            check2=init_tree(check)
            for i in range(len_txt):
                b=list(map(int,c.readline().replace('\n','').split(',')))
                count_inp(check2,b)
            dic.update(dict_tree_tensor_list(check2, num, cut=cut))
            num += 1
            time.asctime( time.localtime(time.time()) )
    with open(out_file_name_, "w") as w:
        for i in list(dic.keys()):
            out_string = str(i) + ":" + str(dic[i]) + "\n"
            out_string = out_string.replace("(","").replace(")","")
            if(len(list(i))==1):
                out_string = out_string.replace(",","")
            w.write(out_string)
    dic = {}
    
def read_n_seq(file_name, n):
    out_seq_name = []
    out_seq_count = []
    with open(file_name, "r") as r:
        line = r.readline()
        while(line):
            n_seq = line.count(",") + 1
            if(n_seq == n):
                line_split = line.split(":")
                out_seq_name.append(line_split[0])
                out_seq_count.append(int(line_split[1]))
            line=r.readline()
    return out_seq_name, out_seq_count

def sort_twolist(list1, list2):
    for c in range(len(list1)):
        for i in range(0, len(list1)-1):
            if(list1[i] < list1[i+1]):
                list1[i], list1[i+1] = list1[i+1], list1[i]
                list2[i], list2[i+1] = list2[i+1], list2[i]
    return list1, list2

def plt_format(seq_inp1x, seq_inp1y, seq_inp2x, seq_inp2y, run_=False):
    seq1x = seq_inp1x[:]
    seq1y = seq_inp1y[:]
    seq2x = seq_inp2x[:]
    seq2y = seq_inp2y[:]
    seq_list = []
    for i in seq1y:
        seq_list.append(i)
    for i in seq2y:
        if(i not in seq_list):
            seq_list.append(i)
    if(run_):
        with open("dif_set_tmp.txt", "w") as w:
            w.write(str(set(seq1y).symmetric_difference(set(seq2y))))
            
    for i in range(len(seq1y)):
        seq1y[i] = seq_list.index(seq1y[i])
    for i in range(len(seq2y)):
        seq2y[i] = seq_list.index(seq2y[i])
    seq1y, seq1x = sort_twolist(seq1y, seq1x)
    seq2y, seq2x = sort_twolist(seq2y, seq2x)
    plt.bar(seq1y, seq1x, alpha=0.5, width=1)
    plt.bar(seq2y, seq2x, alpha=0.5, width=1)
    plt.show()
    total = 0
    for i in seq_list:
        if(i in seq_inp2y):
            out = seq_inp2x[seq_inp2y.index(i)]
        else:
            out = 0
        if(i in seq_inp1y):
            inp = seq_inp1x[seq_inp1y.index(i)]
        else:
            inp = 0
        total += pow(out - inp, 2)
    print("mse=", pow(total, 0.5))
    seq1 = np.zeros((len(seq_list),))
    seq2 = np.zeros((len(seq_list),))
    for i, j in zip(seq1x, seq1y):
        seq1[int(j)] = int(i)
    for i, j in zip(seq2x,seq2y):
        seq2[int(j)] = int(i)
    dist = pdist(np.vstack([seq1, seq2]),'cosine')
    print("cos",float(dist))
    pccs = pearsonr(seq1, seq2)
    print("pccs", pccs)
    
    

def plt_format_plot(seq_inp1x, seq_inp1y, seq_inp2x, seq_inp2y):
    seq1x = seq_inp1x[:]
    seq1y = seq_inp1y[:]
    seq2x = seq_inp2x[:]
    seq2y = seq_inp2y[:]
    seq_list = []
    for i in seq1y:
        seq_list.append(i)
    for i in seq2y:
        if(i not in seq_list):
            seq_list.append(i)
    for i in range(len(seq1y)):
        seq1y[i] = seq_list.index(seq1y[i])
    for i in range(len(seq2y)):
        seq2y[i] = seq_list.index(seq2y[i])
    seq1y, seq1x = sort_twolist(seq1y, seq1x)
    seq2y, seq2x = sort_twolist(seq2y, seq2x)
    plt.plot(seq1y, seq1x, alpha=0.5)
    plt.plot(seq2y, seq2x, alpha=0.5)
    plt.show()
    total = 0
    for i in seq_list:
        if(i in seq_inp2y):
            out = seq_inp2x[seq_inp2y.index(i)]
        else:
            out = 0
        if(i in seq_inp1y):
            inp = seq_inp1x[seq_inp1y.index(i)]
        else:
            inp = 0
        total += pow(out - inp, 2)
    print("mse=", pow(total, 0.5))
    seq1 = np.zeros((len(seq_list),))
    seq2 = np.zeros((len(seq_list),))
    for i, j in zip(seq1x, seq1y):
        seq1[int(j)] = int(i)
    for i, j in zip(seq2x, seq2y):
        seq2[int(j)] = int(i)
    dist = pdist(np.vstack([seq1, seq2]), 'cosine')
    print("cos", float(dist))
    pccs = pearsonr(seq1, seq2)
    print("pccs", pccs)
    
def bigest_num_inlist(list_inp, n):
    max_num = list_inp[:n]
    num_index = np.fromiter(iter(range(n)), dtype=int)
    max_num, num_index = sort_twolist(max_num, num_index)
    for i in range(n, len(list_inp)):
        if(list_inp[i] > max_num[-1]):
            max_num[-1] = list_inp[i]
            num_index[-1] = i
            max_num, num_index = sort_twolist(max_num, num_index)
    return num_index.tolist()
def format_inpdata(data):
    input_data_num = []
    for i in data:
        tmp = []
        for j in range(len(i)):
            if(i[j] == 1):
                tmp.append(j)
        if(tmp != []):
            input_data_num.append(tmp)
    return input_data_num
def format_outdata(out_data, use_avg, avgbase=1, limit=0.5, bigest_num=10):
    out_data_num = []
    sum_num = 0
    for i in out_data:
        tmp = []
        if(use_avg):
            limit = sum(i) / len(i) * avgbase
        for j in range(len(i)):
            if(i[j] > limit):
                tmp.append(j)
        if(len(tmp) > bigest_num):
            tmp = bigest_num_inlist(i, bigest_num)
        if(tmp != []):
            out_data_num.append(tmp)
        sum_num += len(tmp)
    print("total_data_long:", sum_num)
    return out_data_num
def writedatafile(input_data_num, out_data_num, inpdata_file_name="input_data_num.txt", outdata_file_name="out_data_num.txt"):
    with open(outdata_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in out_data_num:
            writer.writerow(i)
    with open(inpdata_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in input_data_num:
            writer.writerow(i)