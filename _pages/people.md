---
permalink: /people/
title: "People"
excerpt: "AITP Lab members"
author_profile: false
redirect_from:
  - /students/
---

<style>
.page__content .archive {
  width: 100%;
  float: none;
}
.person-pi {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 30px;
}
.person-pi img {
  width: 175px;
  height: 175px;
  object-fit: cover;
  border-radius: 50%;
  padding: 5px;
  border: 1px solid #e0e0e0;
  flex-shrink: 0;
}
.people-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  margin-bottom: 40px;
  min-width: 0;
}
.person-card {
  text-align: center;
}
.person-card img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
  padding: 4px;
  border: 1px solid #e0e0e0;
  margin-bottom: 10px;
}
.person-card .name-btn {
  display: inline-block;
  padding: 0.4em 1em;
  border: 1px solid #999;
  border-radius: 20px;
  background: transparent;
  color: #333;
  font-size: 1em;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.2s, color 0.2s;
  margin-bottom: 6px;
}
.person-card .name-btn:hover {
  background-color: rgba(128,128,128,0.3);
}
.person-card .name-btn.active {
  background-color: #333;
  color: #fff;
  border-color: #333;
}
.person-card .role {
  font-size: 0.9em;
  color: #555;
  margin-bottom: 4px;
}
.person-card .keywords {
  font-size: 0.85em;
  color: #777;
  margin-bottom: 4px;
}
.person-card .fun-fact {
  font-size: 0.85em;
  margin-bottom: 4px;
}
.person-card .website-link {
  font-size: 0.85em;
  margin-bottom: 6px;
}
.person-card .info {
  font-size: 0.9em;
  text-align: left;
  line-height: 1.6;
  display: none;
  margin-top: 8px;
}
.person-card .info.open {
  display: block;
}
@media (max-width: 768px) {
  .people-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

{% assign people = site.data.people %}

## Principal Investigator

<div class="person-pi">
  <img src="{{ people.pi.image }}" alt="{{ people.pi.name }}" />
  <div>
    <strong>{{ people.pi.name }}</strong><br/>
    {{ people.pi.bio }}<br/><br/>
    {% if people.pi.links.google_scholar %}<a href="{{ people.pi.links.google_scholar }}"><i class="fas fa-graduation-cap"></i> Google Scholar</a> &nbsp;{% endif %}
    {% if people.pi.links.github %}<a href="{{ people.pi.links.github }}"><i class="fab fa-github"></i> GitHub</a> &nbsp;{% endif %}
    {% if people.pi.links.linkedin %}<a href="{{ people.pi.links.linkedin }}"><i class="fab fa-linkedin"></i> LinkedIn</a> &nbsp;{% endif %}
    {% if people.pi.links.researchgate %}<a href="{{ people.pi.links.researchgate }}"><i class="fab fa-researchgate"></i> ResearchGate</a>{% endif %}
  </div>
</div>

{% assign sections = "current_members,visitors,collaborators,thought_pawrtners,alumni" | split: "," %}
{% assign section_titles = "Current Members,Visitors & Affiliates,Collaborating Labs,Thought Pawrtners,Alumni & Collaborator Network" | split: "," %}
{% assign global_index = 0 %}

{% for section in sections %}
  {% assign idx = forloop.index0 %}
  {% assign section_people = people.members | where: "section", section %}
## {{ section_titles[idx] }}

<div class="people-grid">
  {% for person in section_people %}
    {% if person.name != "" %}
    {% assign global_index = global_index | plus: 1 %}
    <div class="person-card">
      {% if person.image != "" and person.image != "/images/people/placeholder.png" %}<img src="{{ person.image }}" alt="{{ person.name }}" />{% else %}<img src="/images/people/placeholder.png" alt="{{ person.name }}" />{% endif %}
      <button class="name-btn" data-target="person-info-{{ global_index }}">{{ person.name }}</button>
      {% if person.role != "" %}<div class="role">{{ person.role }}</div>{% endif %}
      {% if person.research_keywords.size > 0 %}<div class="keywords">{{ person.research_keywords | join: ", " }}</div>{% endif %}
      {% if person.fun_fact != "" %}<div class="fun-fact"><strong>Fun fact:</strong> {{ person.fun_fact }}</div>{% endif %}
      {% if person.website != "" %}<div class="website-link"><a href="{{ person.website }}" target="_blank">Website</a></div>{% endif %}
      <div class="info" id="person-info-{{ global_index }}">
        {{ person.bio }}
      </div>
    </div>
    {% endif %}
  {% endfor %}
</div>

{% endfor %}

<script>
function initPeopleBtns() { document.querySelectorAll('.name-btn').forEach(function(btn) { if (btn.dataset.initialized) return; btn.dataset.initialized = 'true'; btn.addEventListener('click', function() { var targetId = btn.getAttribute('data-target'); var details = document.getElementById(targetId); var isOpen = details.classList.contains('open'); document.querySelectorAll('.person-card .info.open').forEach(function(el) { el.classList.remove('open'); }); document.querySelectorAll('.name-btn.active').forEach(function(b) { b.classList.remove('active'); }); if (!isOpen) { details.classList.add('open'); btn.classList.add('active'); } }); }); } document.addEventListener('DOMContentLoaded', initPeopleBtns); document.addEventListener('turbo:load', initPeopleBtns);
</script>
