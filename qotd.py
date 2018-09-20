def main(args):
    name = args.get("greeting", "human")
    qotd = name + ": Tough times don't last; tough people do."
    print(qotd)
    return {"qotd": qotd}
