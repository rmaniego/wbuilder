"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from arkivist import Arkivist
from wbuilder import FromJSONBuild


## tests
html = FromJSONBuild(Arkivist("examples\lib.json").show()).build()
print(html)