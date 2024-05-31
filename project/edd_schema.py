# Auto generated from edd_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-31T16:01:00
# Schema: edd
#
# id: https://w3id.org/edd
# description: NON-OFFICIAL rendering of EDD schema as LinkML (for demo purposes)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EDD = CurieNamespace('edd', 'https://w3id.org/edd')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EDD


# Types
class HttpsIdentifier(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "https identifier"
    type_model_uri = EDD.HttpsIdentifier


# Class references



@dataclass
class GeneIdentifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["GeneIdentifier"]
    class_class_curie: ClassVar[str] = "edd:GeneIdentifier"
    class_name: ClassVar[str] = "gene_identifier"
    class_model_uri: ClassVar[URIRef] = EDD.GeneIdentifier

    measurementtype_ptr_id: Optional[int] = None
    gene_length: Optional[str] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurementtype_ptr_id is not None and not isinstance(self.measurementtype_ptr_id, int):
            self.measurementtype_ptr_id = int(self.measurementtype_ptr_id)

        if self.gene_length is not None and not isinstance(self.gene_length, str):
            self.gene_length = str(self.gene_length)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class MeasurementType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["MeasurementType"]
    class_class_curie: ClassVar[str] = "edd:MeasurementType"
    class_name: ClassVar[str] = "MeasurementType"
    class_model_uri: ClassVar[URIRef] = EDD.MeasurementType

    id: Optional[int] = None
    type_name: Optional[str] = None
    short_name: Optional[str] = None
    type_group: Optional[Union[str, "TypeGroupEnum"]] = None
    uuid: Optional[str] = None
    type_source_id: Optional[str] = None
    alt_names: Optional[Union[str, List[str]]] = empty_list()
    provisional: Optional[Union[str, "ProvisionalEnum"]] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, int):
            self.id = int(self.id)

        if self.type_name is not None and not isinstance(self.type_name, str):
            self.type_name = str(self.type_name)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.type_group is not None and not isinstance(self.type_group, TypeGroupEnum):
            self.type_group = TypeGroupEnum(self.type_group)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.type_source_id is not None and not isinstance(self.type_source_id, str):
            self.type_source_id = str(self.type_source_id)

        if not isinstance(self.alt_names, list):
            self.alt_names = [self.alt_names] if self.alt_names is not None else []
        self.alt_names = [v if isinstance(v, str) else str(v) for v in self.alt_names]

        if self.provisional is not None and not isinstance(self.provisional, ProvisionalEnum):
            self.provisional = ProvisionalEnum(self.provisional)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class MeasurementUnit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["MeasurementUnit"]
    class_class_curie: ClassVar[str] = "edd:MeasurementUnit"
    class_name: ClassVar[str] = "MeasurementUnit"
    class_model_uri: ClassVar[URIRef] = EDD.MeasurementUnit

    id: Optional[int] = None
    unit_name: Optional[Union[str, "UnitNameEnum"]] = None
    display: Optional[Union[str, "DisplayEnum"]] = None
    alternate_names: Optional[Union[str, "AlternateNamesEnum"]] = None
    type_group: Optional[Union[str, "TypeGroupEnum"]] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, int):
            self.id = int(self.id)

        if self.unit_name is not None and not isinstance(self.unit_name, UnitNameEnum):
            self.unit_name = UnitNameEnum(self.unit_name)

        if self.display is not None and not isinstance(self.display, DisplayEnum):
            self.display = DisplayEnum(self.display)

        if self.alternate_names is not None and not isinstance(self.alternate_names, AlternateNamesEnum):
            self.alternate_names = AlternateNamesEnum(self.alternate_names)

        if self.type_group is not None and not isinstance(self.type_group, TypeGroupEnum):
            self.type_group = TypeGroupEnum(self.type_group)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class Metabolite(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["Metabolite"]
    class_class_curie: ClassVar[str] = "edd:Metabolite"
    class_name: ClassVar[str] = "Metabolite"
    class_model_uri: ClassVar[URIRef] = EDD.Metabolite

    measurementtype_ptr_id: Optional[int] = None
    charge: Optional[int] = None
    carbon_count: Optional[int] = None
    molar_mass: Optional[float] = None
    molecular_formula: Optional[str] = None
    tags: Optional[Union[Union[str, "TagsEnum"], List[Union[str, "TagsEnum"]]]] = empty_list()
    id_map: Optional[Union[str, List[str]]] = empty_list()
    smiles: Optional[str] = None
    pubchem_cid: Optional[int] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurementtype_ptr_id is not None and not isinstance(self.measurementtype_ptr_id, int):
            self.measurementtype_ptr_id = int(self.measurementtype_ptr_id)

        if self.charge is not None and not isinstance(self.charge, int):
            self.charge = int(self.charge)

        if self.carbon_count is not None and not isinstance(self.carbon_count, int):
            self.carbon_count = int(self.carbon_count)

        if self.molar_mass is not None and not isinstance(self.molar_mass, float):
            self.molar_mass = float(self.molar_mass)

        if self.molecular_formula is not None and not isinstance(self.molecular_formula, str):
            self.molecular_formula = str(self.molecular_formula)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, TagsEnum) else TagsEnum(v) for v in self.tags]

        if not isinstance(self.id_map, list):
            self.id_map = [self.id_map] if self.id_map is not None else []
        self.id_map = [v if isinstance(v, str) else str(v) for v in self.id_map]

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.pubchem_cid is not None and not isinstance(self.pubchem_cid, int):
            self.pubchem_cid = int(self.pubchem_cid)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class MetadataType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["MetadataType"]
    class_class_curie: ClassVar[str] = "edd:MetadataType"
    class_name: ClassVar[str] = "MetadataType"
    class_model_uri: ClassVar[URIRef] = EDD.MetadataType

    id: Optional[int] = None
    type_name: Optional[str] = None
    type_i18n: Optional[str] = None
    type_field: Optional[Union[str, "TypeFieldEnum"]] = None
    input_type: Optional[Union[str, "InputTypeEnum"]] = None
    default_value: Optional[Union[str, "DefaultValueEnum"]] = None
    prefix: Optional[Union[str, "PrefixEnum"]] = None
    postfix: Optional[str] = None
    for_context: Optional[Union[str, "ForContextEnum"]] = None
    uuid: Optional[str] = None
    group_id: Optional[str] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, int):
            self.id = int(self.id)

        if self.type_name is not None and not isinstance(self.type_name, str):
            self.type_name = str(self.type_name)

        if self.type_i18n is not None and not isinstance(self.type_i18n, str):
            self.type_i18n = str(self.type_i18n)

        if self.type_field is not None and not isinstance(self.type_field, TypeFieldEnum):
            self.type_field = TypeFieldEnum(self.type_field)

        if self.input_type is not None and not isinstance(self.input_type, InputTypeEnum):
            self.input_type = InputTypeEnum(self.input_type)

        if self.default_value is not None and not isinstance(self.default_value, DefaultValueEnum):
            self.default_value = DefaultValueEnum(self.default_value)

        if self.prefix is not None and not isinstance(self.prefix, PrefixEnum):
            self.prefix = PrefixEnum(self.prefix)

        if self.postfix is not None and not isinstance(self.postfix, str):
            self.postfix = str(self.postfix)

        if self.for_context is not None and not isinstance(self.for_context, ForContextEnum):
            self.for_context = ForContextEnum(self.for_context)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        if self.group_id is not None and not isinstance(self.group_id, str):
            self.group_id = str(self.group_id)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class ProteinIdentifier(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["ProteinIdentifier"]
    class_class_curie: ClassVar[str] = "edd:ProteinIdentifier"
    class_name: ClassVar[str] = "ProteinIdentifier"
    class_model_uri: ClassVar[URIRef] = EDD.ProteinIdentifier

    measurementtype_ptr_id: Optional[int] = None
    accession_id: Optional[Union[str, List[str]]] = empty_list()
    length: Optional[float] = None
    mass: Optional[Union[str, List[str]]] = empty_list()
    accession_code: Optional[str] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurementtype_ptr_id is not None and not isinstance(self.measurementtype_ptr_id, int):
            self.measurementtype_ptr_id = int(self.measurementtype_ptr_id)

        if not isinstance(self.accession_id, list):
            self.accession_id = [self.accession_id] if self.accession_id is not None else []
        self.accession_id = [v if isinstance(v, str) else str(v) for v in self.accession_id]

        if self.length is not None and not isinstance(self.length, float):
            self.length = float(self.length)

        if not isinstance(self.mass, list):
            self.mass = [self.mass] if self.mass is not None else []
        self.mass = [v if isinstance(v, str) else str(v) for v in self.mass]

        if self.accession_code is not None and not isinstance(self.accession_code, str):
            self.accession_code = str(self.accession_code)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class ProteinStrain(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["ProteinStrain"]
    class_class_curie: ClassVar[str] = "edd:ProteinStrain"
    class_name: ClassVar[str] = "ProteinStrain"
    class_model_uri: ClassVar[URIRef] = EDD.ProteinStrain

    id: Optional[int] = None
    protein_id: Optional[int] = None
    strain_id: Optional[int] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, int):
            self.id = int(self.id)

        if self.protein_id is not None and not isinstance(self.protein_id, int):
            self.protein_id = int(self.protein_id)

        if self.strain_id is not None and not isinstance(self.strain_id, int):
            self.strain_id = int(self.strain_id)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class Protocol(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["Protocol"]
    class_class_curie: ClassVar[str] = "edd:Protocol"
    class_name: ClassVar[str] = "Protocol"
    class_model_uri: ClassVar[URIRef] = EDD.Protocol

    object_ref_id: Optional[int] = None
    categorization: Optional[Union[str, "CategorizationEnum"]] = None
    default_units_id: Optional[int] = None
    owned_by_id: Optional[int] = None
    variant_of_id: Optional[Union[str, "VariantOfIdEnum"]] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object_ref_id is not None and not isinstance(self.object_ref_id, int):
            self.object_ref_id = int(self.object_ref_id)

        if self.categorization is not None and not isinstance(self.categorization, CategorizationEnum):
            self.categorization = CategorizationEnum(self.categorization)

        if self.default_units_id is not None and not isinstance(self.default_units_id, int):
            self.default_units_id = int(self.default_units_id)

        if self.owned_by_id is not None and not isinstance(self.owned_by_id, int):
            self.owned_by_id = int(self.owned_by_id)

        if self.variant_of_id is not None and not isinstance(self.variant_of_id, VariantOfIdEnum):
            self.variant_of_id = VariantOfIdEnum(self.variant_of_id)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


@dataclass
class Strain(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EDD["Strain"]
    class_class_curie: ClassVar[str] = "edd:Strain"
    class_name: ClassVar[str] = "Strain"
    class_model_uri: ClassVar[URIRef] = EDD.Strain

    object_ref_id: Optional[int] = None
    registry_id: Optional[str] = None
    registry_url: Optional[Union[str, HttpsIdentifier]] = None
    db_instance: Optional[Union[str, "DbInstanceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.object_ref_id is not None and not isinstance(self.object_ref_id, int):
            self.object_ref_id = int(self.object_ref_id)

        if self.registry_id is not None and not isinstance(self.registry_id, str):
            self.registry_id = str(self.registry_id)

        if self.registry_url is not None and not isinstance(self.registry_url, HttpsIdentifier):
            self.registry_url = HttpsIdentifier(self.registry_url)

        if self.db_instance is not None and not isinstance(self.db_instance, DbInstanceEnum):
            self.db_instance = DbInstanceEnum(self.db_instance)

        super().__post_init__(**kwargs)


# Enumerations
class DbInstanceEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="DbInstanceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "metadata_plus.abf-public.sql",
            PermissibleValue(
                text="metadata_plus.abf-public.sql",
                description="metadata_plus.abf-public.sql"))
        setattr(cls, "metadata_plus.abf.sql",
            PermissibleValue(
                text="metadata_plus.abf.sql",
                description="metadata_plus.abf.sql"))
        setattr(cls, "metadata_plus.jbei.sql",
            PermissibleValue(
                text="metadata_plus.jbei.sql",
                description="metadata_plus.jbei.sql"))
        setattr(cls, "metadata_plus.jbei-public.sql",
            PermissibleValue(
                text="metadata_plus.jbei-public.sql",
                description="metadata_plus.jbei-public.sql"))

class TypeGroupEnum(EnumDefinitionImpl):

    h = PermissibleValue(
        text="h",
        description="h")
    g = PermissibleValue(
        text="g",
        description="g")
    m = PermissibleValue(
        text="m",
        description="m")
    _ = PermissibleValue(
        text="_",
        description="_")
    p = PermissibleValue(
        text="p",
        description="p")

    _defn = EnumDefinition(
        name="TypeGroupEnum",
    )

class ProvisionalEnum(EnumDefinitionImpl):

    t = PermissibleValue(
        text="t",
        description="t")
    f = PermissibleValue(
        text="f",
        description="f")

    _defn = EnumDefinition(
        name="ProvisionalEnum",
    )

class UnitNameEnum(EnumDefinitionImpl):

    Liters = PermissibleValue(
        text="Liters",
        description="Liters")
    uM = PermissibleValue(
        text="uM",
        description="uM")
    RPKM = PermissibleValue(
        text="RPKM",
        description="RPKM")
    Percent = PermissibleValue(
        text="Percent",
        description="Percent")
    TMM = PermissibleValue(
        text="TMM",
        description="TMM")
    nM = PermissibleValue(
        text="nM",
        description="nM")
    MEFL = PermissibleValue(
        text="MEFL",
        description="MEFL")
    milligrams = PermissibleValue(
        text="milligrams",
        description="milligrams")
    mmol = PermissibleValue(
        text="mmol",
        description="mmol")
    TPM = PermissibleValue(
        text="TPM",
        description="TPM")
    percent = PermissibleValue(
        text="percent",
        description="percent")
    intensity = PermissibleValue(
        text="intensity",
        description="intensity")
    counts = PermissibleValue(
        text="counts",
        description="counts")
    FPKM = PermissibleValue(
        text="FPKM",
        description="FPKM")
    mL = PermissibleValue(
        text="mL",
        description="mL")
    relative = PermissibleValue(
        text="relative",
        description="relative")
    milliliters = PermissibleValue(
        text="milliliters",
        description="milliliters")
    RPM = PermissibleValue(
        text="RPM",
        description="RPM")
    uL = PermissibleValue(
        text="uL",
        description="uL")
    Celsius = PermissibleValue(
        text="Celsius",
        description="Celsius")
    grams = PermissibleValue(
        text="grams",
        description="grams")
    mol = PermissibleValue(
        text="mol",
        description="mol")
    CPM = PermissibleValue(
        text="CPM",
        description="CPM")
    mM = PermissibleValue(
        text="mM",
        description="mM")
    hours = PermissibleValue(
        text="hours",
        description="hours")
    nanograms = PermissibleValue(
        text="nanograms",
        description="nanograms")
    Cmol = PermissibleValue(
        text="Cmol",
        description="Cmol")
    lpm = PermissibleValue(
        text="lpm",
        description="lpm")
    ppm = PermissibleValue(
        text="ppm",
        description="ppm")
    g = PermissibleValue(
        text="g",
        description="g")
    kilograms = PermissibleValue(
        text="kilograms",
        description="kilograms")

    _defn = EnumDefinition(
        name="UnitNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "L/h",
            PermissibleValue(
                text="L/h",
                description="L/h"))
        setattr(cls, "ug/L",
            PermissibleValue(
                text="ug/L",
                description="ug/L"))
        setattr(cls, "L/m",
            PermissibleValue(
                text="L/m",
                description="L/m"))
        setattr(cls, "spectral count",
            PermissibleValue(
                text="spectral count",
                description="spectral count"))
        setattr(cls, "proteins/cell",
            PermissibleValue(
                text="proteins/cell",
                description="proteins/cell"))
        setattr(cls, "Yield (mmole/mmole)",
            PermissibleValue(
                text="Yield (mmole/mmole)",
                description="Yield (mmole/mmole)"))
        setattr(cls, "moles / moles glucose",
            PermissibleValue(
                text="moles / moles glucose",
                description="moles / moles glucose"))
        setattr(cls, "Productivity (g/L/hr)",
            PermissibleValue(
                text="Productivity (g/L/hr)",
                description="Productivity (g/L/hr)"))
        setattr(cls, "g/L",
            PermissibleValue(
                text="g/L",
                description="g/L"))
        setattr(cls, "mol/L/hr",
            PermissibleValue(
                text="mol/L/hr",
                description="mol/L/hr"))
        setattr(cls, "Cmol/L",
            PermissibleValue(
                text="Cmol/L",
                description="Cmol/L"))
        setattr(cls, "mol/L",
            PermissibleValue(
                text="mol/L",
                description="mol/L"))
        setattr(cls, "mg/L",
            PermissibleValue(
                text="mg/L",
                description="mg/L"))
        setattr(cls, "Histogram 0.15:7.95:0.10",
            PermissibleValue(
                text="Histogram 0.15:7.95:0.10",
                description="Histogram 0.15:7.95:0.10"))
        setattr(cls, "mg SolSgr / 10 mg CW",
            PermissibleValue(
                text="mg SolSgr / 10 mg CW",
                description="mg SolSgr / 10 mg CW"))
        setattr(cls, "mmol/L/h",
            PermissibleValue(
                text="mmol/L/h",
                description="mmol/L/h"))
        setattr(cls, "n/a",
            PermissibleValue(
                text="n/a",
                description="n/a"))

class DisplayEnum(EnumDefinitionImpl):

    t = PermissibleValue(
        text="t",
        description="t")
    f = PermissibleValue(
        text="f",
        description="f")

    _defn = EnumDefinition(
        name="DisplayEnum",
    )

class AlternateNamesEnum(EnumDefinitionImpl):

    µM = PermissibleValue(
        text="µM",
        description="µM")
    ng = PermissibleValue(
        text="ng",
        description="ng")
    uM = PermissibleValue(
        text="uM",
        description="uM")
    kg = PermissibleValue(
        text="kg",
        description="kg")
    grams = PermissibleValue(
        text="grams",
        description="grams")
    L = PermissibleValue(
        text="L",
        description="L")
    g = PermissibleValue(
        text="g",
        description="g")
    Percent = PermissibleValue(
        text="Percent",
        description="Percent")
    nanomolar = PermissibleValue(
        text="nanomolar",
        description="nanomolar")
    mL = PermissibleValue(
        text="mL",
        description="mL")
    mg = PermissibleValue(
        text="mg",
        description="mg")
    µL = PermissibleValue(
        text="µL",
        description="µL")

    _defn = EnumDefinition(
        name="AlternateNamesEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mmol/L",
            PermissibleValue(
                text="mmol/L",
                description="mmol/L"))
        setattr(cls, "g/L/hr",
            PermissibleValue(
                text="g/L/hr",
                description="g/L/hr"))
        setattr(cls, "µg/L",
            PermissibleValue(
                text="µg/L",
                description="µg/L"))
        setattr(cls, "mmole/mmole",
            PermissibleValue(
                text="mmole/mmole",
                description="mmole/mmole"))
        setattr(cls, "mmole/mmodel",
            PermissibleValue(
                text="mmole/mmodel",
                description="mmole/mmodel"))

class TagsEnum(EnumDefinitionImpl):

    LCMS = PermissibleValue(
        text="LCMS",
        description="LCMS")
    Mevalonate = PermissibleValue(
        text="Mevalonate",
        description="Mevalonate")
    tag = PermissibleValue(
        text="tag",
        description="tag")
    HPLC = PermissibleValue(
        text="HPLC",
        description="HPLC")

    _defn = EnumDefinition(
        name="TagsEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Acetyl-CoA",
            PermissibleValue(
                text="Acetyl-CoA",
                description="Acetyl-CoA"))
        setattr(cls, "needs-verification",
            PermissibleValue(
                text="needs-verification",
                description="needs-verification"))
        setattr(cls, "Mevalonate Pathway",
            PermissibleValue(
                text="Mevalonate Pathway",
                description="Mevalonate Pathway"))
        setattr(cls, "needs-validation",
            PermissibleValue(
                text="needs-validation",
                description="needs-validation"))

class TypeFieldEnum(EnumDefinitionImpl):

    description = PermissibleValue(
        text="description",
        description="description")
    control = PermissibleValue(
        text="control",
        description="control")
    flush = PermissibleValue(
        text="flush",
        description="flush")
    contact_extra = PermissibleValue(
        text="contact_extra",
        description="contact_extra")
    strains = PermissibleValue(
        text="strains",
        description="strains")
    carbon_source = PermissibleValue(
        text="carbon_source",
        description="carbon_source")
    experimenter = PermissibleValue(
        text="experimenter",
        description="experimenter")
    NONE = PermissibleValue(
        text="NONE",
        description="None")
    contact = PermissibleValue(
        text="contact",
        description="contact")

    _defn = EnumDefinition(
        name="TypeFieldEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "37",
            PermissibleValue(
                text="37",
                description="37"))
        setattr(cls, "0.1",
            PermissibleValue(
                text="0.1",
                description="0.1"))
        setattr(cls, "200",
            PermissibleValue(
                text="200",
                description="200"))
        setattr(cls, "--",
            PermissibleValue(
                text="--",
                description="--"))

class InputTypeEnum(EnumDefinitionImpl):

    replicate = PermissibleValue(
        text="replicate",
        description="replicate")
    strain = PermissibleValue(
        text="strain",
        description="strain")
    user = PermissibleValue(
        text="user",
        description="user")
    textarea = PermissibleValue(
        text="textarea",
        description="textarea")
    carbon_source = PermissibleValue(
        text="carbon_source",
        description="carbon_source")
    checkbox = PermissibleValue(
        text="checkbox",
        description="checkbox")

    _defn = EnumDefinition(
        name="InputTypeEnum",
    )

class DefaultValueEnum(EnumDefinitionImpl):

    ºC = PermissibleValue(
        text="ºC",
        description="ºC")
    rpm = PermissibleValue(
        text="rpm",
        description="rpm")
    flush = PermissibleValue(
        text="flush",
        description="flush")
    hr = PermissibleValue(
        text="hr",
        description="hr")
    mL = PermissibleValue(
        text="mL",
        description="mL")
    mM = PermissibleValue(
        text="mM",
        description="mM")
    NONE = PermissibleValue(
        text="NONE",
        description="None")
    mm = PermissibleValue(
        text="mm",
        description="mm")

    _defn = EnumDefinition(
        name="DefaultValueEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "37",
            PermissibleValue(
                text="37",
                description="37"))
        setattr(cls, "°C",
            PermissibleValue(
                text="°C",
                description="°C"))
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="1"))
        setattr(cls, "bsa-fast-13min-cold.m",
            PermissibleValue(
                text="bsa-fast-13min-cold.m",
                description="bsa-fast-13min-cold.m"))
        setattr(cls, "200",
            PermissibleValue(
                text="200",
                description="200"))
        setattr(cls, "--",
            PermissibleValue(
                text="--",
                description="--"))
        setattr(cls, "Vial 1",
            PermissibleValue(
                text="Vial 1",
                description="Vial 1"))
        setattr(cls, "0.1",
            PermissibleValue(
                text="0.1",
                description="0.1"))

class PrefixEnum(EnumDefinitionImpl):

    A = PermissibleValue(
        text="A",
        description="A")
    L = PermissibleValue(
        text="L",
        description="L")
    S = PermissibleValue(
        text="S",
        description="S")

    _defn = EnumDefinition(
        name="PrefixEnum",
    )

class ForContextEnum(EnumDefinitionImpl):

    replicate = PermissibleValue(
        text="replicate",
        description="replicate")
    string = PermissibleValue(
        text="string",
        description="string")
    A = PermissibleValue(
        text="A",
        description="A")
    L = PermissibleValue(
        text="L",
        description="L")
    strain = PermissibleValue(
        text="strain",
        description="strain")
    user = PermissibleValue(
        text="user",
        description="user")
    textarea = PermissibleValue(
        text="textarea",
        description="textarea")
    S = PermissibleValue(
        text="S",
        description="S")
    carbon_source = PermissibleValue(
        text="carbon_source",
        description="carbon_source")
    checkbox = PermissibleValue(
        text="checkbox",
        description="checkbox")

    _defn = EnumDefinition(
        name="ForContextEnum",
    )

class CategorizationEnum(EnumDefinitionImpl):

    OD = PermissibleValue(
        text="OD",
        description="OD")
    LCMS = PermissibleValue(
        text="LCMS",
        description="LCMS")
    TPOMICS = PermissibleValue(
        text="TPOMICS",
        description="TPOMICS")
    NA = PermissibleValue(
        text="NA",
        description="NA")
    HPLC = PermissibleValue(
        text="HPLC",
        description="HPLC")

    _defn = EnumDefinition(
        name="CategorizationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "5",
            PermissibleValue(
                text="5",
                description="5"))
        setattr(cls, "7",
            PermissibleValue(
                text="7",
                description="7"))
        setattr(cls, "3",
            PermissibleValue(
                text="3",
                description="3"))
        setattr(cls, "10",
            PermissibleValue(
                text="10",
                description="10"))
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="1"))
        setattr(cls, "6",
            PermissibleValue(
                text="6",
                description="6"))

class VariantOfIdEnum(EnumDefinitionImpl):

    OD = PermissibleValue(
        text="OD",
        description="OD")
    RAMOS = PermissibleValue(
        text="RAMOS",
        description="RAMOS")
    LCMS = PermissibleValue(
        text="LCMS",
        description="LCMS")
    TPOMICS = PermissibleValue(
        text="TPOMICS",
        description="TPOMICS")
    NA = PermissibleValue(
        text="NA",
        description="NA")
    HPLC = PermissibleValue(
        text="HPLC",
        description="HPLC")

    _defn = EnumDefinition(
        name="VariantOfIdEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "7948",
            PermissibleValue(
                text="7948",
                description="7948"))

# Slots
class slots:
    pass

slots.measurementtype_ptr_id = Slot(uri=EDD.measurementtype_ptr_id, name="measurementtype_ptr_id", curie=EDD.curie('measurementtype_ptr_id'),
                   model_uri=EDD.measurementtype_ptr_id, domain=None, range=Optional[int])

slots.gene_length = Slot(uri=EDD.gene_length, name="gene_length", curie=EDD.curie('gene_length'),
                   model_uri=EDD.gene_length, domain=None, range=Optional[str])

slots.db_instance = Slot(uri=EDD.db_instance, name="db_instance", curie=EDD.curie('db_instance'),
                   model_uri=EDD.db_instance, domain=None, range=Optional[Union[str, "DbInstanceEnum"]])

slots.id = Slot(uri=EDD.id, name="id", curie=EDD.curie('id'),
                   model_uri=EDD.id, domain=None, range=Optional[int])

slots.type_name = Slot(uri=EDD.type_name, name="type_name", curie=EDD.curie('type_name'),
                   model_uri=EDD.type_name, domain=None, range=Optional[str])

slots.short_name = Slot(uri=EDD.short_name, name="short_name", curie=EDD.curie('short_name'),
                   model_uri=EDD.short_name, domain=None, range=Optional[str])

slots.type_group = Slot(uri=EDD.type_group, name="type_group", curie=EDD.curie('type_group'),
                   model_uri=EDD.type_group, domain=None, range=Optional[Union[str, "TypeGroupEnum"]])

slots.uuid = Slot(uri=EDD.uuid, name="uuid", curie=EDD.curie('uuid'),
                   model_uri=EDD.uuid, domain=None, range=Optional[str])

slots.type_source_id = Slot(uri=EDD.type_source_id, name="type_source_id", curie=EDD.curie('type_source_id'),
                   model_uri=EDD.type_source_id, domain=None, range=Optional[str])

slots.alt_names = Slot(uri=EDD.alt_names, name="alt_names", curie=EDD.curie('alt_names'),
                   model_uri=EDD.alt_names, domain=None, range=Optional[Union[str, List[str]]])

slots.provisional = Slot(uri=EDD.provisional, name="provisional", curie=EDD.curie('provisional'),
                   model_uri=EDD.provisional, domain=None, range=Optional[Union[str, "ProvisionalEnum"]])

slots.unit_name = Slot(uri=EDD.unit_name, name="unit_name", curie=EDD.curie('unit_name'),
                   model_uri=EDD.unit_name, domain=None, range=Optional[Union[str, "UnitNameEnum"]])

slots.display = Slot(uri=EDD.display, name="display", curie=EDD.curie('display'),
                   model_uri=EDD.display, domain=None, range=Optional[Union[str, "DisplayEnum"]])

slots.alternate_names = Slot(uri=EDD.alternate_names, name="alternate_names", curie=EDD.curie('alternate_names'),
                   model_uri=EDD.alternate_names, domain=None, range=Optional[Union[str, "AlternateNamesEnum"]])

slots.charge = Slot(uri=EDD.charge, name="charge", curie=EDD.curie('charge'),
                   model_uri=EDD.charge, domain=None, range=Optional[int])

slots.carbon_count = Slot(uri=EDD.carbon_count, name="carbon_count", curie=EDD.curie('carbon_count'),
                   model_uri=EDD.carbon_count, domain=None, range=Optional[int])

slots.molar_mass = Slot(uri=EDD.molar_mass, name="molar_mass", curie=EDD.curie('molar_mass'),
                   model_uri=EDD.molar_mass, domain=None, range=Optional[float])

slots.molecular_formula = Slot(uri=EDD.molecular_formula, name="molecular_formula", curie=EDD.curie('molecular_formula'),
                   model_uri=EDD.molecular_formula, domain=None, range=Optional[str])

slots.tags = Slot(uri=EDD.tags, name="tags", curie=EDD.curie('tags'),
                   model_uri=EDD.tags, domain=None, range=Optional[Union[Union[str, "TagsEnum"], List[Union[str, "TagsEnum"]]]])

slots.id_map = Slot(uri=EDD.id_map, name="id_map", curie=EDD.curie('id_map'),
                   model_uri=EDD.id_map, domain=None, range=Optional[Union[str, List[str]]])

slots.smiles = Slot(uri=EDD.smiles, name="smiles", curie=EDD.curie('smiles'),
                   model_uri=EDD.smiles, domain=None, range=Optional[str])

slots.pubchem_cid = Slot(uri=EDD.pubchem_cid, name="pubchem_cid", curie=EDD.curie('pubchem_cid'),
                   model_uri=EDD.pubchem_cid, domain=None, range=Optional[int])

slots.type_i18n = Slot(uri=EDD.type_i18n, name="type_i18n", curie=EDD.curie('type_i18n'),
                   model_uri=EDD.type_i18n, domain=None, range=Optional[str])

slots.type_field = Slot(uri=EDD.type_field, name="type_field", curie=EDD.curie('type_field'),
                   model_uri=EDD.type_field, domain=None, range=Optional[Union[str, "TypeFieldEnum"]])

slots.input_type = Slot(uri=EDD.input_type, name="input_type", curie=EDD.curie('input_type'),
                   model_uri=EDD.input_type, domain=None, range=Optional[Union[str, "InputTypeEnum"]])

slots.default_value = Slot(uri=EDD.default_value, name="default_value", curie=EDD.curie('default_value'),
                   model_uri=EDD.default_value, domain=None, range=Optional[Union[str, "DefaultValueEnum"]])

slots.prefix = Slot(uri=EDD.prefix, name="prefix", curie=EDD.curie('prefix'),
                   model_uri=EDD.prefix, domain=None, range=Optional[Union[str, "PrefixEnum"]])

slots.postfix = Slot(uri=EDD.postfix, name="postfix", curie=EDD.curie('postfix'),
                   model_uri=EDD.postfix, domain=None, range=Optional[str])

slots.for_context = Slot(uri=EDD.for_context, name="for_context", curie=EDD.curie('for_context'),
                   model_uri=EDD.for_context, domain=None, range=Optional[Union[str, "ForContextEnum"]])

slots.group_id = Slot(uri=EDD.group_id, name="group_id", curie=EDD.curie('group_id'),
                   model_uri=EDD.group_id, domain=None, range=Optional[str])

slots.accession_id = Slot(uri=EDD.accession_id, name="accession_id", curie=EDD.curie('accession_id'),
                   model_uri=EDD.accession_id, domain=None, range=Optional[Union[str, List[str]]])

slots.length = Slot(uri=EDD.length, name="length", curie=EDD.curie('length'),
                   model_uri=EDD.length, domain=None, range=Optional[float])

slots.mass = Slot(uri=EDD.mass, name="mass", curie=EDD.curie('mass'),
                   model_uri=EDD.mass, domain=None, range=Optional[Union[str, List[str]]])

slots.accession_code = Slot(uri=EDD.accession_code, name="accession_code", curie=EDD.curie('accession_code'),
                   model_uri=EDD.accession_code, domain=None, range=Optional[str])

slots.protein_id = Slot(uri=EDD.protein_id, name="protein_id", curie=EDD.curie('protein_id'),
                   model_uri=EDD.protein_id, domain=None, range=Optional[int])

slots.strain_id = Slot(uri=EDD.strain_id, name="strain_id", curie=EDD.curie('strain_id'),
                   model_uri=EDD.strain_id, domain=None, range=Optional[int])

slots.object_ref_id = Slot(uri=EDD.object_ref_id, name="object_ref_id", curie=EDD.curie('object_ref_id'),
                   model_uri=EDD.object_ref_id, domain=None, range=Optional[int])

slots.categorization = Slot(uri=EDD.categorization, name="categorization", curie=EDD.curie('categorization'),
                   model_uri=EDD.categorization, domain=None, range=Optional[Union[str, "CategorizationEnum"]])

slots.default_units_id = Slot(uri=EDD.default_units_id, name="default_units_id", curie=EDD.curie('default_units_id'),
                   model_uri=EDD.default_units_id, domain=None, range=Optional[int])

slots.owned_by_id = Slot(uri=EDD.owned_by_id, name="owned_by_id", curie=EDD.curie('owned_by_id'),
                   model_uri=EDD.owned_by_id, domain=None, range=Optional[int])

slots.variant_of_id = Slot(uri=EDD.variant_of_id, name="variant_of_id", curie=EDD.curie('variant_of_id'),
                   model_uri=EDD.variant_of_id, domain=None, range=Optional[Union[str, "VariantOfIdEnum"]])

slots.registry_id = Slot(uri=EDD.registry_id, name="registry_id", curie=EDD.curie('registry_id'),
                   model_uri=EDD.registry_id, domain=None, range=Optional[str])

slots.registry_url = Slot(uri=EDD.registry_url, name="registry_url", curie=EDD.curie('registry_url'),
                   model_uri=EDD.registry_url, domain=None, range=Optional[Union[str, HttpsIdentifier]])