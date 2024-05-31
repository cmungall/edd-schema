
# edd


**metamodel version:** 1.7.0

**version:** None


NON-OFFICIAL rendering of EDD schema as LinkML (for demo purposes)


### Classes

 * [MeasurementType](MeasurementType.md)
 * [MeasurementUnit](MeasurementUnit.md)
 * [Metabolite](Metabolite.md)
 * [MetadataType](MetadataType.md)
 * [ProteinIdentifier](ProteinIdentifier.md)
 * [ProteinStrain](ProteinStrain.md)
 * [Protocol](Protocol.md)
 * [Strain](Strain.md)
 * [GeneIdentifier](GeneIdentifier.md)

### Mixins


### Slots

 * [accession_code](accession_code.md)
 * [accession_id](accession_id.md)
 * [alt_names](alt_names.md)
 * [alternate_names](alternate_names.md)
 * [carbon_count](carbon_count.md)
 * [categorization](categorization.md)
 * [charge](charge.md)
 * [db_instance](db_instance.md)
 * [default_units_id](default_units_id.md)
 * [default_value](default_value.md)
 * [display](display.md)
 * [for_context](for_context.md)
 * [gene_length](gene_length.md)
 * [group_id](group_id.md)
 * [id](id.md)
 * [id_map](id_map.md)
 * [input_type](input_type.md)
 * [length](length.md)
 * [mass](mass.md)
 * [measurementtype_ptr_id](measurementtype_ptr_id.md)
 * [molar_mass](molar_mass.md)
 * [molecular_formula](molecular_formula.md)
 * [object_ref_id](object_ref_id.md)
 * [owned_by_id](owned_by_id.md)
 * [postfix](postfix.md)
 * [prefix](prefix.md)
 * [protein_id](protein_id.md)
 * [provisional](provisional.md)
 * [pubchem_cid](pubchem_cid.md)
 * [registry_id](registry_id.md)
 * [registry_url](registry_url.md)
 * [short_name](short_name.md)
 * [smiles](smiles.md)
 * [strain_id](strain_id.md)
 * [tags](tags.md)
 * [type_field](type_field.md)
 * [type_group](type_group.md)
 * [type_i18n](type_i18n.md)
 * [type_name](type_name.md)
 * [type_source_id](type_source_id.md)
 * [unit_name](unit_name.md)
 * [uuid](uuid.md)
 * [variant_of_id](variant_of_id.md)

### Enums

 * [alternate_names_enum](alternate_names_enum.md)
 * [categorization_enum](categorization_enum.md)
 * [db_instance_enum](db_instance_enum.md)
 * [default_value_enum](default_value_enum.md)
 * [display_enum](display_enum.md)
 * [for_context_enum](for_context_enum.md)
 * [input_type_enum](input_type_enum.md)
 * [prefix_enum](prefix_enum.md)
 * [provisional_enum](provisional_enum.md)
 * [tags_enum](tags_enum.md)
 * [type_field_enum](type_field_enum.md)
 * [type_group_enum](type_group_enum.md)
 * [unit_name_enum](unit_name_enum.md)
 * [variant_of_id_enum](variant_of_id_enum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [HttpsIdentifier](types/HttpsIdentifier.md)  ([String](types/String.md)) 
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
