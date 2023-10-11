# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com

import re
from collections import OrderedDict
from cobra.io import model_from_dict, model_to_dict

from gws_core import (ConfigParams, InputSpec, InputSpecs,
                      OutputSpec, OutputSpecs, Task, JSONDict,
                      TaskInputs, TaskOutputs, task_decorator)



@task_decorator(unique_name="GeneRemoveVersion", human_name="Version Gene's remover")

class GeneRemoveVersion(Task):
    input_specs = InputSpecs({'input_json': InputSpec(JSONDict, human_name="input model")})
    output_specs = OutputSpecs({'output_json' : OutputSpec(JSONDict, human_name = "output model")})

    config_specs= {}

    def run(self, params: ConfigParams, inputs: TaskInputs) -> TaskOutputs:


        # Charger le modèle
        model_json_1 = model_from_dict(inputs['input_json'])
        # Fonction pour extraire la partie entière d'une chaîne contenant des décimales
        def extract_integer_part(input_string):
            return re.sub(r"(\d+)\.\d+", r"\1", input_string)
        # Fonction pour supprimer les doublons dans les règles de réaction
        def remove_duplicates(expression, operator):
            elements = expression.split(operator)
            unique_elements = list(OrderedDict.fromkeys(elements).keys())
            return operator.join(unique_elements).strip()
        # Fonction pour traiter et mettre à jour les règles de réaction
        def process_rule(rule, operator):
            pattern = f"([^ {operator}()]+(?: {operator} [^ {operator}()]+)*)"
            matches = re.findall(pattern, rule)
            for match in matches:
                replacement = remove_duplicates(match, f" {operator} ")
                rule = rule.replace(match, replacement)
            return rule
        # Parcourir toutes les réactions et mettre à jour les règles
        for reaction in model_json_1.reactions:
            original_rule = reaction.gene_reaction_rule  # Stocker la règle d'origine
            # Remplacer les décimales par leurs parties entières
            updated_rule = re.sub(r"(\(\d+)\.\d+(\))", r"\1\2", original_rule)
            updated_rule = extract_integer_part(updated_rule)
            # Traitement pour supprimer les doublons dans les règles de réaction
            updated_rule = process_rule(updated_rule, 'and')
            updated_rule = process_rule(updated_rule, 'or')
            # Mettre à jour la règle de réaction
            reaction.gene_reaction_rule = updated_rule
        # Enregistrer le modèle mis à jour
        return {'output_json' : JSONDict(model_to_dict(model_json_1))}


