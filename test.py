def get_num_after(str, target):
    str = str.replace(' ', '')
    str = str.replace('\n', ' ')

    par = str.partition(target)
    num_str = ""
    for c in par[2]:
        if c in ("0","1","2","3","4","5","6","7","8","9","."):
            num_str += c
        else:
            if c == "." or c == " " or c == "*":
                continue
            break
    # print("¥", num_str)
    try:
        print(num_str)
    except:
        print("error")


def get_num_between(str, tar_begin, tar_end):
    str = str.replace(' ', '')
    str = str.replace('\n', ' ')

    par = str.partition(tar_begin)
    par = par[2].partition(tar_end)
    num_str = ""
    for c in par[0]:
        if c in ("0","1","2","3","4","5","6","7","8","9",".","月","日",":"):
            num_str += c
        else:
            if c == "." or c == " " or c == "*" or c == "月" or c == "日" or c ==":":
                continue
            break
    # print("¥", num_str)
    # try:
    #     print("¥", num_str)
    # except:
    #     print("error")
    return num_str

def get_word_between(str, tar_begin, tar_end):
    str = str.replace(' ', '')
    str = str.replace('\n', ' ')

    par = str.partition(tar_begin)
    result = par[2].partition(tar_end)[0]
    # print(par[2].partition(tar_end)[0])
    return result

# str_test = "收 款 到 账 通 知05 月 22 日 16:58收 款 金 额*1.00汇 总 今 日 第 7 笔 收 款 , 共 计 Y8.00 说 明 已 存 入 店 长 roy(** 间 ) 的 零 钱"
# get_num_between(str_test, "收款金额", "汇总")
# get_word_between(str_test, "已存入", "的零钱")
# print(get_num_between(str_test, "收款金额", "汇总"))
# print(get_word_between(str_test, "已存入", "的零钱"))
# num = get_num_between(str_test, "收款金额", "汇总")
# word = get_word_between(str_test, "已存入", "的零钱")
# time = get_num_between(str_test, "到账通知", "收款金额")
# No = get_num_between(str_test, "今日第", "笔收款")




