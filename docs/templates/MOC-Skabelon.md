---
id: <% tp.date.now("YYYYMMDDHHmm") %>
title: "MOC: <% tp.file.title %>"
type: moc
tags:
  - atlas
---

# 🗺️ <% tp.file.title %> MOC

## 📍 Kurateret Indhold
*Her skriver du manuelt dine vigtigste sammenhænge...*

- 

---

## 🤖 Uklassificerede noter (Dataview)
*Disse noter mangler at blive flettet ind i oversigten ovenfor.*

```dataview
LIST
FROM "docs"
WHERE contains(tags, "target-tag-her") 
AND !contains(file.name, "MOC")
SORT created desc
```