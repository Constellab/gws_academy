# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com


from gws_core import (ConfigParams, InputSpec, InputSpecs,
                      OutputSpec, OutputSpecs, Table, Task, BoolParam, StrParam,
                      TaskInputs, TaskOutputs, task_decorator, File, FileDownloader, TaskFileDownloader)


import requests
import os


@task_decorator("kegg_schema", human_name='kegg schema', short_description="Kegg pathway visualiser")
class KeggSchema(Task):
    """
    # LICENCE
    KEGG is a database resource for understanding high-level functions and
    utilities of the biological system. Kanehisa Laboratories owns and controls
    the rights to KEGG. Although the KEGG database is made freely available for
    academic use via the website, it is not in the public domain. All
    commercial use of KEGG requires a license. Please ensure that you have
    licence to use KEGG database."""

    output_specs = OutputSpecs({
        'output_file' : OutputSpec(File, human_name="output scheme")
    })

    config_specs = {
        'pathway_id' : StrParam(
            default_value=None,
            optional=True,
            human_name='pathway id',
            short_description='replace with the pathway id you want to explore (map00010 for example), None, not known',
        ),
        'pathway_name' : StrParam(
            default_value=None,
            optional=True,
            human_name="Pathway name",
            short_description=" i.e : Glycolysis, if you don't know the pathway ID, fill this with the name"
        )
    }

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:
        pathway_name = params['pathway_name']
        pathway_id = params['pathway_id']
        # This is a snippet template for a Python live task.

        def get_kegg_pathway_id_by_name(pathway_name):
            try:
                # Make the request to search for pathway entries by name
                response = requests.get(f"http://rest.kegg.jp/find/pathway/{pathway_name}")


                if response.status_code == 200:
                    # Parse the response to extract the pathway ID
                    lines = response.text.strip().split("\n")
                    if lines:
                        pathway_entry = lines[0].split("\t")
                        if len(pathway_entry) == 2:
                            pathway_id = pathway_entry[0].split(":")[1]
                            return pathway_id


                self.log_error_message(f"Pathway with name '{pathway_name}' not found.")
                return None


            except requests.exceptions.RequestException as e:
                self.log_error_message(f"Error fetching pathway data: {e}")
                return None

        def download_kegg_pathway_image(pathway_id, save_path):
            try:
                # Make the request to fetch the image data
                response = requests.get(f"http://rest.kegg.jp/get/{pathway_id}/image")


                if response.status_code == 200:
                    # Save the image to the specified path
                    with open(save_path, "wb") as f:
                        f.write(response.content)
                    self.log_success_message(f"Pathway image saved to {save_path}")
                else:
                    self.log_error_message(f"Error fetching pathway image. Status code: {response.status_code}")


            except requests.exceptions.RequestException as e:
                self.log_error_message(f"Error fetching pathway image: {e}")


        if(pathway_id is None):
            pathway_id = get_kegg_pathway_id_by_name(pathway_name)




        if pathway_id:
            self.log_info_message(f"The KEGG ID for '{pathway_name}' is: {pathway_id}")
        else:
            self.log_info_message("Pathway not found or error occurred.")


        save_path = pathway_id + "_pathway_image.png"


        download_kegg_pathway_image(pathway_id, save_path)


        return {'output_file' : File(save_path)}
