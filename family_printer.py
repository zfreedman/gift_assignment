def family_printer(family):
    for k in family:
        print("{} | {} | {}".format(
            k, family[k].partner_name, family[k].gift
        ))
