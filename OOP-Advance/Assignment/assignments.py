
class ConfigDict(dict):

	def __init__(self, filename):
		# set the name of the file in the instance
		# use a 'private' attribute for this

		#  check to see if the file exists
		# if file exists: or if true
		    # open the file and read it, line by line
		    # for line in filename:
		        # strip the line
		        # split the line on a '=', return key, value
		        '''
		        # example for line above
		        # key, val = configval.spilt('=', 1)
				
		        # this=that=other
		        '''
		        # set the key and value in the instance
		        # DO NOT USE THIS >> self[key] = value

		        # dict.__setitem__(self, key, value)

	def __setitem__(self, key, value):
		# (called when use says thisdict[key] = value)

		# set key, value in instance
		# (remember, don't use self[key] = value)
		# instance, call the dict() constructor -- as ws done in __init__

		# open the file (use the name you stored in instance)
		# loop through the instance's key / value pairs
		    # write each key/value on a line, joined by an equals sign
		    # fh.write('{0}={1}'.format(key, value))
