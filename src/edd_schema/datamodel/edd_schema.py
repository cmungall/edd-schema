from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class DbInstanceEnum(str, Enum):
    # metadata_plus.abf-public.sql
    metadata_plusFULL_STOPabf_publicFULL_STOPsql = "metadata_plus.abf-public.sql"
    # metadata_plus.abf.sql
    metadata_plusFULL_STOPabfFULL_STOPsql = "metadata_plus.abf.sql"
    # metadata_plus.jbei.sql
    metadata_plusFULL_STOPjbeiFULL_STOPsql = "metadata_plus.jbei.sql"
    # metadata_plus.jbei-public.sql
    metadata_plusFULL_STOPjbei_publicFULL_STOPsql = "metadata_plus.jbei-public.sql"


class TypeGroupEnum(str, Enum):
    # h
    h = "h"
    # g
    g = "g"
    # m
    m = "m"
    # _
    _ = "_"
    # p
    p = "p"


class ProvisionalEnum(str, Enum):
    # t
    t = "t"
    # f
    f = "f"


class UnitNameEnum(str, Enum):
    # L/h
    LSOLIDUSh = "L/h"
    # Liters
    Liters = "Liters"
    # uM
    uM = "uM"
    # RPKM
    RPKM = "RPKM"
    # ug/L
    ugSOLIDUSL = "ug/L"
    # Percent
    Percent = "Percent"
    # TMM
    TMM = "TMM"
    # nM
    nM = "nM"
    # MEFL
    MEFL = "MEFL"
    # milligrams
    milligrams = "milligrams"
    # mmol
    mmol = "mmol"
    # L/m
    LSOLIDUSm = "L/m"
    # spectral count
    spectral_count = "spectral count"
    # TPM
    TPM = "TPM"
    # proteins/cell
    proteinsSOLIDUScell = "proteins/cell"
    # percent
    percent = "percent"
    # Yield (mmole/mmole)
    Yield_LEFT_PARENTHESISmmoleSOLIDUSmmoleRIGHT_PARENTHESIS = "Yield (mmole/mmole)"
    # moles / moles glucose
    moles_SOLIDUS_moles_glucose = "moles / moles glucose"
    # intensity
    intensity = "intensity"
    # counts
    counts = "counts"
    # FPKM
    FPKM = "FPKM"
    # Productivity (g/L/hr)
    Productivity_LEFT_PARENTHESISgSOLIDUSLSOLIDUShrRIGHT_PARENTHESIS = "Productivity (g/L/hr)"
    # mL
    mL = "mL"
    # relative
    relative = "relative"
    # milliliters
    milliliters = "milliliters"
    # RPM
    RPM = "RPM"
    # g/L
    gSOLIDUSL = "g/L"
    # mol/L/hr
    molSOLIDUSLSOLIDUShr = "mol/L/hr"
    # uL
    uL = "uL"
    # Cmol/L
    CmolSOLIDUSL = "Cmol/L"
    # mol/L
    molSOLIDUSL = "mol/L"
    # Celsius
    Celsius = "Celsius"
    # mg/L
    mgSOLIDUSL = "mg/L"
    # grams
    grams = "grams"
    # mol
    mol = "mol"
    # CPM
    CPM = "CPM"
    # Histogram 0.15:7.95:0.10
    Histogram_0FULL_STOP15COLON7FULL_STOP95COLON0FULL_STOP10 = "Histogram 0.15:7.95:0.10"
    # mM
    mM = "mM"
    # hours
    hours = "hours"
    # mg SolSgr / 10 mg CW
    mg_SolSgr_SOLIDUS_10_mg_CW = "mg SolSgr / 10 mg CW"
    # mmol/L/h
    mmolSOLIDUSLSOLIDUSh = "mmol/L/h"
    # nanograms
    nanograms = "nanograms"
    # Cmol
    Cmol = "Cmol"
    # lpm
    lpm = "lpm"
    # ppm
    ppm = "ppm"
    # g
    g = "g"
    # kilograms
    kilograms = "kilograms"
    # n/a
    nSOLIDUSa = "n/a"


class DisplayEnum(str, Enum):
    # t
    t = "t"
    # f
    f = "f"


class AlternateNamesEnum(str, Enum):
    # µM
    µM = "µM"
    # ng
    ng = "ng"
    # mmol/L
    mmolSOLIDUSL = "mmol/L"
    # uM
    uM = "uM"
    # kg
    kg = "kg"
    # grams
    grams = "grams"
    # L
    L = "L"
    # g
    g = "g"
    # Percent
    Percent = "Percent"
    # g/L/hr
    gSOLIDUSLSOLIDUShr = "g/L/hr"
    # µg/L
    µgSOLIDUSL = "µg/L"
    # nanomolar
    nanomolar = "nanomolar"
    # mmole/mmole
    mmoleSOLIDUSmmole = "mmole/mmole"
    # mL
    mL = "mL"
    # mg
    mg = "mg"
    # µL
    µL = "µL"
    # mmole/mmodel
    mmoleSOLIDUSmmodel = "mmole/mmodel"


class TagsEnum(str, Enum):
    # LCMS
    LCMS = "LCMS"
    # Mevalonate
    Mevalonate = "Mevalonate"
    # Acetyl-CoA
    Acetyl_CoA = "Acetyl-CoA"
    # tag
    tag = "tag"
    # needs-verification
    needs_verification = "needs-verification"
    # Mevalonate Pathway
    Mevalonate_Pathway = "Mevalonate Pathway"
    # HPLC
    HPLC = "HPLC"
    # needs-validation
    needs_validation = "needs-validation"


class TypeFieldEnum(str, Enum):
    # 37
    number_37 = "37"
    # description
    description = "description"
    # control
    control = "control"
    # flush
    flush = "flush"
    # 0.1
    number_0FULL_STOP1 = "0.1"
    # contact_extra
    contact_extra = "contact_extra"
    # strains
    strains = "strains"
    # 200
    number_200 = "200"
    # carbon_source
    carbon_source = "carbon_source"
    # experimenter
    experimenter = "experimenter"
    # None
    NONE = "NONE"
    # --
    __ = "--"
    # contact
    contact = "contact"


class InputTypeEnum(str, Enum):
    # replicate
    replicate = "replicate"
    # strain
    strain = "strain"
    # user
    user = "user"
    # textarea
    textarea = "textarea"
    # carbon_source
    carbon_source = "carbon_source"
    # checkbox
    checkbox = "checkbox"


class DefaultValueEnum(str, Enum):
    # 37
    number_37 = "37"
    # °C
    DEGREE_SIGNC = "°C"
    # ºC
    ºC = "ºC"
    # rpm
    rpm = "rpm"
    # 1
    number_1 = "1"
    # bsa-fast-13min-cold.m
    bsa_fast_13min_coldFULL_STOPm = "bsa-fast-13min-cold.m"
    # flush
    flush = "flush"
    # hr
    hr = "hr"
    # mL
    mL = "mL"
    # mM
    mM = "mM"
    # 200
    number_200 = "200"
    # --
    __ = "--"
    # None
    NONE = "NONE"
    # mm
    mm = "mm"
    # Vial 1
    Vial_1 = "Vial 1"
    # 0.1
    number_0FULL_STOP1 = "0.1"


class PrefixEnum(str, Enum):
    # A
    A = "A"
    # L
    L = "L"
    # S
    S = "S"


class ForContextEnum(str, Enum):
    # replicate
    replicate = "replicate"
    # string
    string = "string"
    # A
    A = "A"
    # L
    L = "L"
    # strain
    strain = "strain"
    # user
    user = "user"
    # textarea
    textarea = "textarea"
    # S
    S = "S"
    # carbon_source
    carbon_source = "carbon_source"
    # checkbox
    checkbox = "checkbox"


class CategorizationEnum(str, Enum):
    # 5
    number_5 = "5"
    # 7
    number_7 = "7"
    # OD
    OD = "OD"
    # 3
    number_3 = "3"
    # 10
    number_10 = "10"
    # LCMS
    LCMS = "LCMS"
    # 1
    number_1 = "1"
    # 6
    number_6 = "6"
    # TPOMICS
    TPOMICS = "TPOMICS"
    # NA
    NA = "NA"
    # HPLC
    HPLC = "HPLC"


class VariantOfIdEnum(str, Enum):
    # OD
    OD = "OD"
    # RAMOS
    RAMOS = "RAMOS"
    # LCMS
    LCMS = "LCMS"
    # 7948
    number_7948 = "7948"
    # TPOMICS
    TPOMICS = "TPOMICS"
    # NA
    NA = "NA"
    # HPLC
    HPLC = "HPLC"


class GeneIdentifier(ConfiguredBaseModel):
    measurementtype_ptr_id: Optional[int] = Field(None)
    gene_length: Optional[str] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class MeasurementType(ConfiguredBaseModel):
    id: Optional[int] = Field(None)
    type_name: Optional[str] = Field(None)
    short_name: Optional[str] = Field(None)
    type_group: Optional[TypeGroupEnum] = Field(None)
    uuid: Optional[str] = Field(None)
    type_source_id: Optional[str] = Field(None)
    alt_names: Optional[List[str]] = Field(default_factory=list)
    provisional: Optional[ProvisionalEnum] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class MeasurementUnit(ConfiguredBaseModel):
    id: Optional[int] = Field(None)
    unit_name: Optional[UnitNameEnum] = Field(None)
    display: Optional[DisplayEnum] = Field(None)
    alternate_names: Optional[AlternateNamesEnum] = Field(None)
    type_group: Optional[TypeGroupEnum] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class Metabolite(ConfiguredBaseModel):
    measurementtype_ptr_id: Optional[int] = Field(None)
    charge: Optional[int] = Field(None)
    carbon_count: Optional[int] = Field(None)
    molar_mass: Optional[float] = Field(None)
    molecular_formula: Optional[str] = Field(None)
    tags: Optional[List[TagsEnum]] = Field(default_factory=list)
    id_map: Optional[List[str]] = Field(default_factory=list)
    smiles: Optional[str] = Field(None)
    pubchem_cid: Optional[int] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class MetadataType(ConfiguredBaseModel):
    id: Optional[int] = Field(None)
    type_name: Optional[str] = Field(None)
    type_i18n: Optional[str] = Field(None)
    type_field: Optional[TypeFieldEnum] = Field(None)
    input_type: Optional[InputTypeEnum] = Field(None)
    default_value: Optional[DefaultValueEnum] = Field(None)
    prefix: Optional[PrefixEnum] = Field(None)
    postfix: Optional[str] = Field(None)
    for_context: Optional[ForContextEnum] = Field(None)
    uuid: Optional[str] = Field(None)
    group_id: Optional[str] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class ProteinIdentifier(ConfiguredBaseModel):
    measurementtype_ptr_id: Optional[int] = Field(None)
    accession_id: Optional[List[str]] = Field(default_factory=list)
    length: Optional[float] = Field(None)
    mass: Optional[List[str]] = Field(default_factory=list)
    accession_code: Optional[str] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class ProteinStrain(ConfiguredBaseModel):
    id: Optional[int] = Field(None)
    protein_id: Optional[int] = Field(None)
    strain_id: Optional[int] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class Protocol(ConfiguredBaseModel):
    object_ref_id: Optional[int] = Field(None)
    categorization: Optional[CategorizationEnum] = Field(None)
    default_units_id: Optional[int] = Field(None)
    owned_by_id: Optional[int] = Field(None)
    variant_of_id: Optional[VariantOfIdEnum] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


class Strain(ConfiguredBaseModel):
    object_ref_id: Optional[int] = Field(None)
    registry_id: Optional[str] = Field(None)
    registry_url: Optional[str] = Field(None)
    db_instance: Optional[DbInstanceEnum] = Field(None)


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
GeneIdentifier.model_rebuild()
MeasurementType.model_rebuild()
MeasurementUnit.model_rebuild()
Metabolite.model_rebuild()
MetadataType.model_rebuild()
ProteinIdentifier.model_rebuild()
ProteinStrain.model_rebuild()
Protocol.model_rebuild()
Strain.model_rebuild()

