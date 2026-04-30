"""One-time swap: move Experience section to BEFORE Heroes section in index.astro.

Heroes section currently appears first (after the countdown). The user wants
Experience first. Both sections are bg-navy, so we just swap them in source order.

Approach: locate the two section blocks (including their leading comment headers),
swap them, also renumber the leading comment headers ("2." and "3.").
"""
from pathlib import Path
import re

INDEX = Path(r"C:/Users/USER/countdown250/src/pages/index.astro")
text = INDEX.read_text(encoding="utf-8")

# Heroes block: from its 4-line comment header through its closing </section>
heroes_block_re = re.compile(
    r"(\n    <!-- =+ -->\n"
    r"    <!-- 2\. ALL-AMERICAN HERO LIFETIME ACHIEVEMENT AWARDS -->\n"
    r"    <!-- Premium patriotic section honoring extraordinary Americans\. -->\n"
    r"    <!-- Sits between countdown and All-Inclusive Experience\. -->\n"
    r"    <!-- =+ -->\n"
    r"    <section id=\"heroes\".*?\n"
    r"    </section>\n)",
    re.DOTALL,
)

# Experience block: from its 3-line comment header through its closing </section>
experience_block_re = re.compile(
    r"(\n    <!-- =+ -->\n"
    r"    <!-- 3\. ALL-INCLUSIVE EXPERIENCE -->\n"
    r"    <!-- =+ -->\n"
    r"    <section id=\"experience\".*?\n"
    r"    </section>\n)",
    re.DOTALL,
)

m_heroes = heroes_block_re.search(text)
m_experience = experience_block_re.search(text)

assert m_heroes,     "Heroes block not found"
assert m_experience, "Experience block not found"
assert m_heroes.start() < m_experience.start(), "Heroes should currently be before Experience"

heroes_block     = m_heroes.group(1)
experience_block = m_experience.group(1)

# Renumber the comment headers — Experience becomes "2.", Heroes becomes "3."
new_experience = experience_block.replace(
    "<!-- 3. ALL-INCLUSIVE EXPERIENCE -->",
    "<!-- 2. ALL-INCLUSIVE EXPERIENCE -->",
)
new_heroes = heroes_block.replace(
    "<!-- 2. ALL-AMERICAN HERO LIFETIME ACHIEVEMENT AWARDS -->",
    "<!-- 3. ALL-AMERICAN HERO LIFETIME ACHIEVEMENT AWARDS -->",
)

# Build new file: prefix (everything before Heroes) + new_experience + middle (between Heroes end and Experience start) + new_heroes + suffix (everything after Experience end)
prefix  = text[:m_heroes.start()]
middle  = text[m_heroes.end():m_experience.start()]
suffix  = text[m_experience.end():]

new_text = prefix + new_experience + middle + new_heroes + suffix

# Sanity checks before writing
assert new_text.count("id=\"heroes\"")     == text.count("id=\"heroes\"")
assert new_text.count("id=\"experience\"") == text.count("id=\"experience\"")
assert new_text.count("</section>")        == text.count("</section>")

INDEX.write_text(new_text, encoding="utf-8")
print(f"Swapped. New file size: {len(new_text)} chars (was {len(text)}).")
print("Experience now precedes Heroes in source order.")
