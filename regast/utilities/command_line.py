import argparse
import os
from pathlib import Path
from typing import List, Optional

from regast.detectors.detector import DetectorClassification
from regast.utilities.definitions import DETECTORS_PATH


def parse_argument_contract(contract_path: str) -> List[str]:
    if not os.path.exists(contract_path):
        print(f'[!] File or directory {contract_path} does not exist.')
        exit()
    
    if os.path.isdir(contract_path):
        files = [p for p in Path(contract_path).rglob('*.sol')]
        if not files:
            print(f'[!] Directory {contract_path} is empty.')
            exit()

        return files
    
    if not contract_path.endswith('.sol'):
        print(f'[!] {contract_path} is not a Solidity file.')
        exit()

    return [contract_path]

def parse_argument_detectors(detector_path: str) -> List[str]:
    if not os.path.exists(detector_path):
        print(f'[!] detectors: File or directory {detector_path} does not exist.')
        exit()
    
    if os.path.isdir(detector_path):
        files = [p for p in Path(detector_path).rglob('*.py')]
        if not files:
            print(f'[!] detectors: Directory {detector_path} is empty.')
            exit()

        return files
    
    if not detector_path.endswith('.py'):
        print(f'[!] detector: {detector_path} is not a Solidity file.')
        exit()

    return [detector_path]

def parse_argument_classifications(comma_separated_classifications: Optional[str]) -> Optional[List[DetectorClassification]]:
    if not comma_separated_classifications:
        return [dc for dc in DetectorClassification]

    name_to_classification = {dc.name: dc for dc in DetectorClassification}
    classification_names = ', '.join(dc.name for dc in DetectorClassification)

    classifications = []

    for classification_str in comma_separated_classifications.split(','):
        if (cs := classification_str.strip()) in name_to_classification:
            classifications.append(name_to_classification[cs])
        else:
            print(f'[!] classification: "{cs}" does not match any classification - {classification_names}.')
            exit()

    return classifications

def parse_argument_scope(contract_fnames: List[str], scope_fname: Optional[str]) -> Optional[List[str]]:
    if not scope_fname:
        return

    if not os.path.isfile(scope_fname):
        print(f'[!] scope: {scope_fname} does not exist.')
        exit()

    with open(scope_fname, 'r') as f:
        scope_lines = f.readlines()

        if not scope_lines:
            print(f'[!] scope: {scope_fname} is empty.')
            exit()

        # Match all fnames in scope with actual files
        files_in_scope = []
        for fname in scope_lines:
            filepaths = [x for x in contract_fnames if os.path.abspath(x).endswith(fname)]

            if not filepaths:
                print(f'[!] scope: {fname} does not match any file.')
                exit()

            if len(filepaths) > 1:
                tmp = ', '.join(filepaths)
                print(f'[!] scope: {fname} matches more than one file: {tmp}')
                exit()

            files_in_scope.append(filepaths)
        
        return files_in_scope

def parse_argument_report(fname: Optional[str]) -> Optional[str]:
    if not fname:
        return

    report_fname = f'{fname}.md'
    if os.path.exists(report_fname):
        print(f'[!] report: {report_fname} already exists.')
        exit()

    return report_fname


# def parse_argument_remap(remappings_fname: str) -> Dict[str, str]:
#     if not os.path.isfile(remappings_fname):
#         print(f'[!] --remap: {remappings_fname} does not exist.')

#     with open(remappings_fname, 'r') as f:
#         remap_lines = f.readlines()

#         if not remap_lines:
#             print(f'[!] --remap: {remappings_fname} is empty')

#         remappings = {}
#         for line in remap_lines:
#             identifier, path = line.split('=')
#             remappings[identifier] = path

#         return remappings

def handle_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Scan for vulnerabilities based on regex or AST queries.')
    parser.add_argument(
        'contract', 
        metavar='<contract>', 
        type=str,
        help='.sol file or folder containing .sol files to scan'
    )
    parser.add_argument(
        '-d', '--detectors', 
        metavar='<detector>', 
        type=str,
        default=DETECTORS_PATH,
        help='.py file or folder containing .py files which implement detectors'
    )
    classification_names = ', '.join(dc.name for dc in DetectorClassification)
    parser.add_argument(
        '-c', '--classifications', 
        metavar='<classifications>', 
        type=str,
        help=f'Comma-separated list of classifications: {classification_names}'
    )
    parser.add_argument(
        '-s', '--scope', 
        metavar='<scope>', 
        type=str,
        help='Text file containing a list of contracts in scope'
    )
    parser.add_argument(
        '-r', '--report', 
        metavar='<filename>',
        type=str,
        help='Generate a markdown report in <filename>.md'
    )
    # parser.add_argument(
    #     '-r', '--remap', 
    #     metavar='<remappings.txt>', 
    #     type=str,
    #     help='Text file containing import remappings'
    # )

    args = parser.parse_args()
    args.contract = parse_argument_contract(args.contract)
    args.detectors = parse_argument_detectors(args.detectors)

    args.classifications = parse_argument_classifications(args.classifications)
    args.scope = parse_argument_scope(args.contract, args.scope)
    args.report = parse_argument_report(args.report)

    # if args.remap is not None:
    #     args.remap = parse_argument_remap(args.remap)

    return args