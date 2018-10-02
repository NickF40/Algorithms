import grab
from configs import *

import pdb
pdb.set_trace()

g = grab.Grab()
g.go(link)

print(g.doc.select('//div[contains(@class, "rpBJOHq2PR60pnwJlUyP0 s17qbtaw-0 bxapWf")]').html())


