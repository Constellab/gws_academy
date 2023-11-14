# LICENSE
# This software is the exclusive property of Gencovery SAS.
# The use and distribution of this software is prohibited without the prior consent of Gencovery SAS.
# About us: https://gencovery.com
from gws_core import TaskRunner, JSONDict
from gws_academy.GeneRemoveVersion.gene_remove_version import GeneRemoveVersion
import json
from unittest import TestCase
SHORT_RECON3DMODEL_1 = """
{
    "metabolites": [
        {
            "id": "h[c]",
            "name": "Proton",
            "compartment": "c",
            "charge": 1.0,
            "formula": "H",
            "annotation": {
                "SMILES": [
                    "[H+]"
                ],
                "chebi": [
                    "CHEBI:24636"
                ],
                "inchi": [
                    "InChI=1S/p+1"
                ],
                "kegg.compound": [
                    "C00080"
                ],
                "pubchem.compound": [
                    "1038"
                ]
            }
        },
        {
            "id": "nadh[c]",
            "name": "Nicotinamide Adenine Dinucleotide - Reduced",
            "compartment": "c",
            "charge": -2.0,
            "formula": "C21H27N7O14P2",
            "annotation": {
                "SMILES": [
                    "[H]O[C@@]1([H])[C@@]([H])(O[C@]([H])(C([H])([H])OP([O-])(=O)OP([O-])(=O)OC([H])([H])[C@@]2([H])O[C@@]([H])(N3C([H])=C([H])C([H])([H])C(=C3[H])C(=O)N([H])[H])[C@]([H])(O[H])[C@]2([H])O[H])[C@@]1([H])O[H])N1C([H])=NC2=C(N=C([H])N=C12)N([H])[H]"
                ],
                "chebi": [
                    "CHEBI:16908"
                ],
                "hmdb": [
                    "HMDB01487"
                ],
                "inchi": [
                    "InChI=1S/C21H29N7O14P2/c22-17-12-19(25-7-24-17)28(8-26-12)21-16(32)14(30)11(41-21)6-39-44(36,37)42-43(34,35)38-5-10-13(29)15(31)20(40-10)27-3-1-2-9(4-27)18(23)33/h1,3-4,7-8,10-11,13-16,20-21,29-32H,2,5-6H2,(H2,23,33)(H,34,35)(H,36,37)(H2,22,24,25)/p-2/t10-,11-,13-,14-,15-,16-,20-,21-/m1/s1"
                ],
                "kegg.compound": [
                    "C00004"
                ],
                "pubchem.compound": [
                    "928"
                ]
            }
        },
        {
            "id": "nad[c]",
            "name": "Nicotinamide Adenine Dinucleotide",
            "compartment": "c",
            "charge": -1.0,
            "formula": "C21H26N7O14P2",
            "annotation": {
                "SMILES": [
                    "[H]O[C@@]1([H])[C@@]([H])(O[C@]([H])(C([H])([H])OP([O-])(=O)OP([O-])(=O)OC([H])([H])[C@@]2([H])O[C@@]([H])([N+]3=C([H])C(=C([H])C([H])=C3[H])C(=O)N([H])[H])[C@]([H])(O[H])[C@]2([H])O[H])[C@@]1([H])O[H])N1C([H])=NC2=C(N=C([H])N=C12)N([H])[H]"
                ],
                "chebi": [
                    "CHEBI:15846"
                ],
                "hmdb": [
                    "HMDB00902"
                ],
                "inchi": [
                    "InChI=1S/C21H27N7O14P2/c22-17-12-19(25-7-24-17)28(8-26-12)21-16(32)14(30)11(41-21)6-39-44(36,37)42-43(34,35)38-5-10-13(29)15(31)20(40-10)27-3-1-2-9(4-27)18(23)33/h1-4,7-8,10-11,13-16,20-21,29-32H,5-6H2,(H5-,22,23,24,25,33,34,35,36,37)/p-1/t10-,11-,13-,14-,15-,16-,20-,21-/m1/s1"
                ],
                "kegg.compound": [
                    "C00003"
                ],
                "pubchem.compound": [
                    "5893"
                ]
            }
        },
        {
            "id": "2hb[c]",
            "name": "2-Hydroxybutyrate",
            "compartment": "c",
            "charge": -1.0,
            "formula": "C4H7O3",
            "annotation": {
                "SMILES": [
                    "[H]OC([H])(C([O-])=O)C([H])([H])C([H])([H])[H]"
                ],
                "chebi": [
                    "CHEBI:1148"
                ],
                "hmdb": [
                    "HMDB00008"
                ],
                "inchi": [
                    "InChI=1/C4H8O3/c1-2-3(5)4(6)7/h3,5H,2H2,1H3,(H,6,7)/p-1"
                ],
                "kegg.compound": [
                    "C05984"
                ],
                "pubchem.compound": [
                    "11266"
                ]
            }
        },
        {
            "id": "2obut[c]",
            "name": "2-Oxobutanoate",
            "compartment": "c",
            "charge": -1.0,
            "formula": "C4H5O3",
            "annotation": {
                "SMILES": [
                    "[H]C([H])([H])C([H])([H])C(=O)C([O-])=O"
                ],
                "chebi": [
                    "CHEBI:30831"
                ],
                "hmdb": [
                    "HMDB00005"
                ],
                "inchi": [
                    "InChI=1S/C4H6O3/c1-2-3(5)4(6)7/h2H2,1H3,(H,6,7)/p-1"
                ],
                "kegg.compound": [
                    "C00109"
                ],
                "pubchem.compound": [
                    "58"
                ]
            }
        }
    ],
    "reactions": [
        {
            "id": "2HBO",
            "name": "2-Hydroxybutyrate:NAD+ Oxidoreductase",
            "metabolites": {
                "2hb[c]": -1.0,
                "2obut[c]": 1.0,
                "h[c]": 1.0,
                "nad[c]": -1.0,
                "nadh[c]": 1.0
            },
            "lower_bound": -1000.0,
            "upper_bound": 1000.0,
            "gene_reaction_rule": "92483.1 or 3948.2 or 55293.1 or (3945.1 and 3939.1) or 3939.1 or 160287.1 or 3945.1 or 3948.1",
            "subsystem": "Propanoate metabolism",
            "notes": {
                "Confidence Level": "0.0",
                "NOTES": "NCD"
            },
            "annotation": {
                "ec-code": [
                    "1.1.1.27"
                ],
                "pubmed": [
                    "10108",
                    "21765"
                ]
            }
        }
    ],
    "genes": [
        {
            "id": "92483.1",
            "name": ""
        },
        {
            "id": "3948.2",
            "name": ""
        },
        {
            "id": "55293.1",
            "name": ""
        },
        {
            "id": "3945.1",
            "name": ""
        },
        {
            "id": "3939.1",
            "name": ""
        },
        {
            "id": "160287.1",
            "name": ""
        },
        {
            "id": "3948.1",
            "name": ""
        }
    ],
    "id": "Recon3DModel",
    "compartments": {
        "c": "c"
    },
    "version": "1"
}
"""
SHORT_RECON3DMODEL_1_NO_GENE_VERSION = """
{
    "metabolites": [
        {
            "id": "h[c]",
            "name": "Proton",
            "compartment": "c",
            "charge": 1.0,
            "formula": "H",
            "annotation": {
                "SMILES": [
                    "[H+]"
                ],
                "chebi": [
                    "CHEBI:24636"
                ],
                "inchi": [
                    "InChI=1S/p+1"
                ],
                "kegg.compound": [
                    "C00080"
                ],
                "pubchem.compound": [
                    "1038"
                ]
            }
        },
        {
            "id": "nadh[c]",
            "name": "Nicotinamide Adenine Dinucleotide - Reduced",
            "compartment": "c",
            "charge": -2.0,
            "formula": "C21H27N7O14P2",
            "annotation": {
                "SMILES": [
                    "[H]O[C@@]1([H])[C@@]([H])(O[C@]([H])(C([H])([H])OP([O-])(=O)OP([O-])(=O)OC([H])([H])[C@@]2([H])O[C@@]([H])(N3C([H])=C([H])C([H])([H])C(=C3[H])C(=O)N([H])[H])[C@]([H])(O[H])[C@]2([H])O[H])[C@@]1([H])O[H])N1C([H])=NC2=C(N=C([H])N=C12)N([H])[H]"
                ],
                "chebi": [
                    "CHEBI:16908"
                ],
                "hmdb": [
                    "HMDB01487"
                ],
                "inchi": [
                    "InChI=1S/C21H29N7O14P2/c22-17-12-19(25-7-24-17)28(8-26-12)21-16(32)14(30)11(41-21)6-39-44(36,37)42-43(34,35)38-5-10-13(29)15(31)20(40-10)27-3-1-2-9(4-27)18(23)33/h1,3-4,7-8,10-11,13-16,20-21,29-32H,2,5-6H2,(H2,23,33)(H,34,35)(H,36,37)(H2,22,24,25)/p-2/t10-,11-,13-,14-,15-,16-,20-,21-/m1/s1"
                ],
                "kegg.compound": [
                    "C00004"
                ],
                "pubchem.compound": [
                    "928"
                ]
            }
        },
        {
            "id": "nad[c]",
            "name": "Nicotinamide Adenine Dinucleotide",
            "compartment": "c",
            "charge": -1.0,
            "formula": "C21H26N7O14P2",
            "annotation": {
                "SMILES": [
                    "[H]O[C@@]1([H])[C@@]([H])(O[C@]([H])(C([H])([H])OP([O-])(=O)OP([O-])(=O)OC([H])([H])[C@@]2([H])O[C@@]([H])([N+]3=C([H])C(=C([H])C([H])=C3[H])C(=O)N([H])[H])[C@]([H])(O[H])[C@]2([H])O[H])[C@@]1([H])O[H])N1C([H])=NC2=C(N=C([H])N=C12)N([H])[H]"
                ],
                "chebi": [
                    "CHEBI:15846"
                ],
                "hmdb": [
                    "HMDB00902"
                ],
                "inchi": [
                    "InChI=1S/C21H27N7O14P2/c22-17-12-19(25-7-24-17)28(8-26-12)21-16(32)14(30)11(41-21)6-39-44(36,37)42-43(34,35)38-5-10-13(29)15(31)20(40-10)27-3-1-2-9(4-27)18(23)33/h1-4,7-8,10-11,13-16,20-21,29-32H,5-6H2,(H5-,22,23,24,25,33,34,35,36,37)/p-1/t10-,11-,13-,14-,15-,16-,20-,21-/m1/s1"
                ],
                "kegg.compound": [
                    "C00003"
                ],
                "pubchem.compound": [
                    "5893"
                ]
            }
        },
        {
            "id": "2hb[c]",
            "name": "2-Hydroxybutyrate",
            "compartment": "c",
            "charge": -1.0,
            "formula": "C4H7O3",
            "annotation": {
                "SMILES": [
                    "[H]OC([H])(C([O-])=O)C([H])([H])C([H])([H])[H]"
                ],
                "chebi": [
                    "CHEBI:1148"
                ],
                "hmdb": [
                    "HMDB00008"
                ],
                "inchi": [
                    "InChI=1/C4H8O3/c1-2-3(5)4(6)7/h3,5H,2H2,1H3,(H,6,7)/p-1"
                ],
                "kegg.compound": [
                    "C05984"
                ],
                "pubchem.compound": [
                    "11266"
                ]
            }
        },
        {
            "id": "2obut[c]",
            "name": "2-Oxobutanoate",
            "compartment": "c",
            "charge": -1.0,
            "formula": "C4H5O3",
            "annotation": {
                "SMILES": [
                    "[H]C([H])([H])C([H])([H])C(=O)C([O-])=O"
                ],
                "chebi": [
                    "CHEBI:30831"
                ],
                "hmdb": [
                    "HMDB00005"
                ],
                "inchi": [
                    "InChI=1S/C4H6O3/c1-2-3(5)4(6)7/h2H2,1H3,(H,6,7)/p-1"
                ],
                "kegg.compound": [
                    "C00109"
                ],
                "pubchem.compound": [
                    "58"
                ]
            }
        }
    ],
    "reactions": [
        {
            "id": "2HBO",
            "name": "2-Hydroxybutyrate:NAD+ Oxidoreductase",
            "metabolites": {
                "2hb[c]": -1.0,
                "2obut[c]": 1.0,
                "h[c]": 1.0,
                "nad[c]": -1.0,
                "nadh[c]": 1.0
            },
            "lower_bound": -1000.0,
            "upper_bound": 1000.0,
            "gene_reaction_rule": "92483 or 3948 or 55293 or (3945 and 3939) or 3939 or 160287 or 3945 or 3948",
            "subsystem": "Propanoate metabolism",
            "notes": {
                "Confidence Level": "0.0",
                "NOTES": "NCD"
            },
            "annotation": {
                "ec-code": [
                    "1.1.1.27"
                ],
                "pubmed": [
                    "10108",
                    "21765"
                ]
            }
        }
    ],
    "genes": [
        {
            "id": "92483",
            "name": ""
        },
        {
            "id": "3948",
            "name": ""
        },
        {
            "id": "55293",
            "name": ""
        },
        {
            "id": "3945",
            "name": ""
        },
        {
            "id": "3939",
            "name": ""
        },
        {
            "id": "160287",
            "name": ""
        }
    ],
    "id": "Recon3DModel",
    "compartments": {
        "c": "c"
    },
    "version": "1"
}
"""

class TestGeneRemoveVersion(TestCase):
    def test_gene_remove_version(self):
        model = JSONDict(json.loads(SHORT_RECON3DMODEL_1))
        runner= TaskRunner(task_type=GeneRemoveVersion,
            params=None,
            inputs={'input_json' : model})

        outputs = runner.run()
        json_output : JSONDict = outputs['output_json']
        expected_json = JSONDict(json.loads(SHORT_RECON3DMODEL_1_NO_GENE_VERSION))
        self.assertTrue(json_output.equals( expected_json))
