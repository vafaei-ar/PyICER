import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

colors = ['blue','blue','green','red']
marker_list = ['.','*','o','v','^','<','>','H','+','x','D','8','s','p']

def cvs_lead(nam):
    data = pd.read_table(nam+'.csv',delimiter=',').fillna(0)
    print 'List of columns:'
    for i,c in enumerate(data.columns):
        print str(i+1)+'- '+c
    return data

def column_operator(df,l,func):  
    res = func(df[l].values)
    return res 

def dist_analyze(d):
    print '# of members %d'%(d.shape[0])
    print 'mean +- std: %5.3f+-%5.3f '%(d.mean(),d.std())
    print 'perc 25 = %5.3f , median = %5.3f , perc 75 = %5.3f'%(np.percentile(d,25),np.median(d),np.percentile(d,75))
    print '-----------------------------------------'
    
def pval_paired(df,clm1,clm2):    
    if stats.ks_2samp(df[clm1],df[clm2])[1]<0.05:
        print 'P-val: %s Vs. %s is %7.4e'%(clm1,clm2,stats.wilcoxon(df[clm1],df[clm2])[1])
    else:
        print 'P-val: %s Vs. %s is %7.4e'%(clm1,clm2,stats.ttest_rel(df[clm1],df[clm2])[1])

def fpl(df,l1,l2):
    plt.plot(df[l1],df[l2],'o')
    plt.xlabel(r'$'+l1+'$', fontsize=20)
    plt.ylabel(r'$'+l2+'$', fontsize=20)


def fhist(df,l,cl='k',label_x='x',label_y='y'):
    xmin = df[l].min()
    xmax = df[l].max()
    y = pd.DataFrame(df[l].tolist())
    df[l].hist(bins=15,color=cl,alpha=0.8,label=r'$'+l+'$')
    plt.xlim(xmin,xmax)
    plt.xlabel(r'$'+label_x+'$', fontsize=20)
    plt.ylabel(r'$'+label_y+'$', fontsize=20)
