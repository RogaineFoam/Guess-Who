class Character:
	
	name = ''
	isFemale = False
	hasHat = False
	hasGlasses = False
	hasBeard = False
	hasMustache = False
	hasRosyCheeks = False
	isSmiling = False
	isBald = False
	hairColor = '' 
	isActive = True

	def __init__(self, name, isFemale, hasHat, hasGlasses, hasBeard, hasMustache, hasRosyCheeks, isSmiling, isBald, hairColor):
		self.name = name
		self.isFemale = isFemale
		self.hasHat = hasHat
		self.hasGlasses = hasGlasses
		self.hasBeard = hasBeard
		self.hasMustache = hasMustache
		self.hasRosyCheeks = hasRosyCheeks
		self.isSmiling = isSmiling
		self.isBald = isBald
		self.hairColor = hairColor
		self.isActive = True 

	def isActive():
		return isActive

	def toggleActive():
		isActive = not isActive

	def hasAttribute(attribute):
		if(attribute.equals('female')): 
			return hat 
		if(attribute.equals('hat')): 
			return hat 
