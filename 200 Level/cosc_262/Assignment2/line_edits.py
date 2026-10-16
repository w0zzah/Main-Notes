"""A program to display the output of the line_edits function in an
   html table.
   Originally written for COSC262 DP Assignment by Richard Lobb
   Last editted: May 2026
"""
import os
import re
from html import escape
import webbrowser
import sys

DEFAULT_CSS = """
table {font-size: 100%; border-collapse: collapse}
td, th  {border: 1px solid LightGrey; padding: 2px; }
td del {background-color: #FFBB00; text-decoration: none;}
"""

class HtmlTable:
    """A table to be rendered in HTML."""
    def __init__(self, column_headers):
        """The column headers is a list of strings. Its length determines the
           number of columns in the table"""
        self.headers = column_headers
        self.num_cols = len(column_headers)
        self._html = ""
        self._html += "<tr>" + ''.join(f"<th>{hdr}</th>" for hdr in column_headers) + "</tr>\n"

    def add_row(self, values, column_styles=None):
        """Given a list of strings ('values'), the length of which must match
           the length of the list of column headers when the table was created,
           add one row to the table. column_styles is an optional list of
           strings for setting the style attributes of the row's <td>
           elements. If given, its length must match the number of columns.

           For example
              add_row(["this", "that"], ["background-color:yellow", ""])

           would add a table row containing the values 'this' and 'that' with the
           first column having a background-color of yellow. An empty style
           string is ignored.
           String values are html-escaped (i.e. characters like '&' and '<' get
           converted to HTML-entities). Then, as a special feature for this
           assignment, any sequence of characters wrapped in double square
           brackets is instead wrapped in HTML <del> elements; these are by
           default rendered with a purple background by the HTML renderer.
           Then any newline characters are converted to <br>.
           Finally the resulting string is wrapped in a <pre> element.
        """
        def td_element(value, style, i_column):
            value = escape(value)  # HTML escaping
            value = re.sub(r'\[\[(..*?)\]\]', r'<del>\1</del>', value,
                flags=re.DOTALL + re.MULTILINE)
            value = value.replace('\n', '<br>')
            style_string = f' style="{style}"' if style else ''
            td = f"<td{style_string}><pre>{value}</pre></td>"
            return td

        if column_styles is None:
            column_styles = ["" for i in range(self.num_cols)]
        tds = [td_element(values[i], column_styles[i], i) for i in range(self.num_cols)]
        row = f"<tr>{''.join(tds)}</tr>\n"
        self._html += row

    def html(self):
        return "<table>\n" + self._html + "</table>\n"


class HtmlRenderer:
    """A class to help with displaying HTML for COSC262 DP Assignment"""
    def __init__(self, css=DEFAULT_CSS):
        """Initialise self to contain the given html string"""
        self.html = ''
        self.css = css

    def add_html(self, html):
        """Concatenate the given html to the end of the current html string"""
        self.html += html

    def render(self):
        """Display the current html in a browser window"""
        html = f"""<html><head><style>{self.css}</style></head><body>{self.html}</body></html>"""
        path = os.path.abspath('temp.html')
        with open(path, 'w') as f:
            f.write(html)
        webbrowser.open('file://' + path)


def edit_table(operations):
    """Construct an HtmlTable to display the given sequence of operations, as
       returned by the line_edits function.
    """
    table = HtmlTable(["Previous", "Current"])
    grey = "background-color:LightGrey"
    for op, left, right in operations:
        if op == 'C':
            table.add_row([left, right])
        elif op == 'D':
            table.add_row([left, right], ["background-color:#BBBBFF", grey])
        elif op == 'S':
            bg = "background-color:#FFFF99"
            table.add_row([left, right], [bg, bg])
        else:
            table.add_row([left, right], [grey, "background-color:#ABEBC6"])
    return table

def lcs(s1, s2):

    n = len(s1) + 1
    m = len(s2) + 1

    table = [[0] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    lcs_characters = []
    i = n - 1
    j = m -1
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_characters.append(s1[i-1])
            i -= 1
            j -= 1
        elif table[i-1][j] >= table[i][j-1]:
            i-= 1
        else:
            j -= 1
    return "".join(lcs_characters[::-1])

def wrap_helper(string, lcs_str):
    p = 0
    result = ""
    for character in string:
        if p < len(lcs_str) and lcs_str[p] == character:
            result += character
            p += 1
        else:
            result += f"[[{character}]]"
    return result

def line_edits(s1, s2): 
    line1 = s1.splitlines()
    line2 = s2.splitlines()
    t = [[0] * (len(line2) + 1) for _ in range(len(line1) + 1)]

    for i in range(len(line1) + 1):
        t[i][0] = i
    for j in range(len(line2) + 1):
        t[0][j] = j
    
    for i in range(1, len(line1) + 1):
        for j in range(1, len(line2) + 1):
            cost = 0 if line1[i-1] == line2[j-1] else 1
            t[i][j] = min(t[i-1][j-1] + cost,
            t[i-1][j] + 1, t[i][j-1] + 1)
    
    results = []
    i = len(line1)
    j = len(line2)

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost = 0 if line1[i-1] == line2[j-1] else 1
            if t[i][j] == t[i-1][j-1]+cost and t[i][j]<t[i-1][j]+1 and t[i][j]<t[i][j-1]+1:
                temp1 = line1[i-1]
                temp2 = line2[j-1]
                if cost == 1:
                    common = lcs(temp1, temp2)
                    results.append(("S", wrap_helper(temp1, common), wrap_helper(temp2, common)))
                else: 
                    results.append(("C", temp1, temp2))
                i -= 1
                j -= 1
                continue
        if i > 0 and t[i][j] == t[i-1][j] + 1:
            results.append(("D", line1[i-1], ""))
            i -= 1
        else:
            results.append(("I", "", line2[j-1]))
            j -= 1
    return results[::-1]

def main(s1, s2):
    renderer = HtmlRenderer()
    renderer.add_html("<h1>Show Differences (COSC262)</h1>")
    operations = line_edits(s1, s2)
    table = edit_table(operations)
    renderer.add_html(table.html())
    renderer.render()

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"

main(s1, s2)