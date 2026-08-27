"""
Demonstrates set creation from lists to eliminate duplicates.
"""

def demo_set_deduplication():
    numbers_list = [1, 4, 3, 5, 1, 5, 9, 2, 5, 8]
    print('Original list with duplicates:', numbers_list)

    # Passing list to set() deduplicates items in O(N) time
    unique_set = set(numbers_list)
    print('Deduplicated set:', unique_set)

    # Convert back to list if ordered indexing is needed
    dedup_list = list(unique_set)
    print('Converted back to list:', dedup_list)

    return unique_set, dedup_list

if __name__ == '__main__':
    demo_set_deduplication()
