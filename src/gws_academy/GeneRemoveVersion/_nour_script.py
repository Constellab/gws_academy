##########  COBRAAA ###########
# etape 1 :  version finale qui elimine les dots puis les doublons des reactions
from cobra.io import load_json_model, save_json_model
import re
from collections import OrderedDict

# Charger le modèle
model_json_1 = load_json_model('/lab/user/notebooks/template/gene_rename/model_test_occ_reac.json')
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
save_json_model(model_json_1, 'updated_model_reaction_without_dots_and_duplications_1.json')