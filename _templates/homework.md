<%*
const folder = tp.file.folder(true); // путь от корня vault, напр. Study/Project Neoversity/tier2/generative-agentic-ai/homework/hw04
const tierMatch = folder.match(/tier(\d)\/([^/]+)/);
const tier = tierMatch ? tierMatch[1] : "";
const discipline = tierMatch ? tierMatch[2] : "";
const themeMatch = folder.match(/hw_?theme(\d+)|hw(\d+)/);
const topic = themeMatch ? (themeMatch[1] || themeMatch[2]) : "";

tR += `---
title: "${tp.file.title}"
tier: ${tier}
discipline: ${discipline}
topic: ${topic}
type: homework
status: in-progress
date: ${tp.date.now("YYYY-MM-DD")}
---

# ${tp.file.title}

## Умова

## Рішення

## Результат
`;
%>
