def get_pairs(name_office, office_phone):
    name_phone = {}
    for name in name_office:
        office = name_office[name]
        if office in office_phone:
            name_phone[name] = office_phone[office]
    print(name_phone)


def count_votes(fname: str) -> dict:
    try:
        with open(fname, "r", encoding="utf-8") as fp:
            text = fp.read()
        text = text.split()
        vote_ballot = {}
        for vote in text:
            if vote in vote_ballot:
                vote_ballot[vote] += 1
            else:
                vote_ballot[vote] = 1
        return vote_ballot
    except FileNotFoundError:
        return {}

print(count_votes('votes2.txt'))