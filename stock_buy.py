# input_list = [
# "p1 sell s1 1500 200",
# "p2 buy s2 900 500",
# "p3 buy s1 600 250",
# "p4 buy s1 1200 270",
# "p10 sell s2 1000 400",
# "p5 sell s3 300 800",
# "p6 sell s3 100 750",
# "p7 buy s3 500 900",
# "p20 sell s4 200 100",
# "p21 sell s4 200 150",
# "p22 buy s4 200 300"
# ]
#
#
#
# person type stock qty price
# p1 sell s1 1500 200
# p2 buy s2 900 500
# p3 buy s1 600 250
# p4 buy s1 1200 270
#
# p10 sell s2 1000 400
#
# p5 sell s3 300 800
# p6 sell s3 100 750
# p7  buy     s3  500     900
#
# p20 sell s4 200 100
# p21 sell s4 200 150
# p22 buy     s4  200     300
#
#
#
# Trades
#
# p3:s1:600:200
# p4:s1:900:200
# p2:s2:900:400
# p7:s3:300:800
# p7:s3:100:750
# p22:s4:200:100

# global track incoming variable dict
incoming_dict_buy = {}
incoming_dict_sell = {}


def handler(entry):
    global incoming_dict_buy, incoming_dict_sell
    entry_list = entry.split(" ")

    if entry_list[1] == "buy":
        if entry_list[2] in incoming_dict_buy:
            incoming_dict_buy[entry_list[2]] = incoming_dict_buy[
                                                   entry_list[2]] + [
                                                   entry_list[
                                                   0:2] + entry_list[3:]]
        else:
            incoming_dict_buy[entry_list[2]] = [
                entry_list[0:2] + entry_list[3:]]
    else:
        if entry_list[2] in incoming_dict_sell:
            incoming_dict_sell[entry_list[2]] = incoming_dict_sell[
                                                    entry_list[2]] + [
                                                    entry_list[
                                                    0:2] + entry_list[3:]]
        else:
            incoming_dict_sell[entry_list[2]] = [
                entry_list[0:2] + entry_list[3:]]
    # print(incoming_dict_sell, incoming_dict_buy)
    # # if
    #
    if entry_list[1] == "buy":
        while int(incoming_dict_buy[entry_list[2]][0][2]) > 0:
            if entry_list[2] in incoming_dict_sell:
                index = min_val_index(incoming_dict_sell[entry_list[2]])
                # print(incoming_dict_sell[entry_list[2]][index][2],
                #       incoming_dict_buy[entry_list[2]][0][2])
                calculate_print(entry_list[2], index)
            else:
                break
            if entry_list[2] not in incoming_dict_buy:
                break
    else:
        if entry_list[2] in incoming_dict_buy:
            # print(incoming_dict_sell[entry_list[2]][0][2],
            #       incoming_dict_buy[entry_list[2]][0][2])
            calculate_print(entry_list[2],0)
        else:
            return


def min_val_index(inp_arr):
    min_val = int(inp_arr[0][3])
    idx = 0
    id_dict = {int(inp_arr[0][3]):0}
    for jq in inp_arr:
        # print(jq)
        if int(jq[3]) < min_val:
            min_val = jq[3]
            id_dict[jq[3]] = idx
        idx += 1
    # print(id_dict)
    return id_dict[min_val]


def calculate_print(key, indx):
    global incoming_dict_buy, incoming_dict_sell
    if int(incoming_dict_sell[key][indx][2]) \
            >= int(incoming_dict_buy[key][0][2]):
        # print("sell is higher")
        print(incoming_dict_buy[key][0][0],
              key,
              incoming_dict_buy[key][0][2],
              incoming_dict_sell[key][indx][3])
        incoming_dict_sell[key][indx][2] = \
            int(incoming_dict_sell[key][indx][2]) - \
            int(incoming_dict_buy[key][0][2])
        incoming_dict_buy[key][0][2] = 0
    else:
        # print("buy is higher")
        print(incoming_dict_buy[key][0][0],
              key,
              incoming_dict_sell[key][indx][2],
              incoming_dict_sell[key][indx][3])
        incoming_dict_sell[key][indx][2] = 0
        incoming_dict_buy[key][0][2] = \
            int(incoming_dict_buy[key][0][2]) - \
            int(incoming_dict_sell[key][indx][2])

    if incoming_dict_sell[key][indx][2] == 0:
        del incoming_dict_sell[key][indx]
    if len(incoming_dict_sell[key]) == 0:
        del incoming_dict_sell[key]
    if incoming_dict_buy[key][0][2] == 0:
        del incoming_dict_buy[key][0]
    if len(incoming_dict_buy[key]) == 0:
        del incoming_dict_buy[key]


if __name__ == '__main__':
    input_list = [
        "p1 sell s1 1500 200",
        "p2 buy s2 900 500",
        "p3 buy s1 600 250",
        "p4 buy s1 1200 270",
        "p10 sell s2 1000 400",
        "p5 sell s3 300 800",
        "p6 sell s3 100 750",
        "p7 buy s3 500 900",
        "p20 sell s4 200 100",
        "p21 sell s4 200 150",
        "p22 buy s4 200 300"
    ]
    for i in input_list:
        handler(i)
