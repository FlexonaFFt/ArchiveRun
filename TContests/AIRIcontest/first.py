def can_place(prefix_len: int, heights: list[int], cabinet_height: int) -> bool:
    sorted_prefix = sorted(heights[:prefix_len], reverse=True)
    required_height = sum(sorted_prefix[::2])
    return required_height <= cabinet_height


def main() -> None:
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    left, right = 0, n
    while left < right:
        mid = (left + right + 1) // 2
        if can_place(mid, a, h):
            left = mid
        else:
            right = mid - 1

    print(left)


if __name__ == "__main__":
    main()
