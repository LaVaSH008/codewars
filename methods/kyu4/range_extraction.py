def solution(args):
    args.sort()
    s = []
    start, end = True, False
    i = 0
    while i < len(args):
        try:
            if args[i] == args[i + 1] - 1 == args[i + 2] - 2 and start:
                s.append(str(args[i]) + '-')
                start, end = False, True
            elif args[i] == args[i + 1] - 1 and not start:
                pass
            elif end:
                s[-1] += str(args[i])
                start, end = True, False
            else:
                s.append(str(args[i]))
                start, end = True, False
        except IndexError:
            continue
        i += 1
