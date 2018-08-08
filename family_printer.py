def family_printer(family, detailed=False):
    sep = "===          FAMILY          ==="
    print(sep)
    if detailed:
        for k in family:
            print("N: {} | P: {} | G: {}".format(
                k, family[k].partner_name, family[k].gift
            ))
    else:
        for k in family:
            print("{} | {} | {}".format(
                k, family[k].partner_name, family[k].gift
            ))
    print(sep)
