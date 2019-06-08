import bs4


htmlstr ="""
<html>
    <table>
        <tr>
            <th항목</th>
            <td>2013</td>
            <td>2014</td>
            <td>2015</td>
        </tr>
        <tr>
            <th>매출액</th>
            <td>11</td>
            <td>22</td>
            <td>33</td>
        </tr>
    </table>
</html>
"""

bsObject = bs4.BeautifulSoup(htmlstr, "html.parser")

print(bsObject)
print(type(bsObject))

print(bsObject.find("td"))
print(bsObject.find_all("th"))
print(bsObject.find_all("td"))