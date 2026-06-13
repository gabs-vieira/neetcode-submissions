class Solution:
    #lenght prefix source
    
    def encode(self, strs: list[str]) -> str:
        # Format: "<length>#<content>" for each string
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, encoded: str) -> list[str]:
        result = []
        i = 0

        while i < len(encoded):
            # Find the '#' delimiter from current position
            delim = encoded.index('#', i)

            # Parse the length before the delimiter
            length = int(encoded[i:delim])

            # Extract exactly 'length' chars after the delimiter
            start = delim + 1
            result.append(encoded[start:start + length])

            # Advance pointer
            i = start + length

        return result