tsvs:
	./util/pgdump2tsv.pl data/metadata_plus.*sql

#INC = --enum-columns type_name
INC =
auto.yaml:
	poetry run schemauto generalize-tsvs  -n edd  $(INC) --max-enum-size 100 --enum-threshold 0.6 tmp/*.tsv > $@
#	pipenv run ../linkml-model-enrichment/linkml_model_enrichment/infer_model.py tsvs2model -n edd  $(INC) --enum-mask-columns id --enum-mask-columns uuid --max-enum-size 500 --enum-threshold 0.6 tmp/*.tsv > $@

