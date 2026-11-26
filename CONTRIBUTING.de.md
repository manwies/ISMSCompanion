# Mitwirken an ISMSCompanion

Vielen Dank für dein Interesse an ISMSCompanion. Dieses Dokument erklärt, wie du helfen kannst und wie das Projekt mit Beiträgen umgeht.

_English version: [CONTRIBUTING.md](CONTRIBUTING.md). Bei Abweichungen gilt die englische Fassung._

## Aktuelle Regel: keine externen Code-Beiträge

ISMSCompanion wird derzeit von einem einzelnen Maintainer entwickelt. Das Projekt **nimmt vorerst keine externen Code-Beiträge an**. Das gilt für Pull Requests, Patches und Code-Schnipsel. Pull Requests von Dritten werden ohne Merge geschlossen, unabhängig von ihrer Qualität. Bitte nimm das nicht persönlich.

Der Grund ist praktisch: Der Maintainer möchte alle Rechte am Code in einer Hand behalten. So bleibt das Projekt unter der Lizenz `AGPL-3.0-only` verfügbar und kann später zusätzlich zu anderen Bedingungen angeboten werden. Externer Code würde das erheblich erschweren. Sollte sich diese Regel ändern, wird das hier und in der README bekannt gegeben.

## So kannst du trotzdem helfen

Dein Input ist in diesen Formen willkommen:

- **Fehlerberichte**: Eröffne ein Issue und beschreibe, was du erwartet hast, was passiert ist und wie man es nachstellen kann.
- **Ideen und Funktionswünsche**: Eröffne ein Issue und beschreibe das Problem, das du lösen möchtest. Ideen gelten nur als Anregungen. Der Maintainer entscheidet eigenständig, ob und wie er sie umsetzt.
- **Fragen und Feedback**: Nutze den Issue Tracker oder die Discussions.
- **Sicherheitsmeldungen**: Bitte keine öffentlichen Issues. Folge der [.github/SECURITY.md](.github/SECURITY.md).

Bitte beschreibe das Problem in Worten, wenn du ein Issue schreibst. Bitte füge keinen eigenen Quellcode und keine Patches ein, weil das Projekt sie nicht übernehmen kann (siehe nächster Abschnitt).

## Code und Rechte in Issues

- Poste keinen Code, den du selbst geschrieben hast und der im Projekt verwendet werden soll.
- Kurze Zitate aus dem bestehenden Code dieses Repositorys, Fehlermeldungen und Log-Ausgaben sind in Ordnung.
- Poste keinen Code aus anderen Projekten, besonders nicht unter einer Lizenz, die mit `AGPL-3.0-only` nicht kompatibel ist.
- Ideen und Vorschläge in Issues gelten nicht als Code-Beiträge. Der Maintainer setzt sie eigenständig um.

## Bots

Bots für Dependency-Updates wie Renovate können Pull Requests öffnen, die Versionen oder Pins von Abhängigkeiten ändern. Diese werden vom Maintainer geprüft und gemergt.

## KI-gestützte Entwicklung

Teile des Projekts werden mit KI-Unterstützung entwickelt. Der gesamte KI-generierte Code wird vom Maintainer geprüft, getestet und angepasst. Siehe den Hinweis in der [README](README.de.md).

## Interner Workflow (für den Maintainer)

Dieser Abschnitt dokumentiert, wie Änderungen entstehen, damit der Ablauf transparent ist.

- **Branches**: ein Branch pro Aufgabe vom aktuellen `main`, benannt `feature|fix|sec|docs|chore|test/<kurzname>`.
- **Commits**: atomare Commits im Format [Conventional Commits](https://www.conventionalcommits.org/), auf Englisch.
- **Pull Requests**: ein Thema pro Pull Request, mit dem Pull-Request-Template. Gemergt wird ausschließlich per **Squash Merge** in der GitHub-Weboberfläche, damit der Commit auf `main` signiert ist. Siehe `docs/security/merge-policy.md`.
- **Versionierung**: SemVer. Die Version wird als letzter Commit eines geprüften Pull Requests angehoben. Reine Änderungen an Doku, Tests, Chores und CI ohne Auswirkung auf ausgeliefertes Verhalten brauchen keinen Bump.
- **Lokales Setup**: `pip install -e ".[dev]"`, danach die Pre-commit-Hooks aktivieren.

### Definition of Done

- Lint-, Format- und Typing-Prüfungen laufen sauber.
- Für neue Logik gibt es Tests, auch für Security- und Fehlerpfade.
- Keine Secrets und keine personenbezogenen Daten im Repository.
- Neue Dependencies sind begründet, gepinnt und auf Lizenz und bekannte Schwachstellen geprüft.
- Dokumentation und `CHANGELOG.md` sind aktualisiert.
- UI-Texte nur über i18n (Deutsch und Englisch).
- Code-Kommentare sind auf Englisch.

## Lizenz

Das Projekt steht unter der `AGPL-3.0-only`. Siehe [LICENSE](LICENSE).

## Fragen

Wenn in diesem Dokument etwas unklar ist, eröffne bitte ein Issue. Danke für dein Verständnis und dein Interesse am Projekt.
