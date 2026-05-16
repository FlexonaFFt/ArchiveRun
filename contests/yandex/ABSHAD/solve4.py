import sys
import json
import math
import itertools

def rel_dcg(results):
    return sum(doc['relevance'] / (i+1) for i, doc in enumerate(results))

def revenue(results):
    return sum(doc['cost'] / math.sqrt(i+1) for i, doc in enumerate(results))

def solve_query(orig, new_docs):
    n = len(orig)
    best_revenue = revenue(orig)
    best_rel = rel_dcg(orig)
    m = len(new_docs)
    if m == 0:
        return best_revenue
    positions = list(range(n+1))
    for places in itertools.combinations(positions, m):
        res = []
        orig_idx = 0
        new_idx = 0
        for i in range(n + m):
            if new_idx < m and i in places:
                res.append(new_docs[new_idx])
                new_idx += 1
            else:
                res.append(orig[orig_idx])
                orig_idx += 1
        
        res = res[:n]
        cur_rel = rel_dcg(res)
        cur_rev = revenue(res)
        if cur_rel + 1e-8 >= best_rel and cur_rev > best_revenue + 1e-8:
            best_revenue = cur_rev
    return best_revenue

def main():
    data = json.load(sys.stdin)
    serpset = data['serpset']
    new_documents = data['new_documents']
    new_by_query = {}
    for doc in new_documents:
        new_by_query.setdefault(doc['query'], []).append(doc)
    total = 0.0
    for serp in serpset:
        query = serp['query']
        orig = sorted(serp['results'], key=lambda d: d['position'])
        new_docs = new_by_query.get(query, [])
        total += solve_query(orig, new_docs)
    print(f"{total:.2f}")

if __name__ == "__main__":
    main()

