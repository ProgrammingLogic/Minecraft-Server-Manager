class InvalidArguments(Exception):
    def __init__(self, invalid_argument, *args, **kargs):
        error_message = f"""{invalid_argument} is an invalid option. Please use -h or --help for help."""
        super().__init__(error_message, *args, **kargs)
