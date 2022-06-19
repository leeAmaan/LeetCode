class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], '', 0
        for r in searchWord:
            prefix += r
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i: i+3] if w.startswith(prefix)])
        return res