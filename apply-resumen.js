const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = content.indexOf(`body.bp-compact .section-note:not([role=status])`);
const e = content.indexOf(`body.bp-compact #kpis .energy-card .eyebrow {display:none!important;}`) + 69;

const CSS_SEARCH = content.substring(s, e);
const CSS_REPLACE = `body.bp-compact .section-note:not([role=status]):not(.form-error),body.bp-compact .safe-info,body.bp-compact .progress-note,body.bp-compact .chart-caption:not([role=status]),body.bp-compact .weekly-note,body.bp-compact .weekly-summary,body.bp-compact .brief-denominator,body.bp-compact .brief-actions,body.bp-compact .trend-summary,body.bp-compact .section-heading p,body.bp-compact .bp-muted:not([aria-live]),body.bp-compact .legend,body.bp-compact .micro-status,body.bp-compact .micro-split,body.bp-compact .calendar-legend,body.bp-compact .hevy-source,body.bp-compact .section-number,body.bp-compact .fat-method,body.bp-compact .estimate-toggle,body.bp-compact .day-context,body.bp-compact .notice:not(#storage-warning),body.bp-compact .week-brief .eyebrow,body.bp-compact .shake-preview details,body.bp-compact .ai-steps,body.bp-compact .bp-fast .tiny,body.bp-compact .micro-amount small,body.bp-compact .calendar-day>small,body.bp-compact .preset-card .subtext,body.bp-compact .brief-macro small,body.bp-compact .week-micro-card p,body.bp-compact .week-micro-card small,body.bp-compact .ratio-card small,body.bp-compact .meal-key small,body.bp-compact .fat-key small,body.bp-compact .week-column>em,body.bp-compact .trend-week>em,body.bp-compact .weekly-shortcuts,body.bp-compact #bp-fast>.row,body.bp-compact .bp-head h3,body.bp-compact .energy-card .subtext,body.bp-compact #view-micros>.card>.row.between:first-child,body.bp-compact .micro-toolbar>.tiny,body.bp-compact #kpis .energy-percent,body.bp-compact #kpis .progress-note,body.bp-compact #macro-progress-grid .macro-track,body.bp-compact #macro-progress-grid .micro-amount,body.bp-compact #macro-progress-grid .micro-percent,body.bp-compact #macro-donut-card,body.bp-compact #ratio-summary .rg-head>span,body.bp-compact #ratio-summary .rg-scale,body.bp-compact #ratio-summary .rg-ticks,body.bp-compact #coach-card,body.bp-compact .day-coach {display:none!important}
body.bp-compact .week-micro-card,body.bp-compact .ratio-card,body.bp-compact .total-card,body.bp-compact .brief-macro {min-height:0!important;padding:9px!important;gap:4px!important}
body.bp-compact #ratio-summary {display:flex!important;flex-direction:row!important;gap:4px!important;overflow-x:auto!important;}
body.bp-compact #ratio-summary .rg {flex:1!important;min-width:0!important;padding:4px!important;margin:0!important;}
body.bp-compact #ratio-summary .rg-head {justify-content:center!important;margin-bottom:0!important;}
body.bp-compact #ratio-summary .rg-chip {display:none!important;}
body.bp-compact #ratio-summary strong {font-size:13px!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important;text-align:center!important;}
body.bp-compact #macro-progress-grid {display:flex!important;flex-direction:row!important;}
body.bp-compact #macro-progress-grid .macro-card {flex:1!important;}
body.bp-compact #macro-progress-grid .ring-label {font-size:12px!important;}
body.bp-compact #kpis {display:flex!important;flex-direction:column!important;gap:8px!important;}
body.bp-compact #kpis .energy-card {flex-direction:row!important;align-items:center!important;justify-content:space-between!important;padding:8px 12px!important;}
body.bp-compact #kpis .energy-card .energy-track {display:none!important;}
body.bp-compact #kpis .energy-card>div:first-child {display:flex!important;align-items:center!important;gap:12px!important;}
body.bp-compact #kpis .energy-card .energy-amount strong {font-size:20px!important;}
body.bp-compact #kpis .energy-card .eyebrow {display:none!important;}`;

content = content.replace(CSS_SEARCH, CSS_REPLACE);
fs.writeFileSync('index.html', content);
console.log("Compact CSS applied");
