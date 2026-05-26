#!/usr/bin/env python3
"""
One-off retagger for the publications collection.
Replaces the legacy 7-tag taxonomy (which lumped most things under
"Large Language Models" and "Cognitive Science") with a thrust-aligned
8-tag system, and rewrites the `keywords:` front-matter field on every
_publications/*.md file.

Tag taxonomy:
    AI Thought Partners       — the framework paper, AITP-meta papers
    Representational Alignment — Thrust 1
    LO-shot Learning           — Thrust 2 (incl. dataset distillation, FSL)
    Cognitive Science of AI    — Thrust 3 (psych paradigms applied to AI)
    Collective Intelligence    — Thrust 4 (multi-agent, Rogers' paradox, teams)
    AI Safety & Trust          — Thrust 5
    Education                  — Thrust 6 sub-domain
    Robotics                   — Thrust 6 sub-domain

Some early/applied papers outside the lab's current scope get no tags.
"""
import re
from pathlib import Path

PUBS_DIR = Path(__file__).resolve().parent.parent / "_publications"

# Map: filename substring -> list of tags
TAGS = {
    # ---------- 2026 ----------
    "Language-Model-Teams-as-Distributed-Systems":          ["Collective Intelligence", "AI Thought Partners"],
    "Under-the-Influence":                                  ["AI Safety & Trust", "AI Thought Partners"],
    "Why-Human-Guidance-Matters":                           ["AI Thought Partners", "Collective Intelligence"],
    "Human-AI-Synergy-Supports-Collective-Creative-Search": ["AI Thought Partners", "Collective Intelligence"],

    # ---------- 2025 ----------
    "AI-Impact-on-Human-Proof-Formalization-Workflows":     ["Education", "AI Thought Partners"],
    "Explicitly-unbiased-large-language-models":            ["Cognitive Science of AI", "AI Safety & Trust"],
    "Learning-a-Doubly-Exponential-Number":                 ["LO-shot Learning"],
    "Large-language-models-surpass-human-experts":          ["Cognitive Science of AI"],
    "Using-LLMs-to-advance-the-cognitive-science-of-collectives": ["Collective Intelligence", "Cognitive Science of AI"],
    "Representational-Alignment-Supports-Effective-Teaching":     ["Representational Alignment", "Education"],
    "Characterizing-the-LargeScale-Structure-of-Multimodal":      ["Cognitive Science of AI"],
    "Measuring-and-mitigating-overreliance":                ["AI Safety & Trust", "AI Thought Partners"],
    "Identifying-Evaluating-and-Mitigating-Risks-of-AI-Thought":  ["AI Thought Partners", "AI Safety & Trust"],
    "When-should-we-orchestrate-multiple-agents":           ["Collective Intelligence", "AI Thought Partners"],
    "On-benchmarking-human-like-intelligence-in-machines":  ["Cognitive Science of AI"],
    "What-is-a-Number-That-a-Large-Language-Model":         ["Cognitive Science of AI"],
    "Humanitys-last-exam":                                  ["Cognitive Science of AI"],
    "Revisiting-Rogers-Paradox":                            ["Collective Intelligence", "AI Thought Partners"],
    "Using-the-tools-of-cognitive-science-to-understand-large-language-models": ["Cognitive Science of AI"],

    # ---------- 2024 ----------
    "Studying-the-Effect-of-Globalization-on-Color-Perception":   ["Cognitive Science of AI"],
    # Sensory judgments six modalities (Marjieh)
    "predict-human-sensory-judgments":                      ["Cognitive Science of AI"],
    # GPT for multilingual psychology
    "GPT-is-an-effective-tool":                             ["Cognitive Science of AI"],
    "Using-compositionality-to-learn-many-categories":      ["LO-shot Learning"],
    "Pushing-the-Limits-of-Learning-from-Limited-Data":     ["LO-shot Learning"],
    "conversational-tones":                                 ["Cognitive Science of AI"],
    "Preference-conditioned-language-guided-abstraction":   ["Robotics"],
    # exKidneyBERT — applied medical, outside current thrusts
    "exKidneyBERT":                                         [],
    "Learning-human-like-representations-to-enable-learning-human-values": ["Representational Alignment", "AI Safety & Trust"],
    "First-Workshop-on-Representational-Alignment":         ["Representational Alignment"],
    "Dimensions-of-disagreement":                           ["AI Thought Partners", "Cognitive Science of AI"],
    "Grounded-Semantic-Networks":                           ["Cognitive Science of AI"],
    "Building-machines-that-learn-and-think-with-people":   ["AI Thought Partners"],
    "Quantifying-knowledge-distillation":                   ["LO-shot Learning"],
    "Mind-your-step":                                       ["Cognitive Science of AI"],
    "Adaptive-language-guided-abstraction":                 ["Robotics"],
    "Multilevel-interpretability":                          ["Representational Alignment"],
    "Modulating-language-model-experiences-through-frictions": ["AI Safety & Trust", "AI Thought Partners"],
    "Towards-formalizing-spuriousness":                     ["LO-shot Learning", "AI Safety & Trust"],
    "assume-people-are-more-rational":                      ["Cognitive Science of AI"],
    "Analyzing-the-roles-of-language-and-vision":           ["LO-shot Learning"],
    "Learning-with-language-guided-state-abstractions":     ["Robotics"],
    "speech-to-song-illusion":                              ["Cognitive Science of AI"],
    "2024-01-01-Concept-alignment":                         ["Representational Alignment"],
    "Quantifying-spuriousness-of-biased-datasets":          ["LO-shot Learning", "AI Safety & Trust"],
    "Why-should-we-care-if-machines-learn-human-like":      ["Representational Alignment"],

    # ---------- 2023 ----------
    "On-the-informativeness-of-supervision-signals":        ["Representational Alignment", "LO-shot Learning"],
    "What-language-reveals-about-perception":               ["Cognitive Science of AI"],
    "Large-language-models-meet-cognitive-science":         ["Cognitive Science of AI"],
    "Introducing-deep-learning":                            [],
    "Human-uncertainty-in-concept-based-ai-systems":        ["AI Thought Partners", "AI Safety & Trust"],
    "End-to-End-Learnable-Masks":                           [],
    "Concept-alignment-as-a-prerequisite-for-value-alignment": ["Representational Alignment", "AI Safety & Trust"],
    "Getting-aligned-on-representational-alignment":        ["Representational Alignment"],
    "Around-the-world-in-60-words":                         ["Cognitive Science of AI"],
    "Alignment-with-human-representations-supports-robust-few-shot": ["Representational Alignment", "LO-shot Learning"],

    # ---------- 2022 ----------
    "Human-in-the-Loop-Mixup":                              ["AI Thought Partners"],
    "Playing-the-Lottery-of-a-Lifetime":                    ["Collective Intelligence"],
    "Analyzing-diffusion-as-serial-reproduction":           ["Cognitive Science of AI"],
    "Words-are-all-you-need":                               ["Cognitive Science of AI"],
    "Predicting-human-similarity-judgments-using-large-language-models": ["Cognitive Science of AI"],
    "Can-humans-do-less-than-one-shot":                     ["LO-shot Learning"],

    # ---------- 2021 ----------
    "Secdd":                                                [],
    "Less-Than-One-Shot-Learning":                          ["LO-shot Learning"],
    "Optimal-1-NN-prototypes":                              ["LO-shot Learning"],
    "Learning-From-Almost-No-Data":                         ["LO-shot Learning"],
    "One-Line-To-Rule-Them-All":                            ["LO-shot Learning"],

    # ---------- 2019 ----------
    "Pay-attention-and-you-wont-lose-it":                   [],
    "Soft-Label-Dataset-Distillation":                      ["LO-shot Learning"],
    "Deep-Learning-for-System-Trace-Restoration":           [],

    # ---------- 2018 ----------
    "ConvART":                                              [],

    # ---------- 2017 ----------
    "Text-mining-with-n-gram-variables":                    [],
}


def find_tags_for(filename: str):
    for key, tags in TAGS.items():
        if key.lower() in filename.lower():
            return tags
    return None


def rewrite_keywords(path: Path, tags):
    text = path.read_text(encoding="utf-8")
    formatted = (
        "[" + ", ".join(f'"{t}"' for t in tags) + "]"
        if tags else "[]"
    )
    new_line = f"keywords: {formatted}"
    if re.search(r"^keywords:.*$", text, re.MULTILINE):
        new = re.sub(r"^keywords:.*$", new_line, text, count=1, flags=re.MULTILINE)
    else:
        # Inject before the closing --- of front matter
        new = re.sub(
            r"(\n---\s*\n)",
            f"\n{new_line}\\1",
            text,
            count=1,
        )
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    matched, unmatched = [], []
    for path in sorted(PUBS_DIR.glob("*.md")):
        tags = find_tags_for(path.name)
        if tags is None:
            unmatched.append(path.name)
            continue
        changed = rewrite_keywords(path, tags)
        matched.append((path.name, tags, changed))
    print(f"Matched {len(matched)} files; rewrote {sum(1 for _,_,c in matched if c)}.")
    if unmatched:
        print(f"\nUnmatched ({len(unmatched)}):")
        for n in unmatched:
            print(" ", n)


if __name__ == "__main__":
    main()
