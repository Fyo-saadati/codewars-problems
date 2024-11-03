def recover_secret(triplets):
    result_str = ""
    ch_set = list(set("".join(["".join(ls) for ls in triplets])))
    while len(triplets) > 0:
        for ch in ch_set:
            flag = True
            for ls in triplets:
                if ch in ls and ls.index(ch) != 0:
                    flag = False
                    break
            if flag:
                for ls in triplets:
                    if ch in ls:
                        if ch not in result_str:
                            result_str += ch
                        ls.remove(ch)
            triplets = list(filter(None, triplets))
    return result_str
