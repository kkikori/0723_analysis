import sys
from pathlib import Path
import simplejson as json
from .extract_caseparticle import extract_caseparticle_main

sys.path.append('/Users/ida/github/AskingKalliopeia/src/')
import case_particle
import tfidf


def _pre_paths(group_n):
    f_cases = Path("/Users/ida/Desktop/0723_resutls/caseparticle")
    f_cases = f_cases / group_n
    # f_mrph = Path("/Users/ida/Dropbox/results_asking1/MrphAnalysis")
    stops = Path("/Users/ida/Dropbox/AskQuestion/stopword.txt")
    stop_word_list = tfidf.create_stop_word_list(stops)

    return f_cases, stop_word_list


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


def reading_cases(group_n, Post_list):
    print("reading_cases")
    f_cases, stop_word_list = _pre_paths(group_n)
    Caseframe_list = extract_caseparticle_main(Post_list, stop_word_list)
    case_particle.update_cases_file(f_cases, Caseframe_list.keys(), Caseframe_list)
