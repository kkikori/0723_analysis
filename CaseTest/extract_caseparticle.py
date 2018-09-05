import sys

sys.path.append('/Users/ida/github/AskingKalliopeia/src/')
import case_particle
import mynlp


def _extract_from_sentence(post):
    si = 0
    while si < len(post.sentences):
        sentence = post.sentences[si]
        if sentence.body[-1] == "、" and si != len(post.sentences) - 1:
            sis = [si, si + 1]
            si += 1
            s = sentence.body + post.sentences[si].body
        else:
            sis = si
            s = sentence.body

        phs = mynlp.convert(s, False)
        cps = case_particle.extract_cp_and_embed_class(phs, post.belong_th_i, post.id, sis, post.user_id)
        si += 1
    return cps


def extract_caseparticle_main(Post_list, stopword_list):
    Caseframe_list = {}
    for pi, post in Post_list.items():
        print("           pi =",pi)
        cps = _extract_from_sentence(post)
        if len(cps) == 0:
            continue
        for cp in cps:
            if cp in cps:
                if cp["noun"] in stopword_list:
                    continue
                if cp["noun"] not in Caseframe_list.keys():
                    Caseframe_list[cp["noun"]] = case_particle.CaseframeClass(noun=cp["noun"])
                Caseframe_list[cp["noun"]].pairs.append(cp["cp"])

    return Caseframe_list

