from transposition_table_simple import TranspositionTable

tt = TranspositionTable()

board = "BWBWBWBW"
hash_list = tt.generate_hash(board)
# Check if all elements are unique.
assert len(set(hash_list)) == len(hash_list)

hash = tt.board_hash(board, hash_list)

third = hash_list[2]
print("before update", hash)
# updated hash.
hash1 = hash^third
print("after update", hash1)

hash2 = hash1^third
print("after  2xupdate", hash2)
assert hash2 == hash