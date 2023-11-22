import os
import json
import pandas as pd

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        data_list = []

        for file in os.listdir(self.data_path):
            if file.endswith('.json'):
                data = self._extract_data(os.path.join(self.data_path, file))
                data_list.append(data)

        return pd.DataFrame(data_list)

    def _extract_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        protocol = data.get('protocolSection', {})
        identification = protocol.get('identificationModule', {})
        description = protocol.get('descriptionModule', {})
        conditions = protocol.get('conditionsModule', {})
        design = protocol.get('designModule', {})
        eligibility = protocol.get('eligibilityModule', {})

        primary_purpose = design.get('designInfo', {}).get('primaryPurpose', '')

        extracted_data = {
            "NCT ID": self._try_except(identification, 'nctId'),
            "Official Title": self._try_except(identification, 'officialTitle'),
            "Description": self._try_except(description, 'detailedDescription'),
            "Conditions": self._try_except(conditions, 'conditions', join=True),
            "Keywords": self._try_except(conditions, 'keywords', join=True),
            "Study Type": self._try_except(design, 'studyType'),
            "Phases": self._try_except(design, 'phases', join=True),
            "Primary Purpose": primary_purpose,
            "Eligibility Criteria": self._try_except(eligibility, 'eligibilityCriteria'),
            "Is Healthy Volunteers": self._try_except(eligibility, 'healthyVolunteers'),
            "Sex": self._try_except(eligibility, 'sex'),
            "Minimum Age": self._try_except(eligibility, 'minimumAge'),
            "Standard Ages": self._try_except(eligibility, 'stdAges', join=True)
        }

        return extracted_data

    def _try_except(self, data_dict, field_name, join=False):
        try:
            value = data_dict.get(field_name, '')
            if join and isinstance(value, list):
                return ", ".join(value)
            return value
        except Exception as e:
            print(f"Error extracting {field_name}: {str(e)}")
            return ''

