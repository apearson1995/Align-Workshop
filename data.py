import numpy as np
from scipy.io import loadmat

########################################################
# ----------------- Cleaning the Data -----------------#
########################################################

hiv_data = loadmat('flhivdata.mat')

# Got the keys by inspecting the data manually

dnt    = hiv_data["dnt"][0]

ctrl_1 = hiv_data["lc1"][0]
ctrl_5 = hiv_data["lc5"][0]

ptb    = hiv_data["ptb"][0]
ptc    = hiv_data["ptc"][0]
ptd    = hiv_data["ptd"][0]

min_len = min(len(dnt),len(ctrl_1),len(ctrl_5),len(ptb),len(ptc),len(ptd))

def chop(seq):
    ans    = min_len*["o"]
    tokens = list(seq)
    for i in xrange(min_len):
        ans[i] = tokens[i]
    return ''.join(ans)

dnt    = chop(dnt)
ctrl_1 = chop(ctrl_1)
ctrl_5 = chop(ctrl_5)

ptb    = chop(ptb)
ptc    = chop(ptc)
ptd    = chop(ptd)

HIV_names = ["dnt", "ptb", "ptc", "ptd", "ctrl1", "ctrl5"]
HIV_seqs  = [dnt, ptb, ptc, ptd, ctrl_1, ctrl_5]