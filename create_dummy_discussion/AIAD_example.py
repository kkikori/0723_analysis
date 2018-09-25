import fetch_api


def elephant():
    # 一個前の投稿
    token_elephant = fetch_api.get_access_token("Elephant", "test")
    d = {"title": "publicness",
         "body": "I think ... "}
    fetch_api.create_thread(token_elephant, d)
    d = {"title": "No.4 should be abolished",
         "body": "Since there is a possibility that the report of the present stage has been conveniently reported by editing,\n does not it change so much even if it is abolished?"}
    fetch_api.create_thread(token_elephant, d)

    # 一個前の投稿の色付け
    d = {"component_type": "PREMISE", "related_to_id": 4}
    fetch_api.updated_sentence(3, token_elephant, d)
    # 一個前の投稿の色付け
    d = {"component_type": "CLAIM", "related_to_id": None}
    fetch_api.updated_sentence(4, token_elephant, d)


def otter1(token_otter):
    d = {"body": "As I think the regulation by the law is just meaningful,\n therefore the law should be abolished.",
         "in_reply_to_id": 2}
    fetch_api.create_post(token_otter, d)


def otter2(token_otter):
    d = {
        "body": "Unless we regulate by law,\n lawless situations will happen in your life.\n I want to take a way to reward people who are keeping the law property.",
        "in_reply_to_id": 4}
    fetch_api.create_post(token_otter, d)


def otter2_coloed(token):
    d = {"component_type": "PREMISE", "related_to_id": 12}
    fetch_api.updated_sentence(11, token, d)

    d = {"component_type": "CLAIM", "related_to_id": None}
    fetch_api.updated_sentence(12, token, d)


def otter1_coloed(token):
    d = {"component_type": "PREMISE", "related_to_id": 6}
    fetch_api.updated_sentence(5, token, d)
    d = {"component_type": "CLAIM", "related_to_id": None}
    fetch_api.updated_sentence(6, token, d)


def AIAD_comment(token):
    s = "Thank you for your comment!\n>> “As I think the regulation by the law is just meaningful, therefore the law should be abolished.”\nDo you have any premise or evidences for this claim?"
    print("aiad comment", s)

    d = {"body": s, "in_reply_to_id": 3}
    fetch_api.create_post(token, d)


def main():
    token_otter = fetch_api.get_access_token("Otter", "test")
    token_AIAD = fetch_api.get_access_token("AIAD", "test")
    elephant()
    #otter1(token_otter)
    key = input('続けるには y を入力してください。')
    otter1_coloed(token_otter)
    key = input('続けるには y を入力してください。')
    AIAD_comment(token_AIAD)
    #otter2(token_otter)
    key = input('続けるには y を入力してください。')
    otter2_coloed(token_otter)


if __name__ == "__main__":
    main()
