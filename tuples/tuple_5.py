"""
Demonstrates tuple concatenation using '+' operator to produce new tuples.
"""

def demo_tuple_concatenation():
    storage = ('Arsenal', 'Southampton', 'Man Utd', 'Liverpool',
               'Man City', 55.687, 5, 'Chelsea', -12, 'Tottenham')

    put_together = ('Everton', 'Aston Villa', 'Fulham')  # Fixed typos

    # Concatenate tuples (creates new tuple object)
    combined = storage + put_together
    print('Combined tuple size:', len(combined))
    print('Combined content:', combined)

    return combined

if __name__ == '__main__':
    demo_tuple_concatenation()
