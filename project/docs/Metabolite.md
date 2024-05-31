
# Class: Metabolite



URI: [edd:Metabolite](https://w3id.org/eddMetabolite)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Metabolite&#124;measurementtype_ptr_id:integer%20%3F;charge:integer%20%3F;carbon_count:integer%20%3F;molar_mass:float%20%3F;molecular_formula:string%20%3F;tags:tags_enum%20*;id_map:string%20*;smiles:string%20%3F;pubchem_cid:integer%20%3F;db_instance:db_instance_enum%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Metabolite&#124;measurementtype_ptr_id:integer%20%3F;charge:integer%20%3F;carbon_count:integer%20%3F;molar_mass:float%20%3F;molecular_formula:string%20%3F;tags:tags_enum%20*;id_map:string%20*;smiles:string%20%3F;pubchem_cid:integer%20%3F;db_instance:db_instance_enum%20%3F])

## Attributes


### Own

 * [measurementtype_ptr_id](measurementtype_ptr_id.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
     * Example: 260597 None
 * [charge](charge.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
     * Example: 0 None
 * [carbon_count](carbon_count.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
     * Example: 6 None
 * [molar_mass](molar_mass.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
     * Example: 113.16000 None
 * [molecular_formula](molecular_formula.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: C6H11NO None
 * [tags](tags.md)  <sub>0..\*</sub>
     * Range: [tags_enum](tags_enum.md)
     * Example: needs-validation None
 * [id_map](id_map.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: CHEBI:CHEBI:16608|KEGG Compound:C03845|CHEBI:CHEBI:2139|Human Metabolome Database:HMDB06841|MetaNetX (MNX) Chemical:MNXM2494|Human Metabolome Database:HMDB06541|LipidMaps:LMST01010096|BioCyc:META:CPD-8621|CHEBI:CHEBI:12170|CHEBI:CHEBI:20645|SEED Compound:cpd02398|Human Metabolome Database:HMDB59618 None
 * [smiles](smiles.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: C1CCC(=O)NCC1 None
 * [pubchem_cid](pubchem_cid.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
     * Example: 7768 None
 * [db_instance](db_instance.md)  <sub>0..1</sub>
     * Range: [db_instance_enum](db_instance_enum.md)
     * Example: metadata_plus.jbei.sql None
