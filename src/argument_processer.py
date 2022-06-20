import arguments
import os
import converter_manager


def process_arguments(args: arguments.ConversionArguments):
    if args.proc_count is None:
        args.proc_count = os.cpu_count()
    supported_formats = [".docx", ".doc", ".xls", ".xlsx"]
    args.input_paths = list(filter(lambda x: x.suffix in supported_formats, args.input_paths))
    args.input_paths.sort(key=lambda x: x.stat().st_size)  # Sort them according to filesize
    converter_manager.start_conversion(args)
