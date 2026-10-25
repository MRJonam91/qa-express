# Report QA Express — ESEMPIO ILLUSTRATIVO / FICTIONAL SAMPLE

**Non è un audit eseguito. Non esistono cliente, misurazioni o allegati riferiti a questo esempio.** Gli scenari spiegano la struttura della consegna. / **This is not an executed audit. No customer, measurements or evidence attachments exist for this sample.**

## Copertura / Coverage

In un incarico reale indicare data, versione/commit, URL autorizzato, browser e versione effettiva, dispositivo reale o viewport, dati di prova, azioni consentite e pagine percorse. Non elencare ambienti non provati. / Record the actual date, version, authorized URL, browser, real device or viewport, test data, permitted actions and tested pages.

## Scenario dimostrativo QA-01: controllo coperto su mobile

| Campo / Field | Esempio ipotetico / Hypothetical example |
|---|---|
| Flusso / Flow | Checkout di test, prima di qualunque pagamento reale / Test checkout before any real payment |
| Ambiente / Environment | Da registrare durante il test / Record during the test |
| Passi / Steps | Aprire il carrello di test, procedere al checkout, aprire il banner cookie / Open the test cart, proceed to checkout, open the cookie banner |
| Atteso / Expected | Pulsante principale raggiungibile e utilizzabile / Main action remains reachable and usable |
| Osservato / Observed | In questo scenario inventato il banner copre il pulsante / In this fictional scenario the banner covers the button |
| Evidenza / Evidence | Non presente: nessuno screenshot o video è stato acquisito / None; no screenshot or video was captured |
| Priorità / Priority | Da confermare con il cliente in base a frequenza, percorso alternativo e impatto / Confirm based on frequency, workaround and impact |
| Suggerimento / Suggestion | Esaminare layout, spaziatura e gestione degli elementi fissi; verificare il fix / Inspect layout, spacing and fixed elements, then retest |

## Scenario dimostrativo QA-02: errore del form poco chiaro

Passi ipotetici: compilare il form di test con un numero telefonico contenente spazi; inviare usando dati sintetici. Atteso: dati accettati o messaggio comprensibile associato al campo. Osservato ipotetico: invio fallito senza indicazione visibile. Evidenza: assente. Stato: esempio, non difetto osservato.

Hypothetical steps: submit a test form with a spaced phone number using synthetic data. Expected: acceptance or a clear field-level error. Fictional observation: failed submission without visible explanation. Evidence: none. Status: illustrative, not an observed defect.

## Accessibilità e limiti / Accessibility and limitations

In un audit reale separare controlli automatici, ispezione DOM e verifiche manuali; indicare strumenti effettivamente eseguiti. La presenza di una label non prova l'accessibilità di un flusso. Questi materiali non certificano conformità WCAG, EAA o altre norme. Nessun valore LCP, contrasto, perdita vendite o tempo di fix è stato misurato nell'esempio.

In real work, distinguish automated checks, DOM inspection and manual tests, naming only tools actually run. Labels alone do not establish flow accessibility. This sample certifies no legal or accessibility compliance and contains no measured performance, revenue impact or fix-time claims.

## Integrità / Integrity

Un eventuale file di checksum reale rileva cambiamenti dei byte rispetto a un riferimento fidato. Non dimostra autore, data certa, copertura o veridicità. Questo esempio non contiene hash o firme fittizie. / A real checksum detects changed bytes against a trusted reference. It does not establish authorship, trusted time, coverage or truth. No invented digest or signature is provided.
