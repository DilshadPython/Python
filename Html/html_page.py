TABLE = '''
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <table>
            <tr>
                <th>Char</th>
                <th>ASCII</th>
            </tr>
%s
        </table>
    </body>
</html>
'''
ROW = ' ' * 16 + "<tr><td>%s</td><td>%d</td></tr>"
 
rows_list = [ROW % (chr(q), q) for q in range(33, 48)]
strTable = TABLE % '\n'.join(rows_list)
 
with open(r"d:\asciiCharHTMLTable.html", 'w') as f:
    f.write(strTable)

print(strTable)
