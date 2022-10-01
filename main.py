import calculate
c = calculate


def main():
    quitter = ""
    while quitter != "q":
        i = input("Please enter an equation ending in \'=\' (Ex. 90 / 3 + 21 =) or \'q\' to quit: : ")
        if i == 'q':
            quitter = i
        else:
            i_list = i.split(" ")
            c.calculator(i_list)


if __name__ == '__main__':
    main()
