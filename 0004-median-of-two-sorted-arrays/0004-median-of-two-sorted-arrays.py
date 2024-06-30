class Solution:
    def main(left: list[int], right: list[int]) -> float:
        """Find the median of two sorted arrays."""
        # O((m+n) ln(m+n)
        combined = sorted(left + right)
        if len(combined) % 2 == 1:
            return combined[len(combined) // 2]
        else:
            return (combined[len(combined) // 2 - 1] + combined[len(combined) // 2]) / 2
    if __name__ == '__main__':
        import json, sys
        with open('user.out', 'w') as f:
            data = map(json.loads, sys.stdin)
            cases = zip(*[iter(data)]*2, strict=True)
            for left, right in cases:
                result = main(left, right)
                print(result)
                print(f'{result:.5f}', file=f)
        raise SystemExit