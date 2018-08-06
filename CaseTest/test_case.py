import sys

sys.path.append('/Users/ida/github/AskingKalliopeia/src/')
import case_particle
import mynlp


def prints_info(ph):
    for ph_i, v in ph.items():
        print("token_id " + str(ph_i))
        print("     phrase : " + str(v))
        print("     parent_id : " + str(v.parent_id))
        print("     children : " + str(v.children))
        print("     phrase : [", end="")
        for x in v.words:
            print(str(x.base) + "(" + str(x.pos) + "," + str(x.pos_detail) + "), ", end="")
        print("]")


def main():
    sentence = "ケーキが好きだ。"
    phs = mynlp.convert(sentence, False)
    prints_info(phs)

    cps = case_particle.extract_cp(phs)
    print("cps")
    for cp in cps:
        print(cp["noun"], cp["particle"], cp["predicate"])


if __name__ == "__main__":
    main()
