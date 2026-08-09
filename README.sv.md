# Projektplanering & journalföring — en Claude Skill

[English](./README.md) · **Svenska** · [فارسی](./README.fa.md)

[![check-links](https://github.com/mh-mansouri/Project-Planning-Journaling/actions/workflows/check-links.yml/badge.svg)](https://github.com/mh-mansouri/Project-Planning-Journaling/actions/workflows/check-links.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

![Project Planning & Journaling demo](assets/skill-demo-mockup.gif)

En skill för [Claude](https://claude.ai) som hjälper dig att avgränsa ett projekt
ordentligt innan någon kod skrivs, och sedan för en levande projektjournal över allt som
händer — en journal du enkelt kan plocka upp igen, oavsett hur långt in i projektet ni är.

Öppna en helt ny session några veckor senare, peka Claude mot `project-journal/README.md`,
så vet den exakt var arbetet ligger — utan att du behöver bläddra igenom gammal
chatthistorik.

Föredrar du en sida framför en chatt? [`index.sv.html`](./index.sv.html) är en statisk
översikt med samma installationslänkar — live på
[mh-mansouri.github.io/Project-Planning-Journaling/index.sv.html](https://mh-mansouri.github.io/Project-Planning-Journaling/index.sv.html),
eller öppna filen lokalt, ingen server behövs.

## Vad den gör

- **Projektintag** — innan koden rör vid något, frågar den om projekttyp, om ett Git-repo
  redan finns (och om inte, föreslår ett namn, synlighet och en licens), kortsiktiga mot
  långsiktiga mål, och om detta ska förbli publikt/öppen källkod eller senare kan bli en
  privat produkt.
- **Skapar en `project-journal/`-mapp** — separat från källkoden, med en instrumentpanel
  `README.md`, en `decisions/`-logg, riktiga kodexempel i `snippets/`, och valfria
  anteckningar per session.
- **Skriver en lättöverskådlig instrumentpanel** — enkelt språk, tabeller och
  Mermaid-diagram i stället för löptext, checklistor för varje milstolpe, hopfällbara
  sektioner för allt som är långt.
- **Håller sig själv uppdaterad** — efter varje meningsfullt steg, beslut, commit eller
  push uppdaterar den automatiskt färdplanen, beslutsloggen, git-historiken och nästa steg.
- **Erbjuder ett val av utvecklingsstil** — spec-first (planera helt i förväg),
  interactive/iterative (flexibelt, journalen fångar beslut i efterhand), eller en
  milstolpebaserad hybrid.
- **Gör en återkommande genomgång, inte bara händelsestyrda uppdateringar** — i den takt
  du väljer (vecka som standard): kontrollerar att alla länkar fortfarande fungerar, att
  inget beslut tyst har åsidosatts, att ingen punkt i färdplanen blivit liggande obemärkt,
  och att eventuella externa källor som citeras fortfarande är trovärdiga — inte bara
  fortfarande nåbara online.

## Installation

**Alternativ A — ett klick (enklast):**
Ladda ner [`project-planning-journaling.skill`](./project-planning-journaling.skill), öppna
den i Claude och klicka på **Save skill**. (Skill-sparande måste vara aktiverat för ditt
konto eller din organisation.)

**Alternativ B — från källmappen:**
Kopiera mappen [`project-planning-journaling/`](./project-planning-journaling) till din
skills-katalog.

**Alternativ C — vilken annan AI-chatt som helst (ChatGPT, Grok, Gemini, Copilot,
DeepSeek, ...):**
Kopiera [`universal-prompt.md`](./universal-prompt.md) till ditt första meddelande — ingen
installation, ingen filuppladdning, fungerar överallt.

## Använd den

Berätta bara för Claude att du startar (eller återupptar) ett projekt, till exempel:

> Jag startar ett nytt sidoprojekt — ett CLI-verktyg för att döpa om en hel mapp med
> bildfiler i ett svep. Låt oss planera det innan vi skriver något.

eller, på ett befintligt projekt:

> Skapa en projektjournal för allt vi har byggt hittills, och håll den uppdaterad från
> och med nu.

eller, för att återuppta:

> Öppna projektjournalen och berätta var vi var.

## Bra att veta

Skillen frågar redan från början om ett projekt ska förbli publikt/öppen källkod eller
senare kan grenas till en privat branch och utvecklas som en fristående produkt — men det
faktiska beslutet (och all juridisk/licensrelaterad uppföljning) är ditt att fatta. Skillen
dokumenterar det, den bestämmer det inte åt dig.

## Grundad i etablerad praxis

Stegen är inte påhittade ur tomma intet — de bygger på tio fritt tillgängliga källor
(architecture decision records, dokumentationsramverk, changelog- och commit-konventioner,
discovery-fas-metodik, Scrum) plus fem kommersiellt publicerade böcker/standarder som
citeras enbart för sina koncept. Fullständig lista, belägg för att varje källa faktiskt är
erkänd (inte bara den första sökträffen), och vilket steg var och en backar upp, i
[`references/research.md`](./project-planning-journaling/references/research.md).
Detta repo praktiserar sitt eget steg 6: två veckovisa GitHub Actions håller listan ärlig —
en kontrollerar om alla länkar på nytt, den andra öppnar ett påminnelseärende för
trovärdighetsgranskningen.

## Bidra

Förbättringar är välkomna — särskilt verkliga fall där journalformatet inte fungerade
eller intagsfrågorna missade något. Se [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licens

Utgiven under [MIT-licensen](./LICENSE) — fri att använda, dela och bygga vidare på.

En av de bifogade filerna kommer från tredje part: 2020 års Scrum Guide,
vidaredistribuerad under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
och omfattas inte av MIT-licensen. Fullständig attribution i [NOTICE.md](./NOTICE.md).
