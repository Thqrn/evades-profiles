def maxlength(tab):

    newtab = []

    for col in tab:
        newcol = []
        for r in col:
            if type(r) != str and type(r) != list:
                r = str(r)
            if type(r) == list:
                r = max(r, key = len)
            newcol.append(r)
        newtab.append(newcol)

    spacers = []

    for i in range(len(newtab[0])):
        spacers.append(max([len(col[i]) for col in newtab]))

    return spacers
        

def tablizer(table, header, alignment=["left"]):
    # set alignments

    if len(alignment) == 1:
        alignment = alignment*len(header)

    if len(alignment) == 2 and len(alignment) != len(header):
        alignment.extend([alignment[1]]*(len(header)-2))

    # find longest lines of any multi-line headers
    # and make all headers strings (maybe)
    newheader = []
    longesthead = 1
    for i, head in enumerate(header):
        if type(head) != str:
            head = str(head)
        head = head.split("\n")
        if len(head) == 1:
            head = head[0]
        if type(head) == list:
            if len(head) > longesthead:
                longesthead = len(head)
        newheader.append(head)

    # spacing for everything
    spacing = maxlength(table + [newheader])

    # print header with alignment
    for h in range(longesthead):
        for i, head in enumerate(newheader):
            if type(head) == list:
                if len(head) > h:
                    if alignment[i] == "left":
                        print(f"{head[h]:<{spacing[i]}}", end="")
                    elif alignment[i] == "right":
                        print(f"{head[h]:>{spacing[i]}}", end="")
                    else:
                        print(f"{head[h]:^{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()
                else:
                    print(f"{'':<{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()
            else:
                if h == 0:
                    if alignment[i] == "left":
                        print(f"{head:<{spacing[i]}}", end="")
                    elif alignment[i] == "right":
                        print(f"{head:>{spacing[i]}}", end="")
                    else:
                        print(f"{head:^{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()
                else:
                    print(f"{'':<{spacing[i]}}", end="")
                    if i != len(newheader)-1:
                        print(" | ", end="")
                    else:
                        print()

    # print separator
    for i, space in enumerate(spacing):
        print(f"{'-'*space}", end="")
        if i != len(spacing)-1:
            print("-+-", end="")
        else:
            print()

    # print each row of data with alignment
    for row in table:
        for i, col in enumerate(row):
            if alignment[i] == "left":
                print(f"{col:<{spacing[i]}}", end="")
            elif alignment[i] == "right":
                print(f"{col:>{spacing[i]}}", end="")
            else:
                print(f"{col:^{spacing[i]}}", end="")
            if i != len(row)-1:
                print(" | ", end="")
        print()

headers = ["example\nheader", "line 2", "it fits to long\nstuff"]
data = ["yahoo", "123", "like suuuuuuper long lines"]
datamore = ["data4", 3, "5%"]
dataints = [7, 8, 1239.123]

tablizer([data, datamore, dataints], headers, ["left", "center"])