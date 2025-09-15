def count_keys(comments, search_terms):
    counts = {kw: 0 for kw in search_terms}
    amount_comments = 0
    for comment in comments:
        amount_comments += 1
        for kw in search_terms:
            counts[kw] += comment.lower().count(kw.lower())

    print(f"Total comments: {amount_comments}\n")
    for kw, count in counts.items():
        print(f"{kw}: {count}")
    
def number_comments(comments, channel):
    number = input("\nHow many comments do you need?: ")
    while True:
        if number.isdigit():
            break
        else:
            number = input("\nEnter again: ")

    print(f"\nChannel: {channel}")
    for i, c in enumerate(comments[:int(number)], 1):
        print(f"\n\n{i}:\n{c}")