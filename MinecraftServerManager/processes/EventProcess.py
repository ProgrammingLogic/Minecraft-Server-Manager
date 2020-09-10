from multiprocessing import Process

class EventProcess(Process):
    """
    The Process that handles events and distributes events
    occuring in the application.

    :param application: The base application object.
    """
    def __init__(self, application, *args, **kargs):
        self.application = application
        super().__init__(target=self.process_events, name='PythonEventProcess')


    def process_events(self):
        """
        Processes each of the events in the queue.
        """
        while True:
            if not self.application.no_events():
                self.process_event(self.application.pull_event())


    def process_event(self, event):
        """
        Processes and distrubes and individual event.

        :param event: The event to be handled.
        """
        self.application.processes[event['type']].run_event(event)


    def run_event(self, event):
        """
        Runs the specified event for the module.

        :param event: The event to be ran.
        """
        if event['title'] == 'stop':
            print(self.application)
            self.application.stop()

