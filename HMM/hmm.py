import re
import os
import nltk


atwc = pickle.load(open('pickles/All_tagword_cnt.pkl','rb'))
attw = pickle.load(open('pickles/All_tagstowords.pkl','rb'))
atc = pickle.load(open('pickles/All_tag_cnt.pkl','rb'))
