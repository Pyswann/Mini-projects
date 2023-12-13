import func as fn

'''get the title'''
title = fn.title_gen("https://gearsvine.com/best-bandsaw-blades-for-resawing/")
# print(title)


'''get all the h3s'''
H3_headings = fn.get_h3s("https://gearsvine.com/best-bandsaw-blades-for-resawing/")
# print(H3_headings[22])

'''get all paragraphs'''
paragraph = fn.get_p("https://gearsvine.com/best-bandsaw-blades-for-resawing/")
print(paragraph)






