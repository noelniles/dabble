"""A module that processes data.

The main idea is that each module has an input queue
and an output queue. Modules can request data packets
from other modules.

Modules also have a processing function. While there is
data in a modules input queue the module will pop items
and feed them to the processing function.

After processing the data packet a module will add it to
it's output queue. When a downstream module requests a
data packet this module will return the data packet from
the top of the output stack.
"""
import Queue

from PyQt5 import QtWidgets


class Module(QtWidgets.QWidget):
    def __init__(self, name=None, number_inputs=0, function=None, parent=None):
        self.name     = name
        self.parent   = parent
        self.data     = DataPacket()
        self.inputs   = [None]*number_inputs
        self.function = function

        self.inputQueue = Queue.Queue()
        self.inputQueueLength = len(inputQueue)

        self.outputQueue = Queue.Queue()
        self.outputQueueLength = len(outputQueue)

    def enqueueInputData(self, data):
        """Put some data in the input queue."""
        return self.inputQueue.put(data)

    def enqueuOutputData(self, data):
        """Put some data in the output queue."""
        return self.outputQueue.put(data)

    def dequeueInputData(self, data):
        """Dequeue a data packet from the input queue."""
        return self.inputQueue.get()

    def dequeueOutputData(self, data):
        """Dequeue a data packet from the output queue."""
        return self.inputQueue.get()

    def getData(data):
        """Request data from another module."""
        pass

    def sendData(self):
        """Send a data packet to another module.

        This should just pop a data packet from the output queue.
        """
        return self.outPutQueue.get()
        pass

    def process(self):
        """Return a data object that can be passed to another module."""
        pass

    def reset(self):
        pass

