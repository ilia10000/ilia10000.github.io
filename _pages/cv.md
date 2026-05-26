---
layout: archive
title: "CV"
permalink: /cv/
author_profile: false
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25em;
  margin: 1.2em 0 2em 0;
}
@media (max-width: 720px) { .cv-cards { grid-template-columns: 1fr; } }
.cv-card {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-left: 4px solid #c0392b;
  border-radius: 6px;
  padding: 1.1em 1.3em;
}
.cv-card h3 {
  font-family: Georgia, serif;
  font-size: 1.1em;
  font-weight: 700;
  margin: 0 0 0.4em 0;
  color: #1a1a1a;
}
.cv-card p { margin: 0 0 0.4em 0; line-height: 1.55; color: #2a2d34; }
.cv-card a { color: #c0392b; border-bottom: 1px solid rgba(192,57,43,0.25); text-decoration: none; }
.cv-card a:hover { border-bottom-color: #c0392b; }
.cv-quicklinks {
  list-style: none !important;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
}
.cv-quicklinks li { margin: 0; list-style: none !important; }
.cv-quicklinks a {
  display: inline-flex;
  padding: 0.45em 0.95em;
  background: #f6f7fb;
  border: 1px solid #e5e7eb !important;
  border-radius: 999px;
  font-size: 0.9em;
  font-weight: 600;
  color: #1a1a1a !important;
  text-decoration: none !important;
}
.cv-quicklinks a:hover {
  background: #fff;
  border-color: rgba(192,57,43,0.45) !important;
  color: #c0392b !important;
}
</style>

<div class="cv-cards">
  <div class="cv-card">
    <h3>Live CV (always current)</h3>
    <p>Maintained as a Google Doc. Sections include positions, peer-reviewed publications, preprints, invited talks, grants, awards, teaching, and service.</p>
    <p><a href="https://docs.google.com/document/d/1zidrssc8bdr2Rw2tS6rxzxumWVZ_axb8DPbh7cu65aQ/edit?usp=sharing">Open the live CV →</a></p>
  </div>
  <div class="cv-card">
    <h3>PDF snapshot</h3>
    <p>For sharing or printing. May lag the Google Doc by a few weeks.</p>
    <p><a href="{{ base_path }}/files/Sucholutsky_CV.pdf">Download the PDF →</a></p>
  </div>
</div>

**Looking for something shorter?**

<ul class="cv-quicklinks">
  <li><a href="{{ base_path }}/research/">Six research thrusts</a></li>
  <li><a href="{{ base_path }}/publications/">All publications</a></li>
  <li><a href="https://scholar.google.ca/citations?user=6MfHyuMAAAAJ&hl=en">Google Scholar</a></li>
  <li><a href="{{ base_path }}/people/">People in the lab</a></li>
  <li><a href="{{ base_path }}/contact/">How to reach the lab</a></li>
</ul>
