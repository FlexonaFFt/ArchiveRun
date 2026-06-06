class Solution:

    def main(self):
        p, n, k = map(int, input().split())
        topics, counter, curr = [], {}, 0

        for _ in range(p):
            topics.append(input())
        ids = list(map(int, input().split()))

        output = []
        for i in range(p):
            topic, curr_id = topics[i], ids[i]

            if counter.get(topic, 0) < k:
                counter[topic] = counter.get(topic, 0) + 1
                output.append(topic + ' #' + str(curr_id))

                curr += 1
                if curr == n: break

        print('\n'.join(output))


if __name__ == '__main__':
    Solution().main()
