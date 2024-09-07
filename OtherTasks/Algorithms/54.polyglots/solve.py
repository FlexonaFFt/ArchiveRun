def find_the_solve():
    n = int(input().strip())
    all_languages, common_languages = set(), None
    for _ in range(n):
        li = int(input().strip())
        languages = set()
        for _ in range(li):
            language = input().strip()
            languages.add(language)
        all_languages.update(languages)

        if common_languages is None:
            common_languages = languages
        else:
            common_languages.intersection_update(languages)

    common_languages = sorted(common_languages) if common_languages else []
    all_languages = sorted(all_languages)
    print(len(common_languages))
    for lang in common_languages:
        print(lang)
    print(len(all_languages))
    for lang in all_languages:
        print(lang)

if __name__ == '__main__':
    find_the_solve()
