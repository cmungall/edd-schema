tsvs:
	./util/pgdump2tsv.pl data/metadata_plus.*sql

auto.yaml:
	pipenv run ../linkml-model-enrichment/linkml_model_enrichment/infer_model.py tsvs2model -n edd --enum-mask-columns id --enum-mask-columns uuid --max-enum-size 500 --enum-threshold 0.4 tmp/*.tsv > $@

