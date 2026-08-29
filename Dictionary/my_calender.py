"""
Demonstrates dictionary lookup using get() with default fallbacks.
"""

def demo_calendar():
    month_table = {
        'Jan': 'January', 'Feb': 'February', 'Mar': 'March',
        'Apr': 'April', 'May': 'May', 'Jun': 'June',
        'Jul': 'July', 'Aug': 'August', 'Sep': 'September',
        'Oct': 'October', 'Nov': 'November', 'Dec': 'December'  # Fixed typo: December
    }

    august = month_table.get('Aug')
    unknown_month = month_table.get('Inv', 'Invalid Month')

    print('August lookup:', august)
    print('Invalid lookup fallback:', unknown_month)

    return august, unknown_month

if __name__ == '__main__':
    demo_calendar()
