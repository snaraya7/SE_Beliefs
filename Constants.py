"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess belief 1 Corbat ́o’s law
License: See LICENSE file
"""

import math

"""
period constants
"""
one_year = 31556926
one_month = 2629743
one_day = 86400

# train_window_size =  24 * one_month
# test_window_size = 48 * one_month


"""
Methodology parameters
"""

SHOULD_NORMALIZE = True




SIG_LEVEL = 0.01
MIN_MOD_RHO = 0.35
STRONG_MOD_RHO = 0.5
NUM_RELEASES_TO_CONSIDER = math.inf
MIN_NUM_FILES_PER_RELEASE = 2 #18
MAX_NUM_FILES_PER_RELEASE =  math.inf #50 #85 #math.inf

SAMPLE_LIMIT = math.inf

TEST_WINDOW = (3 * one_month)
MIN_TRAIN_DAYS = 1
MAX_TRAIN_DAYS = math.inf
LIMIT_BIAS = False
# MIN_NUM_FILES_ALL_RELEASES = 83 #83 #29 or 779

# PEAR_r_INDEX = 0
# PEAR_p_INDEX = 1
# SPEAR_r_INDEX = 2
# SPEAR_p_INDEX = 3
#
# SWAP = False # experimental

"""
entropy related
"""
# phi = 10
BURST_SIZE = 3 #commit count (no. of changes)
BURST_GAP = 14 * one_day #biweekly dambros (but check)

"""
Beliefs
"""

LINE_INSERTIONS = "insertions"
LINE_DELETIONS = "deletions"
LOC = "loc"
MORE_COMMITS = "more_commits"
MORE_DEVELOPERS = "more_developers"
MORE_BUG_FIXES = "more_bug_fixes"
COMPLEX_CODE_CHANGE = "complex_code_change"
LESS_OWNER_CONTRIB = "less_owner_contrib"

RECENTLY_CREATED = "recently_created" #Bug Prediction based on fine-grained module histories - age( # of days in existence )
RECENTLY_CHANGED = "recently_changed"
RECENTLY_BUG_FIXED = "recently_bug_fixed"

CALLED_BY = "called_by"
CALLING = "calling"

LARGE_COMMITS = "large_commits"

# ALL_BELIEFS = [LINE_INSERTIONS, LINE_DELETIONS, LOC, MORE_COMMITS,
#                MORE_DEVELOPERS, MORE_BUG_FIXES, COMPLEX_CODE_CHANGE, LESS_OWNER_CONTRIB, RECENTLY_CREATED, RECENTLY_CHANGED, RECENTLY_BUG_FIXED,
#                LARGE_COMMITS]

ALL_BELIEFS = [ LINE_INSERTIONS, LINE_DELETIONS,  MORE_COMMITS,
               MORE_DEVELOPERS, MORE_BUG_FIXES, COMPLEX_CODE_CHANGE, LESS_OWNER_CONTRIB, RECENTLY_CHANGED, RECENTLY_BUG_FIXED,
               LARGE_COMMITS]

BELIEF_AGREEMENT_MAP = {}

BELIEF_AGREEMENT_MAP[COMPLEX_CODE_CHANGE] = 76
BELIEF_AGREEMENT_MAP[MORE_DEVELOPERS] = 64
BELIEF_AGREEMENT_MAP[LINE_INSERTIONS] = 61
BELIEF_AGREEMENT_MAP[RECENTLY_CHANGED] = 58
BELIEF_AGREEMENT_MAP[LARGE_COMMITS] = 57
BELIEF_AGREEMENT_MAP[RECENTLY_BUG_FIXED] = 49
BELIEF_AGREEMENT_MAP[MORE_BUG_FIXES] = 48
BELIEF_AGREEMENT_MAP[MORE_COMMITS] = 46
BELIEF_AGREEMENT_MAP[LINE_DELETIONS] = 35
BELIEF_AGREEMENT_MAP[LESS_OWNER_CONTRIB] = 30


BELIEF_PRETTY_NAMEMAP = {}


# BELIEF_PRETTY_NAMEMAP[LINE_INSERTIONS] = 'B3: Insertions'
# BELIEF_PRETTY_NAMEMAP[LINE_DELETIONS] = 'B9' \
#                                         ': Deletions'
# BELIEF_PRETTY_NAMEMAP[MORE_COMMITS] = 'B8: More Commits'
# BELIEF_PRETTY_NAMEMAP[MORE_DEVELOPERS] = 'B2: More Developers'
# BELIEF_PRETTY_NAMEMAP[MORE_BUG_FIXES] = 'B7: More Bug Fixes'
# BELIEF_PRETTY_NAMEMAP[COMPLEX_CODE_CHANGE] = 'B1: Complex Change'
# BELIEF_PRETTY_NAMEMAP[LESS_OWNER_CONTRIB] = 'B10: Owner Contribution'
# BELIEF_PRETTY_NAMEMAP[RECENTLY_CHANGED] = 'B4: Recent Change'
# BELIEF_PRETTY_NAMEMAP[RECENTLY_BUG_FIXED] = 'B6: Recent Bug fix'
# BELIEF_PRETTY_NAMEMAP[LARGE_COMMITS] = 'B5: Large Commits'

BELIEF_PRETTY_NAMEMAP[LINE_INSERTIONS] = 'B3'
BELIEF_PRETTY_NAMEMAP[LINE_DELETIONS] = 'B9'
BELIEF_PRETTY_NAMEMAP[MORE_COMMITS] = 'B8'
BELIEF_PRETTY_NAMEMAP[MORE_DEVELOPERS] = 'B2'
BELIEF_PRETTY_NAMEMAP[MORE_BUG_FIXES] = 'B7'
BELIEF_PRETTY_NAMEMAP[COMPLEX_CODE_CHANGE] = 'B1'
BELIEF_PRETTY_NAMEMAP[LESS_OWNER_CONTRIB] = 'B10'
BELIEF_PRETTY_NAMEMAP[RECENTLY_CHANGED] = 'B4'
BELIEF_PRETTY_NAMEMAP[RECENTLY_BUG_FIXED] = 'B6'
BELIEF_PRETTY_NAMEMAP[LARGE_COMMITS] = 'B5'


"""
HTML Color Codes
"""

yellow = '#F1C40F'
violet = '#9B59B6'
gray = '#BDC3C7'
black = '#000000'
orange = '#DC7633'
green_light = '#82E0AA'
purple_light = '#F4ECF7'
orange_light = '#FBEEE6'
white = '#FFFFFF'
blue = '#5DADE2'

LINE_WIDTH = 2
FONT_SIZE = 30
FONT_SIZE_MED = 10
FONT_SIZE_SMALL = 5
FONT_NAME = 'Times New Roman'

RHO_SYMBOL = 'ρ'

CHOSEN_PROGRAMMING_LANGUAGES = ['C', 'C++', 'C#', 'JAVA', 'VB']
# CHOSEN_PROGRAMMING_LANGUAGES = ['C', 'C++', 'C#', 'JAVA', 'VB', 'COBOL','SQL','PROGRESS','POWERBUILDER','VC++','ADA','PASCAL','NATURAL']
CHOSEN_PROGRAMMING_LANGUAGES_SET_2 = [ 'COBOL','SQL','PROGRESS','POWERBUILDER','VC++','ADA','PASCAL','NATURAL']





