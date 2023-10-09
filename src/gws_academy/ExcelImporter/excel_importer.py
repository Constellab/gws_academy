# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs,
                      OutputSpec, OutputSpecs, StrParam,  Task,
                      TaskInputs, TaskOutputs, task_decorator, JSONDict,
                      File)

from pandas import read_excel, DataFrame

@task_decorator("ExcelImporter", human_name="Excel Importer")
class ExcelImporter(Task):
    """
    Convert a Excel to Json
    """

    input_specs = InputSpecs({'file': InputSpec(File, human_name='excel file')})
    output_specs = OutputSpecs({'result': OutputSpec(JSONDict, human_name='Json dict result')})

    config_specs = {
        'meta_data_sheet':
        StrParam(default_value="MetaData", human_name="meta_data sheet"),
        'Layout_data_sheet': StrParam(default_value="LayoutData", human_name="LayoutData sheet"),

        'Process_Data_sheet': StrParam(default_value="ProcessData", human_name="Process Data sheet"),
        'Channel_1_sheet': StrParam(default_value="Channel1", human_name='channel 1 sheet'),
        'Channel_2_sheet': StrParam(default_value="Channel2", human_name='channel 2 sheet'),
        'Channel_3_sheet': StrParam(default_value="Channel3", human_name='channel 3 sheet'),
        'Channel_4_sheet': StrParam(default_value="Channel4", human_name='channel 4 sheet'),
        'Volumes_sheet':  StrParam(default_value="Volumes", human_name='volumes sheet'),
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        """Run the task"""

        def unique_key(dictionnary: dict):
            key_list: list = list(dictionnary.keys())
            return dictionnary[key_list[0]], key_list[0]

        # import data from file to list
        file = inputs['file'].path

        data_name = [
            params['Channel_1_sheet'],
            params['Channel_2_sheet'],
            params['Channel_3_sheet'],
            params['Channel_4_sheet'],
            params['Volumes_sheet']]

        big: dict = read_excel(file, sheet_name=data_name)
        whole = []
        while big:
            sheet_name, sheet_value = big.popitem()
            whole.append({sheet_name: sheet_value})

        # Transform the meta_data into a dict

        meta_data = read_excel(file, sheet_name=params['meta_data_sheet'], header=None, index_col=None)
        meta_data : DataFrame = meta_data.set_index(meta_data.columns[0])
        Meta_d  : DataFrame = meta_data.to_dict()[meta_data.columns[0]]

        # Transform LayoutData into a Table
        LayoutData = read_excel(file, sheet_name=params['Layout_data_sheet'])
        LayoutData.dropna(how='all', inplace=True)
        LayoutData = LayoutData.iloc[:, 0:4]

        # Transform ProcessData into dict
        ProcessData = read_excel(file, sheet_name=params['Process_Data_sheet'])
        ProcessData.dropna(how='all', inplace=True)
        ProcessData.set_index(ProcessData.columns[0], inplace=True)
        Process_d = {ProcessData.index.name: ProcessData.to_dict('index')}

        # Build the data dict
        data = {}
        number = 0  # of wells
        for wells in range(len(LayoutData.iloc[:, 0])):  # each wells from A01 to F08
            data[LayoutData.iat[wells, 0]] = {}

            for j in range(1, 4,):  # add the key Start Volume, Max Volume, Description
                column_name = LayoutData.columns[j]
                data[LayoutData.iat[wells, 0]][column_name] = LayoutData.iat[wells, j]

        for wells in data.keys():
            for table in range(1, 5, 1):  # for each sheet of channel
                sheet = whole[table]

                for cal_row in range(2):  # for twice per sheet (raw / calibrated)
                    col = 2 + number + cal_row*48

                    df = [unique_key(sheet)[0]][0]
                    name_col = df.columns[col]

                    data[wells][name_col] = df[name_col].tolist()[3:]

            # add volumes to the data
            df = [unique_key(whole[0])[0]][0]
            for vol in range(3):
                col = 2 + number + vol*48

                name_col = df.columns[col]
                data[wells][name_col] = df[name_col].tolist()[3:]
            number += 1

        # Create a time list
        key_list = list(whole[0].keys())
        df = whole[0][key_list[0]]
        Time = df.iloc[3:, 1].tolist()

        experience = {
            params['meta_data_sheet']: Meta_d,
            params['Process_Data_sheet']: Process_d,
            df.columns[1]: Time,
            "data": data
        }

        def replace_nan_with_null(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    data[key] = replace_nan_with_null(value)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    data[i] = replace_nan_with_null(item)
            elif isna(data):  # Check if it's a NaN value
                data = "null"
            return data

        # experience = replace_nan_with_null(experience)

        # set the new table a output or the live task
        exp = JSONDict(experience)
        exp.name = inputs['file'].name+'.json'
        return {'result': exp}
