---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

You can also find our articles on <u><a href="https://scholar.google.ca/citations?user=6MfHyuMAAAAJ&hl=en">Google Scholar</a>.</u>

{% include base_path %}

{% assign sorted_pubs = site.publications | sort: 'date' | reverse %}
{% assign current_year = "" %}

{% for post in sorted_pubs %}
  {% assign pub_year = post.date | date: "%Y" %}
  {% if pub_year != current_year %}
    {% assign current_year = pub_year %}
<h2>{{ current_year }}</h2>
  {% endif %}

  <p>
    {% if post.paperurl %}
      <a href="{{ post.paperurl }}" target="_blank"><strong>{{ post.title }}</strong></a>
    {% else %}
      <strong>{{ post.title }}</strong>
    {% endif %}
    <br/>
    <span style="font-size: 0.9em;">{{ post.authors | replace: " and ", ", " }}</span>
    {% if post.venue and post.venue != "" %}
      <br/><em>{{ post.venue }}</em>
    {% endif %}
  </p>
{% endfor %}
