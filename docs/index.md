---
hide:
  - navigation
---

# 🗃️ Bartoghs Digitale Arkiv

Velkommen til mit personlige vidensarkiv. Dette website er bygget som en digital forlængelse af Niklas Luhmanns Zettelkasten-metode, optimeret til læsning på tværs af alle mine enheder – fra min **Samsung Galaxy Book4** til min mobil.

---

## 📇 Overblikket

```dataview
LIST title
FROM ""
WHERE type = "zettel"
AND !contains(file.path, "templates")
AND !contains(file.path, "journal")
SORT created desc
```

---
## 📂 Aktuelle Indgange

Her kan du dykke ned i de forskellige spor i arkivet:

* **[[202603311400-luhmann-systemet]]** – Grundprincipperne for min arbejdsmetode.
* **[[202603311405-css-design]]** – Dokumentation af websitets visuelle identitet og CSS.

---

## 🧠 Om systemet

Dette arkiv er opbygget af "atomare" noter. Det betyder, at hver note indeholder én specifik tanke eller idé. Ved at forbinde dem med interne links (Wiki-links), opstår der nye mønstre og indsigt over tid.

> "Uden skrivning kan man ikke tænke – i hvert fald ikke på en sofistikeret måde."
> — *Niklas Luhmann*

---
Sidst opdateret: *31. marts 2026* | System: *Python 3.14.3 & MkDocs-Material*
