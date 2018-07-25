def main(args):
    name = args.get("greeting", "human")
    qotd = name + ": Tough times don't last; tough poeple do."
    print(qotd)
    return {"qotd": qotd}