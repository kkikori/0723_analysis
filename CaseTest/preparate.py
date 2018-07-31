import sys
from pathlib import Path

sys.path.append('/Users/ida/github/AskingKalliopeia/src/')
import case_particle
import tfidf


def _pre_paths():
    f_cases = Path()
    f_mrph = Path()
    stops = Path("/Users/ida/Dropbox/AskQuestion/stopword.txt")
    stop_word_list = tfidf.create_stop_word_list(stops)

    return f_cases, f_mrph, stop_word_list


def Cases_main(Thread_list, Post_list, User_list):
    f_cases, f_mrph, stop_word_list = _pre_paths()
    new_post_pi_list = Post_list.keys()
    Caseframe_list = case_particle.preparate_caseparticle(f_cases, f_mrph, Post_list, new_post_pi_list, stop_word_list)
