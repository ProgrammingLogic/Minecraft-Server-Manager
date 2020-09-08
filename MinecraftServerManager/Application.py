from processes import EventProcess, PacketProcess
from exceptions import InvalidArguments

import json
import sys


class Application():
    def __init__(self, options):
        self.store_options(options)
        self.event_queue = []
        self.processes = {}

        self.add_process('EventProcess', EventProcess(application=self))
        self.add_process('PacketProcess', PacketProcess(application=self, host=options['host'], port=options['port']))


    def start(self):
        """
        Starts the application.
        """
        for process in self.processes.values():
            process.start()


    def add_process(self, name, process):
        self.processes[name] = process


    def store_options(self, options):
        """
        Stores the options so Scripts that interact with the Application
        know what values to use.
        """
        with open('./configuration/options.json', 'w') as output:
            json.dump(options, output)


    def add_event(self, event):
        """
        Adds an event to the application's event queue.

        :param event:
        """
        self.event_queue.append(event)


    def pull_event(self):
        """
        Pulls an item from the front of the queue.

        :return item: The item at the front of the queue.
        """
        return self.event_queue.pop(0)


    def no_events(self):
        """
        Checks if the events queue is empty.

        :return boolean: Whether or not there are events in the queue.
        """
        if len(self.event_queue) < 1:
            return True
        else:
            return False


def process_arguments(arguments, letterValues):
    options = {}
    skip = False

    if len(arguments) == 0:
        with open('./configuration/options.json', 'r') as options_file:
            return json.load(options_file)

    for index, argument in enumerate(arguments):
        if skip:
            skip = False
            continue
        
        if '-' in argument[:1]:
            if argument[1] == '-':
                argument = argument[2:]
                if '-' in arguments[index + 1][:1]:
                    options[argument] = True
                else:
                    value = arguments[index + 1]
                    
                    try:
                        int(value)
                        value = int(value)
                    except:
                        pass

                    options[argument] = value
                    skip = True
            else:
                for letterValue in argument[1:]:
                    if letterValue in letterValues:
                        options[letterValues[letterValue]] = True
                    else:
                        raise InvalidArgument(letterValue)

    return options

                
def init_application():
    arguments = sys.argv[1:]
    
    with open('./configuration/letterValues.json') as json_file:
        try:
            letterValues = json.load(json_file)
        except json.JSONDecodeError as error:
            print(error)
            letterValues = None

    return process_arguments(arguments, letterValues)
    

def main():
    """
    The main part of the application.
    """
    options = init_application()
    app = Application(options)
    app.start()


if __name__ == '__main__':
    main()
