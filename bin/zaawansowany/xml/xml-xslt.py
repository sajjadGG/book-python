#!/usr/bin/env python3

import io
from lxml import etree


XSLT = '''
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
	<foo><xsl:value-of select="/a/b/text()" /></foo>
    </xsl:template>
</xsl:stylesheet>
'''

xslt_root = etree.XML(XSLT)
transform = etree.XSLT(xslt_root)

f = io.StringIO('<a><b>Text</b></a>')
doc = etree.parse(f)
result_tree = transform(doc)

print(result_tree)

