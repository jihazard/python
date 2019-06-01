from xml.etree.ElementTree import Element, dump, SubElement

note2 = Element("note2")
to = Element("to2")
to.text = "hello"

dummy = Element("dummy")
dummy.text = "연습이야" 

note2.append(to)
note2.insert(1,dummy)

SubElement(note2, "address").text = "서울"
dump(note2)



# from xml.etree.ElementTree import parse

# tree = parse("note.xml")
# note = tree.getroot()

# print(note.get("date"))
# print(note.get("foo", "default"))
# print(note.keys())
# print(note.item())

# from_tag = note.fine("from")
# from_tags = note.findall("from")
# from_text = note.findtext("from")

# print(from_tag)
# print(from_tags)
# print(from_text)