import sys
from pathlib import Path
import simplejson as json

sys.path.append('/Users/ida/github/AskingKalliopeia/src/')
import case_particle
import tfidf


def _pre_paths():
    f_cases = Path("/Users/ida/Desktop/0608_results/caseparticle")
    f_mrph = Path("/Users/ida/Dropbox/results_asking1/MrphAnalysis")
    stops = Path("/Users/ida/Dropbox/AskQuestion/stopword.txt")
    stop_word_list = tfidf.create_stop_word_list(stops)

    return f_cases, f_mrph, stop_word_list

def _preparate_file_paths():
    fn = Path("file_paths.json")
    if not fn.exists():
        sys.exit()
    group_file_paths = {}
    f = fn.open("r")
    jsonData = json.load(f)
    for group_n, group in jsonData.items():
        file_paths = {}
        for fn, fp in group.items():
            if not fp:
                file_paths[fn] = None
            else:
                file_paths[fn] = Path(fp)
        group_file_paths[group_n] = file_paths
    return group_file_paths

def reading_cases(Thread_list, Post_list, User_list):
    print("reading_cases")
    f_cases, f_mrph, stop_word_list = _pre_paths()
    new_post_pi_list = Post_list.keys()
    Caseframe_list = case_particle.preparate_caseparticle(f_cases, f_mrph, Post_list, new_post_pi_list, stop_word_list)
