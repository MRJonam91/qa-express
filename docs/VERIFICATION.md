# Verifica / Verification — 2026-10-25

## Eseguito / Executed

- `python scripts/check_public.py`: riferimenti locali e anchor, assenza form di raccolta, etichetta illustrativa e dimensione core; esito PASS. / Local references, anchors, no data-collection form, fictional label and core size passed.
- Smoke browser sulla landing locale, Chrome installato, viewport **1440×1000, 390×1000, 360×1000**: titolo e contenuto, nessun overflow orizzontale, console/pageerror senza errori, navigazione report e contatti, contatto mail e report HTTP 200. / Local Chrome smoke passed at all three viewports.
- Schermate reali acquisite e ispezione visiva della versione mobile; non incluse nella consegna commerciale come prove cliente. / Actual screenshots captured; mobile visually inspected. They are not customer audit evidence.
- Il primo controllo ha trovato una richiesta favicon 404; aggiunta un'icona vuota inline e ripetuto lo stesso controllo con esito positivo. / Initial favicon 404 corrected and the same smoke rerun successfully.

Browser plugin assente; Playwright disponibile usato con Chrome locale dopo il mancato avvio del Chromium incluso. / Browser plugin unavailable; used bundled Playwright with installed Chrome after the bundled Chromium failed to launch.

## Limiti / Limits

Non verificati Safari, Firefox, dispositivi fisici, screen reader, consegna email, accesso account LinkedIn o il risultato di un incarico cliente. Il mailto è stato verificato come collegamento; nessun messaggio inviato. Nessun audit WCAG/EAA completo o test di domanda. La CI controlla il pacchetto statico, non ripete il browser smoke.

Safari, Firefox, physical devices, screen readers, email delivery, LinkedIn login and customer delivery remain untested. Mailto was checked as a link without sending messages. No full accessibility or demand validation. CI checks static materials, not browser smoke.
