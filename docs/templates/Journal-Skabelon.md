---
id: <% tp.date.now("YYYYMMDD") %>0000
title: "Journal: <% tp.date.now("DD-MM-YYYY") %>"
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
type: journal
tags:
  - daily-log
---

# 📓 Journal: <% tp.date.now("DD. MMMM YYYY") %>

## 🧠 Dagens Tanker (Fleeting Notes)
> Brug `Ctrl + Shift + R` for at flytte en tanke til arkivet uden første linje som title.
> Brug `Ctrl + Alt + R` for at flytte en tanke til arkivet med første linje som titel.

- <% tp.file.cursor() %>

## 📅 Log & Hændelser
- 

## 🔗 Dagens Forbindelser
- **Nye Zettels i dag:**
```dataview
LIST title
FROM ""
WHERE created >= "<% tp.date.now('YYYY-MM-DD') %>" AND type = "zettel"
```
---
*Dagens citat: <% tp.web.daily_quote() %>*
