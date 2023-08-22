#!/usr/bin/env python3

import importlib.util as import_util
import inspect
from typing import Dict, List

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.regast import Regast
from regast.utilities.command_line import handle_arguments
from regast.utilities.output import Output
from regast.utilities.setup_dependencies import initialize_dependencies


def get_detectors(detector_paths: List[str]) -> List[Detector]:
    detectors = []

    for detector_path in detector_paths:
        # Dynamically load module from Python file path
        spec = import_util.spec_from_file_location('all_detectors', detector_path)
        module = import_util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Get detectors from loaded module
        for detector_class in inspect.getmembers(module, inspect.isclass):
            if issubclass(detector_class[1], Detector) and detector_class[1] != Detector:
                detectors.append(detector_class[1])

    return detectors

def get_results_from_ast(args) -> Dict[DetectorClassification, Dict[Detector, List[Result]]]:
    # Initialize regast class, which parses ast
    regast = Regast(args.contract, args.scope)

    # Run detectors and filter results
    for detector in get_detectors(args.detectors):
        if detector.CLASSIFICATION in args.classifications:
            regast.register_detector(detector)

    results = regast.run_detectors()
    return results

def main():
    # Handle dependencies
    initialize_dependencies()

    # Parse arguments from command line
    args = handle_arguments()

    # Run detectors
    results = get_results_from_ast(args)

    # Output results to stdout, and generate markdown report if specified
    output = Output(results)
    output.to_stdout()
    if args.report:
        output.to_markdown(args.report)

if __name__ == '__main__':
    main()


"""
cacheVariable.ts
calldataViewFunctions.ts
smallUintIncrement.ts
storageVsMemoryStructArray.ts
uselessInternal.ts
"""