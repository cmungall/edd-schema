-- # Class: "gene_identifier" Description: ""
--     * Slot: id Description: 
--     * Slot: measurementtype_ptr_id Description: 
--     * Slot: gene_length Description: 
--     * Slot: db_instance Description: 
-- # Class: "MeasurementType" Description: ""
--     * Slot: uid Description: 
--     * Slot: id Description: 
--     * Slot: type_name Description: 
--     * Slot: short_name Description: 
--     * Slot: type_group Description: 
--     * Slot: uuid Description: 
--     * Slot: type_source_id Description: 
--     * Slot: provisional Description: 
--     * Slot: db_instance Description: 
-- # Class: "MeasurementUnit" Description: ""
--     * Slot: uid Description: 
--     * Slot: id Description: 
--     * Slot: unit_name Description: 
--     * Slot: display Description: 
--     * Slot: alternate_names Description: 
--     * Slot: type_group Description: 
--     * Slot: db_instance Description: 
-- # Class: "Metabolite" Description: ""
--     * Slot: id Description: 
--     * Slot: measurementtype_ptr_id Description: 
--     * Slot: charge Description: 
--     * Slot: carbon_count Description: 
--     * Slot: molar_mass Description: 
--     * Slot: molecular_formula Description: 
--     * Slot: smiles Description: 
--     * Slot: pubchem_cid Description: 
--     * Slot: db_instance Description: 
-- # Class: "MetadataType" Description: ""
--     * Slot: uid Description: 
--     * Slot: id Description: 
--     * Slot: type_name Description: 
--     * Slot: type_i18n Description: 
--     * Slot: type_field Description: 
--     * Slot: input_type Description: 
--     * Slot: default_value Description: 
--     * Slot: prefix Description: 
--     * Slot: postfix Description: 
--     * Slot: for_context Description: 
--     * Slot: uuid Description: 
--     * Slot: group_id Description: 
--     * Slot: db_instance Description: 
-- # Class: "ProteinIdentifier" Description: ""
--     * Slot: id Description: 
--     * Slot: measurementtype_ptr_id Description: 
--     * Slot: length Description: 
--     * Slot: accession_code Description: 
--     * Slot: db_instance Description: 
-- # Class: "ProteinStrain" Description: ""
--     * Slot: uid Description: 
--     * Slot: id Description: 
--     * Slot: protein_id Description: 
--     * Slot: strain_id Description: 
--     * Slot: db_instance Description: 
-- # Class: "Protocol" Description: ""
--     * Slot: id Description: 
--     * Slot: object_ref_id Description: 
--     * Slot: categorization Description: 
--     * Slot: default_units_id Description: 
--     * Slot: owned_by_id Description: 
--     * Slot: variant_of_id Description: 
--     * Slot: db_instance Description: 
-- # Class: "Strain" Description: ""
--     * Slot: id Description: 
--     * Slot: object_ref_id Description: 
--     * Slot: registry_id Description: 
--     * Slot: registry_url Description: 
--     * Slot: db_instance Description: 
-- # Class: "MeasurementType_alt_names" Description: ""
--     * Slot: MeasurementType_uid Description: Autocreated FK slot
--     * Slot: alt_names Description: 
-- # Class: "Metabolite_tags" Description: ""
--     * Slot: Metabolite_id Description: Autocreated FK slot
--     * Slot: tags Description: 
-- # Class: "Metabolite_id_map" Description: ""
--     * Slot: Metabolite_id Description: Autocreated FK slot
--     * Slot: id_map Description: 
-- # Class: "ProteinIdentifier_accession_id" Description: ""
--     * Slot: ProteinIdentifier_id Description: Autocreated FK slot
--     * Slot: accession_id Description: 
-- # Class: "ProteinIdentifier_mass" Description: ""
--     * Slot: ProteinIdentifier_id Description: Autocreated FK slot
--     * Slot: mass Description: 

CREATE TABLE gene_identifier (
	id INTEGER NOT NULL, 
	measurementtype_ptr_id INTEGER, 
	gene_length TEXT, 
	db_instance VARCHAR(29), 
	PRIMARY KEY (id), 
	UNIQUE (gene_length)
);
CREATE TABLE "MeasurementType" (
	uid INTEGER NOT NULL, 
	id INTEGER, 
	type_name TEXT, 
	short_name TEXT, 
	type_group VARCHAR(1), 
	uuid TEXT, 
	type_source_id TEXT, 
	provisional VARCHAR(1), 
	db_instance VARCHAR(29), 
	PRIMARY KEY (uid)
);
CREATE TABLE "MeasurementUnit" (
	uid INTEGER NOT NULL, 
	id INTEGER, 
	unit_name VARCHAR(24), 
	display VARCHAR(1), 
	alternate_names VARCHAR(12), 
	type_group VARCHAR(1), 
	db_instance VARCHAR(29), 
	PRIMARY KEY (uid)
);
CREATE TABLE "Metabolite" (
	id INTEGER NOT NULL, 
	measurementtype_ptr_id INTEGER, 
	charge INTEGER, 
	carbon_count INTEGER, 
	molar_mass FLOAT, 
	molecular_formula TEXT, 
	smiles TEXT, 
	pubchem_cid INTEGER, 
	db_instance VARCHAR(29), 
	PRIMARY KEY (id)
);
CREATE TABLE "MetadataType" (
	uid INTEGER NOT NULL, 
	id INTEGER, 
	type_name TEXT, 
	type_i18n TEXT, 
	type_field VARCHAR(13), 
	input_type VARCHAR(13), 
	default_value VARCHAR(21), 
	prefix VARCHAR(1), 
	postfix TEXT, 
	for_context VARCHAR(13), 
	uuid TEXT, 
	group_id TEXT, 
	db_instance VARCHAR(29), 
	PRIMARY KEY (uid)
);
CREATE TABLE "ProteinIdentifier" (
	id INTEGER NOT NULL, 
	measurementtype_ptr_id INTEGER, 
	length FLOAT, 
	accession_code TEXT, 
	db_instance VARCHAR(29), 
	PRIMARY KEY (id)
);
CREATE TABLE "ProteinStrain" (
	uid INTEGER NOT NULL, 
	id INTEGER, 
	protein_id INTEGER, 
	strain_id INTEGER, 
	db_instance VARCHAR(29), 
	PRIMARY KEY (uid), 
	UNIQUE (protein_id), 
	UNIQUE (strain_id)
);
CREATE TABLE "Protocol" (
	id INTEGER NOT NULL, 
	object_ref_id INTEGER, 
	categorization VARCHAR(7), 
	default_units_id INTEGER, 
	owned_by_id INTEGER, 
	variant_of_id VARCHAR(7), 
	db_instance VARCHAR(29), 
	PRIMARY KEY (id)
);
CREATE TABLE "Strain" (
	id INTEGER NOT NULL, 
	object_ref_id INTEGER, 
	registry_id TEXT, 
	registry_url TEXT, 
	db_instance VARCHAR(29), 
	PRIMARY KEY (id)
);
CREATE TABLE "MeasurementType_alt_names" (
	"MeasurementType_uid" INTEGER, 
	alt_names TEXT, 
	PRIMARY KEY ("MeasurementType_uid", alt_names), 
	FOREIGN KEY("MeasurementType_uid") REFERENCES "MeasurementType" (uid)
);
CREATE TABLE "Metabolite_tags" (
	"Metabolite_id" INTEGER, 
	tags VARCHAR(18), 
	PRIMARY KEY ("Metabolite_id", tags), 
	FOREIGN KEY("Metabolite_id") REFERENCES "Metabolite" (id)
);
CREATE TABLE "Metabolite_id_map" (
	"Metabolite_id" INTEGER, 
	id_map TEXT, 
	PRIMARY KEY ("Metabolite_id", id_map), 
	FOREIGN KEY("Metabolite_id") REFERENCES "Metabolite" (id)
);
CREATE TABLE "ProteinIdentifier_accession_id" (
	"ProteinIdentifier_id" INTEGER, 
	accession_id TEXT, 
	PRIMARY KEY ("ProteinIdentifier_id", accession_id), 
	FOREIGN KEY("ProteinIdentifier_id") REFERENCES "ProteinIdentifier" (id)
);
CREATE TABLE "ProteinIdentifier_mass" (
	"ProteinIdentifier_id" INTEGER, 
	mass TEXT, 
	PRIMARY KEY ("ProteinIdentifier_id", mass), 
	FOREIGN KEY("ProteinIdentifier_id") REFERENCES "ProteinIdentifier" (id)
);