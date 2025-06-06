class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        character_position = defaultdict(set)
        for i, c in enumerate(ring):
            character_position[c].add(i)
        def minStep(fromm, to):
            if fromm == to:
                return 0
            minSteps = abs(fromm - to)
            minSteps = min(minSteps, abs(len(ring) - minSteps))
            return minSteps
        n = len(key)
        dp = [0] * len(ring)
        for p in character_position[key[0]]:
            dp[p] = minStep(0, p)
        prev_char = key[0]
        for c in key[1:]:
            if prev_char == c:
                continue
            for next_pos in character_position[c]:
                dp[next_pos] = min(dp[prev_pos] + minStep(prev_pos, next_pos) for prev_pos in character_position[prev_char])
            prev_char = c
        return min(dp[p] for p in character_position[prev_char]) + len(key)