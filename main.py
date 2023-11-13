import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# print("\n\nClasses---------------------")
# for(name, member) in getmembers(ET, isclass):
#     if not name.startswith("_"):
#         print(name)

# print("\n\nFunctions---------------------")
# for(name, member) in getmembers(ET, isfunction):
#     if not name.startswith("_"):
#         print(name)
'''
Testrail XML Tree Schema:
-------------------------
<root>
    - id
    - name
    - description
    <sections>        ------------ can repeat
        <section>
            - name
            - description
            <cases>
                <case>
                    - id
                    - title
                    - template
                    - type
                    - priority
                    - references
                    <custom>
                        - preconds
                        - steps
                        - expected
                    </custom>
                </case>
            </cases>
        </section>
    </sections>
</root>


'''
tree = ET.parse('intellidash_fd.xml')
root = tree.getroot()
suite_description = root.find('description')

sections = root.findall('sections/section')
for curr_section in sections: 
    section_name = curr_section.find('name').text
    section_description = curr_section.find('description').text
    print('[0]' + section_name)

    # cases = curr_section.findall('sections/section/cases')
    # for curr_case in cases:
    #     case_title = curr_case.find('title')
        
    #     if case_title is not None:
    #         title_text = curr_case.find('title').text
    #         print('[1]' + title_text)

#print(ET.tostring(root))
'''
# Use relative paths to access <section> elements
sections = root.findall(".//section")

       # Access the text within the <custom> element
        custom = case.find(".//custom")
'''