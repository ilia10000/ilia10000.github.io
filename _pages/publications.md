---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

You can also find our articles on <u><a href="https://scholar.google.ca/citations?user=6MfHyuMAAAAJ&hl=en">Google Scholar</a>.</u>

{% include base_path %}

<style>
.keyword-filters {
  margin: 1em 0 1.5em;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.keyword-btn {
  display: inline-block;
  padding: 0.4em 1em;
  border: 1px solid #999;
  border-radius: 20px;
  background: transparent;
  color: #333;
  font-size: 0.9em;
  cursor: pointer;
  transition: background-color 0.2s, color 0.2s;
}
.keyword-btn:hover {
  background-color: rgba(128,128,128,0.3);
}
.keyword-btn.active {
  background-color: #333;
  color: #fff;
  border-color: #333;
}
.pub-year-heading.hidden, .pub-entry.hidden {
  display: none;
}
</style>

{% assign sorted_pubs = site.publications | sort: 'date' | reverse %}

{% comment %} Collect all keywords {% endcomment %}
{% assign all_keywords = "" %}
{% for post in sorted_pubs %}
  {% if post.keywords %}
    {% for kw in post.keywords %}
      {% assign all_keywords = all_keywords | append: kw | append: "," %}
    {% endfor %}
  {% endif %}
{% endfor %}
{% assign keyword_array = all_keywords | split: "," | uniq | sort %}

<div class="keyword-filters" id="keyword-filters">
  <button class="keyword-btn active" data-keyword="all">All Topics</button>
  {% for kw in keyword_array %}
    {% if kw != "" %}
      <button class="keyword-btn" data-keyword="{{ kw }}">{{ kw }}</button>
    {% endif %}
  {% endfor %}
</div>

{% assign current_year = "" %}

{% for post in sorted_pubs %}
  {% assign pub_year = post.date | date: "%Y" %}
  {% if pub_year != current_year %}
    {% assign current_year = pub_year %}
<h2 class="pub-year-heading" data-year="{{ current_year }}">{{ current_year }}</h2>
  {% endif %}

  <p class="pub-entry" data-keywords="{% if post.keywords %}{{ post.keywords | join: ',' }}{% endif %}" data-year="{{ pub_year }}">
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
    {% if post.keywords %}
      <br/><span style="font-size: 0.8em; color: #777;">{% for kw in post.keywords %}<span style="background: #eee; padding: 2px 6px; border-radius: 10px; margin-right: 4px;">{{ kw }}</span>{% endfor %}</span>
    {% endif %}
  </p>
{% endfor %}

<script>
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('keyword-filters').addEventListener('click', function(e) {
    var btn = e.target;
    if (!btn.classList.contains('keyword-btn')) return;

    var keyword = btn.getAttribute('data-keyword');

    // Update active button
    document.querySelectorAll('.keyword-btn').forEach(function(b) {
      b.classList.remove('active');
    });
    btn.classList.add('active');

    // Filter publications
    document.querySelectorAll('.pub-entry').forEach(function(entry) {
      if (keyword === 'all') {
        entry.classList.remove('hidden');
      } else {
        var kws = entry.getAttribute('data-keywords');
        if (kws && kws.split(',').indexOf(keyword) !== -1) {
          entry.classList.remove('hidden');
        } else {
          entry.classList.add('hidden');
        }
      }
    });

    // Show/hide year headings
    document.querySelectorAll('.pub-year-heading').forEach(function(heading) {
      var year = heading.getAttribute('data-year');
      var hasVisible = false;
      document.querySelectorAll('.pub-entry[data-year="' + year + '"]').forEach(function(entry) {
        if (!entry.classList.contains('hidden')) {
          hasVisible = true;
        }
      });
      heading.classList.toggle('hidden', !hasVisible);
    });
  });
});
</script>
