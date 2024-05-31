
# Class: ProteinIdentifier



URI: [edd:ProteinIdentifier](https://w3id.org/eddProteinIdentifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinIdentifier&#124;measurementtype_ptr_id:integer%20%3F;accession_id:string%20*;length:float%20%3F;mass:string%20*;accession_code:string%20%3F;db_instance:db_instance_enum%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinIdentifier&#124;measurementtype_ptr_id:integer%20%3F;accession_id:string%20*;length:float%20%3F;mass:string%20*;accession_code:string%20%3F;db_instance:db_instance_enum%20%3F])

## Attributes


### Own

 * [measurementtype_ptr_id](measurementtype_ptr_id.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
     * Example: 260597 None
 * [accession_id](accession_id.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: 575 None
 * [length](length.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
     * Example: 62153.00000 None
 * [mass](mass.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: JDK_p00002 None
 * [accession_code](accession_code.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: P77495 None
 * [db_instance](db_instance.md)  <sub>0..1</sub>
     * Range: [db_instance_enum](db_instance_enum.md)
     * Example: metadata_plus.jbei.sql None
