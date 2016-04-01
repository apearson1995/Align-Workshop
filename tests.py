import numpy as np

########################################################
# ---------------- Tests for Atendees -----------------#
########################################################

def test_prop_diff(func):
    if func("ATTGAC","ATGGCC") < .34 and func("ATTGAC","ATGGCC") > .32:
        return "CONGRTULATIONS YOUR FUNCTION IS CORRECT :) !"
    else:
        return "You made a mistake, please try again"




        