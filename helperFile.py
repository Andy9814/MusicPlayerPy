import eyed3
import os.path
import os

class Song():
	def __init__(self, filepath):
		self.filepath = self.Validate(filepath)
		self.metadata = self.Analyze(self.filepath)
		self.title = u"".join(self.metadata["title"])
		self.artist = u"".join(self.metadata["singer"])
		self.album = u"".join(self.metadata["album"])
		self.length = u"".join(self.metadata["length"])
	def Validate(self, filepath):
		if os.path.exists(filepath):
			return filepath
		else:
			return ""

	def Analyze(self, filepath):
		metadict = {}
		try:
			audio_data = eyed3.load(filepath)
		except IOError:
			print "Not a valid file!"

		if audio_data == None:
			# if eyed3 fails to load the file
			# return a dict with empty values
			metadict["title"] = "(none)"
			metadict["singer"] = "(none)"
			metadict["album"] = "(none)"
			metadict["length"] = "(none)"
			return metadict
		else:
			metadict["title"] = audio_data.tag.title
			metadict["singer"] = audio_data.tag.artist
			metadict["album"] = audio_data.tag.album

			length_min = audio_data.info.time_secs / 60
			length_secs = audio_data.info.time_secs % 60
			if length_secs < 10:
				# I want a LEADING ZERO on this thing, STAT!
				metadict["length"] = "%d:%02d" % (length_min, length_secs)
			else:
				metadict["length"] = "%d:%d" % (length_min, length_secs)

			return metadict
