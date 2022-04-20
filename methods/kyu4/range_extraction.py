def solution(args):
    args.sort()
    start, end, s, i = True, False, [], 0
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
            if not args[i] == args[-1] - 1 and not start:
                s[-1] += str(args[i])
                start, end = False, True
            if not end:
                s.append(str(args[i]))
                start, end = True, False

        i += 1

    return ','.join(map(str, s))