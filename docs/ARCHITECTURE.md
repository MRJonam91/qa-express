# Struttura / Structure

IT — `site/` contiene una pagina statica senza dipendenze. `examples/` e `templates/` contengono materiali testuali illustrativi. `scripts/check_public.py` verifica collegamenti locali e vincoli di pubblicazione; non esegue un audit cliente. La CI ripete questa verifica. Il repository non raccoglie dati e non ha backend. Per estendere i modelli mantenere scope, stato delle evidenze e IT/EN coerenti.

EN — `site/` is dependency-free static HTML. `examples/` and `templates/` contain illustrative text materials. The checker validates local references and publication boundaries, not customer sites. CI repeats it. No data collection or backend is included. Keep scope, evidence status and languages consistent when extending materials.
