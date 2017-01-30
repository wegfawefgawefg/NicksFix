'''	try to convert string to int
	return false if string cannot be converted to int
'''
def stringToInt( inString ):
	try:
		return int( inString )
	except:
		return False

'''	get an int from the user
	if string is not convertable to int, request another int from the user
'''
def requestConvertableStringInt( inRequestMessage ):
	isNotConvertable = True
	while isNotConvertable:
		userNumAsString = input( inRequestMessage )
		userNumAsInt = stringToInt( userNumAsString )
		if( type(userNumAsString) is bool ):
			break

'''	get an int from the user
	if int is not in valid range, or if int is not convertable to an int,
	ask for a new number.
'''
isNotInRange = True;
while isNotInRange:
	userNum = requestConvertableStringInt( "Pick a number between 1 and 100..." )
	if ( 0 <= userNum ) and ( usernum <= 100 ):
		break

print( userNum )