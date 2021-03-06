#MenuTitle: Copy Glyph and add Ending to Name
# -*- coding: utf-8 -*-
# Code by Olli Meier, Oktober 2017, Version 1.02
__doc__="""
Copy glyph from selection and add somthing to the name.
"""

from GlyphsApp import *

try:
	from vanilla import *
except:
	Glyphs.displayDialog_(u'Vanilla for python is missing.')


font = Glyphs.font

warnings = []
added = []
def copyGlyph_addName(font, glyph,x):
	oldName = glyph.name
	newName = glyph.name + x
	
	skip = False
	if font.glyphs[newName]:
		warnings.append(newName)
		skip = True
	
	if not skip:
		newGlyph = font.glyphs[oldName].copy()
		newGlyph.name = newName
		newGlyph.unicode = '' #It makes no sense to copy the unicode. For the future it would be nice to check the GlyphData.xml if there is a unicode for the new name. 
		added.append(newName)
		font.glyphs.append(newGlyph)

def updateGlyphInfo(added):
	for name in added:
		font.glyphs[name].updateGlyphInfo()


class WindowComb(object):
	
	def __init__(self):
		a = 400
		b = a/3 - 50
		
		self.w = Window((a, b), "Copy and add ending to name")

		self.w.w_width = TextBox((10, 13, -10, 17), "Add to name: ")
		self.w.textEditor_1 = EditText((a*2/4, 10, -10, 22))
		self.w.textEditor_1.set('.case')
		
		self.w.Button = Button((10, b - 40 , -10, -10), "process", callback = self.Button)

		self.w.open()

		
	def Button(self, sender):
		
		x = self.w.textEditor_1.get() 
		
		
		#### start: main part
		
		if x: 
			for glyph in font.selection:
				copyGlyph_addName(font, glyph, x)
			if added:
				updateGlyphInfo(added)
			print "Done."
			self.w.close()

		if not x:
			Glyphs.displayDialog_(u'Ups, empty text box. Please add somthing before you hit the process buttom.')
				
		if warnings:
			start = 'The following glyph/s already exists:\n'
			warningsPrep = '\n'.join(warnings)
			Glyphs.displayDialog_(str(start + warningsPrep))
			
		#### end: main part


WindowComb()

