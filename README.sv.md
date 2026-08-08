# Projektplanering & journalföring — en Claude Skill

[English](./README.md) · **Svenska** · [فارسی](./README.fa.md)

En skill för [Claude](https://claude.ai) som hjälper dig att avgränsa ett projekt ordentligt
innan någon kod skrivs, och sedan för en levande, återupptagbar dokumentationsjournal över
allt som händer medan projektet fortskrider.

Öppna en helt ny session några veckor senare, peka Claude mot `project-journal/README.md`,
så vet den exakt var ni är — utan att behöva bläddra igenom gammal chatthistorik.

Föredrar du en sida framför en chatt? [`index.html`](./index.html) är en statisk översikt
med samma installationslänkar — när GitHub Pages är påslaget (Settings → Pages → Deploy
from branch → `main` / `/root`) ligger den live på
`https://mh-mansouri.github.io/Project-Planning-Journaling/`, eller öppna filen lokalt,
ingen server behövs.

## Vad den gör

- **Projektintag** — innan koden rör vid något, frågar den om projekttyp, om ett Git-repo
  redan finns (och om inte, föreslår ett namn, synlighet och en licens), kortsiktiga mot
  långsiktiga mål, och om detta ska förbli publikt/öppen källkod eller senare kan bli en
  privat produkt.
- **Sätter upp en `project-journal/`-mapp** — separat från källkoden, med en
  instrumentpanel `README.md`, en `decisions/`-logg, riktiga kodexempel i `snippets/`, och
  valfria anteckningar per session.
- **Skriver en lättöverskådlig instrumentpanel** — enkelt språk, tabeller och
  Mermaid-diagram i stället för löptext, checklistor för varje milstolpe, hopfällbara
  sektioner för allt som är långt.
- **Håller sig själv uppdaterad** — efter varje meningsfullt steg, beslut, commit eller
  push uppdaterar den automatiskt färdplanen, beslutsloggen, git-historiken och nästa steg.
- **Erbjuder ett val av utvecklingsstil** — spec-first (planera helt i förväg),
  interactive/iterative (flexibelt, journalen fångar beslut i efterhand), eller en
  milstolpebaserad hybrid.

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

> Jag startar ett nytt sidoprojekt — ett CLI-verktyg för att byta namn på fotobatcher. Låt
> oss planera det innan vi skriver något.

eller, på ett befintligt projekt:

> Sätt upp en projektjournal för allt vi har byggt hittills, och håll den uppdaterad från
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
citeras enbart för sina koncept. Fullständig lista, och vilket steg var och en backar upp,
i [`references/research.md`](./project-planning-journaling/references/research.md).

## Bidra

Förbättringar är välkomna — särskilt verkliga fall där journalformatet inte fungerade
eller intagsfrågorna missade något. Se [CONTRIBUTING.md](./CONTRIBUTING.md).

## Licens

Utgiven under [MIT-licensen](./LICENSE) — fri att använda, dela och bygga vidare på.

En medföljande fil är tredje part: 2020 års Scrum Guide, vidaredistribuerad under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) och omfattas inte av
MIT-licensen. Fullständig attribution i [NOTICE.md](./NOTICE.md).
