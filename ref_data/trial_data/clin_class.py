from ref_data.trial_data.utils import request_ct
from utils import csv_handler, json_handler


class ClinTrials:
    _base_url = "http://clinicaltrials.gov/api/"
    _query = "query/"
    _json = "fmt=json"
    _csv = "fmt=csv"
    _info = "info/"


    def __init__(self):
        self.get_info = self.__get__info()
    
    @property
    def study_fields(self):
        fields_list = json_handler(
            f"{self._base_url}{self._info}study_fields_list?{self._json}"
        )
        return fields_list["StudyFields"]["Fields"]

    def __get__info(self):

        data_vrs = json_handler(f"{self.base_url}{self.info}/data_vrs?{self.json_}")['DataVrs']

        api_vrs = json_handler(f"{self.base_url}{self.info}/data_vrs?{self.json_}")['ApiVrs']

        return data_vrs, api_vrs
    
    def get_study_fields(self, search_expr, fields, max_studies=50, fmt="csv"):
        """Returns study content for specified fields
        Retrieves information from the study fields endpoint, which acquires specified information
        from a large (max 1000) studies. To see a list of all possible fields, check the class'
        study_fields attribute.
        Args:
            search_expr (str): A string containing a search expression as specified by
                `their documentation <https://clinicaltrials.gov/api/gui/ref/syntax#searchExpr>`_.
            fields (list(str)): A list containing the desired information fields.
            max_studies (int): An integer indicating the maximum number of studies to return.
                Defaults to 50.
            fmt (str): A string indicating the output format, csv or json. Defaults to csv.
        Returns:
            Either a dict, if fmt='json', or a list of records (e.g. a list of lists), if fmt='csv.
            Both containing the maximum number of study fields queried using the specified search expression.
        Raises:
            ValueError: The number of studies can only be between 1 and 1000
            ValueError: One of the fields is not valid! Check the study_fields attribute
                for a list of valid ones.
            ValueError: Format argument has to be either 'csv' or 'json'
        """
        if max_studies > 1000 or max_studies < 1:
            raise ValueError("The number of studies can only be between 1 and 1000")
        elif not set(fields).issubset(self.study_fields):
            raise ValueError(
                "One of the fields is not valid! Check the study_fields attribute for a list of valid ones."
            )
        else:
            concat_fields = ",".join(fields)
            req = f"study_fields?expr={search_expr}&max_rnk={max_studies}&fields={concat_fields}"
            if fmt == "csv":
                url = f"{self._BASE_URL}{self._QUERY}{req}&{self._CSV}"
                return csv_handler(url)

            elif fmt == "json":
                url = f"{self._BASE_URL}{self._QUERY}{req}&{self._JSON}"
                return json_handler(url)

            else:
                raise ValueError("Format argument has to be either 'csv' or 'json'")
        
