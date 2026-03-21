---
permalink: /people/
title: "People"
excerpt: "AITP Lab members"
author_profile: false
redirect_from:
  - /students/
---

<style>
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
.person-card .name {
  font-weight: 500;
  font-size: 1.05em;
  margin-bottom: 6px;
}
.person-card .name a {
  color: inherit;
  text-decoration: none;
}
.person-card .name a:hover {
  text-decoration: underline;
}
.person-card .info {
  font-size: 0.9em;
  text-align: left;
  line-height: 1.6;
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

{% assign sections = "current_members,collaborators,alumni,thought_pawrtners" | split: "," %}
{% assign section_titles = "Current Members,Collaborators,Alumni,Thought Pawrtners" | split: "," %}

{% for section in sections %}
  {% assign idx = forloop.index0 %}
  {% assign section_people = people.members | where: "section", section %}
## {{ section_titles[idx] }}

<div class="people-grid">
  {% for person in section_people %}
    {% if person.name != "" %}
    <div class="person-card">
      {% if person.image != "" and person.image != "/images/people/placeholder.png" %}<img src="{{ person.image }}" alt="{{ person.name }}" />{% else %}<img src="/images/people/placeholder.png" alt="{{ person.name }}" />{% endif %}
      <div class="name">{% if person.website != "" %}<a href="{{ person.website }}">{{ person.name }}</a>{% else %}{{ person.name }}{% endif %}</div>
      <div class="info">
        {% if person.role != "" %}<strong>Role:</strong> {{ person.role }}<br/>{% endif %}
        {% if person.bio != "" %}<strong>Bio:</strong> {{ person.bio }}<br/>{% endif %}
        {% if person.research_keywords.size > 0 %}<strong>Research:</strong> {{ person.research_keywords | join: ", " }}<br/>{% endif %}
        {% if person.fun_fact != "" %}<strong>Fun fact:</strong> {{ person.fun_fact }}{% endif %}
      </div>
    </div>
    {% endif %}
  {% endfor %}
</div>

{% endfor %}
