import calculate, order_of_ops
c = calculate
o = order_of_ops

def main():
    ops = ["*", "/", "//", "%", "**"]
    quitter = ""
    while quitter != "q":
        i = input("Please enter an equation ending in \'=\' (Ex. 90 / 3 + 21 =) or \'q\' to quit: : ")
        if i == 'q':
            quitter = i
        else:
            i_list = i.split(" ")
            for i1 in i_list:
                if i1 in ops:
                    i_list = o.look_through(i_list)
            answer = c.calculator(i_list)
            print(i + " " + str(answer))


if __name__ == '__main__':
    main()
