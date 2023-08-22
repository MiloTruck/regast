from typing import Dict, List, Tuple

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result

class Output:
    def __init__(self, detectors_results: List[Tuple[Detector, Result]]):
        self.results = Output.sort_results(detectors_results)
    
    @staticmethod
    def sort_results(detectors_results: List[Tuple[Detector, Result]]) -> Dict[DetectorClassification, Dict[Detector, Dict[str, List[Result]]]]:
        organized_results = {}

        for detector, results in detectors_results:
            classification = detector.CLASSIFICATION
            
            if classification not in organized_results:
                organized_results[classification] = {}
            if detector not in organized_results[classification]:
                organized_results[classification][detector] = {}

            for result in results:
                fname = result.fname

                if fname not in organized_results[classification][detector]:
                    organized_results[classification][detector][fname] = []
                organized_results[classification][detector][fname].append(result)

        return organized_results

    @staticmethod
    def format_fname_to_results(fname_to_results: Dict[str, List[Result]]) -> str:
        formatted_fname_results = []

        for fname, results in fname_to_results.items():
            s = f'{fname}:\n'
            sorted_results = sorted(results, key=lambda r: r.start_line)
            s += '\n'.join(r.code for r in sorted_results)

            formatted_fname_results.append(s)

        return '\n'.join(formatted_fname_results)

    def to_stdout(self):
        formatted_classification_results = []
        for classification, detector_to_results in self.results.items():
            classification_s = '-'*25 + ' ' + classification.name + ' ' + '-'*25 + '\n'

            formatted_detector_results = []
            for detector, fname_to_results in detector_to_results.items():
                result_count = sum([len(r) for r in fname_to_results.values()])
                detector_s = f'{detector.NAME} ({result_count})\n'
                detector_s += Output.format_fname_to_results(fname_to_results)
                
                formatted_detector_results.append(detector_s)
            
            classification_s += '\n'.join(formatted_detector_results)
            formatted_classification_results.append(classification_s)

        print('\n'.join(formatted_classification_results))
            
    def to_markdown(self, report_fname: str):
        s = ''

        for classification, detector_to_results in self.results.items():
            s += f'# {classification.name} Findings\n'

            summary_s = '## Summary\n\n|Label|Optimization|Instances|\n|:-|:-|:-:|\n'
            detector_s = ''

            for i, (detector, fname_to_results) in enumerate(detector_to_results.items()):
                label = f'[{classification}-{str(i+1).zfill(2)}]'
                result_count = sum([len(r) for r in fname_to_results.values()])

                summary_s += f'|{i+1}|{detector.NAME}|{result_count}|\n'

                detector_s += f'## {label} {detector.NAME}\n'
                detector_s += f'{detector.DESCRIPTION}\n\n'
                detector_s += '_There ' + ('is' if result_count == 1 else 'are') + f' **{result_count}** instances of this issue:_\n'
                detector_s += '```solidity\n'
                detector_s += Output.format_fname_to_results(fname_to_results)
                detector_s += '```\n'

            s += summary_s + detector_s + '\n'

        with open(report_fname, 'w') as f:
            f.write(s)