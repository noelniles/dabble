"""Reader will read a stream of images.

The idea here is that you give the reader a location
where some heterogenous data is stored. Maybe you tell
the reader the extension or maybe it just reads anything
I don't know yet.

There will be a large list of data files and we don't want
to hold the actual data in memory so the first plan is to
just use a generator and yield the next data item.

This class will put each item into a data packet.
"""
class Reader:
    def __init__(self):
        self.data = None
        self.type = None
        self.size = None


#class Reader:
#    def __init__(self):
#        print('Made a reader')
#
#    def filenames(directory):
#        """This is a generator that will produce the next
#        item in the file list.
#        """
#        for entry in os.scandir(directory):
#            if entry.name.endswith(extension):
#                yield os.path.join(directory, entry.name)
#
