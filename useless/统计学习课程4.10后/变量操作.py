import numpy as np

#变量估计
def est(x,y,n):
    hb1 = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
    hb0 = np.mean(y) - hb1 * np.mean(x)
    hsigmafang = np.var(y-hb0-hb1*x)
    sebeta0 = np.sqrt(hsigmafang * (1 / n + np.mean(x) ** 2 / np.sum((x - np.mean(x))**2)))
    sebeta1 = np.sqrt(hsigmafang / np.sum((x - np.mean(x))**2))
    return hb1,hb0,hsigmafang,sebeta1,sebeta0

#求置信区间
def confidence(hb1, hb0, sebeta1, sebeta0,a):
    uhb1 = hb1+a*sebeta1
    dhb1 = hb1-a*sebeta1
    uhb0 = hb0+a*sebeta0
    dhb0 = hb0-a*sebeta0
    return uhb1,dhb1,uhb0,dhb0

