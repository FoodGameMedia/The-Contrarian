# THE CONTRARIAN — SKILL.md
## Style Guide, Voice Rules & App Workflow Reference

**App:** `foodgamemedia.github.io/The-Contrarian`  
**Repo:** `FoodGameMedia/The-Contrarian` (single file `index.html`)  
**Author:** Julian Blok, Food Game Media  
**Last updated:** February 2026

---

## 1. WHAT THE CONTRARIAN IS

The Contrarian is an opinion column that finds the argument nobody is making — across **business, economics, culture, behavioural observations, people-watching, and wherever ideas intersect with how and why people do what they do.**

It is **not** a hospitality publication. It is not sector-specific. The beat is human behaviour and the surprising logic underneath ordinary decisions. Hospitality, finance, retail, urban planning, sport — all valid territory if the angle is behavioural and counterintuitive.

The closest reference point is **Rory Sutherland** (Ogilvy Vice Chairman, author of *Alchemy*): finding the overlooked signal in ordinary behaviour, reframing the obvious, and arguing that the psychological reality of a situation is usually more interesting than the economic one.

---

## 2. VOICE & TONE

### What it sounds like
- **Conversational authority.** The smartest person at the dinner party who has read everything and worked out why most of it is wrong. Never pompous, never casual to the point of being unserious.
- **Counterintuitive by default.** If the obvious answer is X, explore why not-X might be more interesting. The signature move is the reframe — taking something that looks like one thing and revealing it is actually another.
- **Rich analogy and metaphor.** Ideas land through unexpected parallels: evolutionary biology, poker strategy, behavioural economics, urban planning, military logistics, architecture, game theory. The best analogy is the most surprising one, not the most obvious.
- **Casual register, serious thinking.** Can be funny but never flippant. Every joke carries a point.
- **Confident.** Write with the certainty of someone who has seen the same pattern a thousand times and finally understands why it keeps repeating.

### What it does not sound like
- Academic or jargon-heavy
- Consultancy-speak (no frameworks, no "key takeaways")
- Hedging or wishy-washy ("arguably", "perhaps", "it could be said")
- AI-generic (no "delve", "nuanced", "multifaceted", "landscape", "crucial", "pivotal", "foster", "leverage", "paradigm")
- Newsletter-cheerful or LinkedIn-motivational

---

## 3. STRUCTURE RULES

Every Contrarian piece follows this arc — not rigidly, but reliably:

### Opening
- Hook in the **first two sentences**. A provocative observation, paradox, or counterintuitive claim.
- Do not open with context-setting or scene-setting. Start mid-argument.
- Do not open a sentence with: "Moreover", "Furthermore", "Indeed", "This is", "It is", "What is", "There is", "There are"

### Body
- Build the argument through **connected insights**, each one surprising. Not a linear march — a winding path that arrives somewhere unexpected.
- Use specific examples, data, and real situations from source material.
- Cite source URLs naturally in text as markdown hyperlinks: `[anchor text](url)`
- No subheadings. No bullet points. No numbered lists. **Flowing prose only.**
- Treat the reader as intelligent and experienced. Do not explain basic concepts.

### Closer — Food for Thought
- The final paragraph is pulled out and displayed as a separate **"Food for Thought"** block in the app's rendered output.
- It should be a **practical provocation** — something the reader will think about differently after reading.
- It speaks to anyone making decisions under uncertainty — essentially everyone.
- **No summarising conclusion.** End on a thought that keeps working after the reader finishes.
- No "in conclusion", "to summarise", "key takeaways", "in other words"

### Sign-off
- Always end the raw text with `- JB`

---

## 4. HARD RULES — NEVER VIOLATE

| Rule | Detail |
|------|--------|
| No em dashes | Never use `—`. Use a comma, full stop, or rewrite the sentence |
| No hedging | Never use "arguably" or "perhaps" — commit to the argument |
| No forbidden openers | Never open a sentence with "Moreover", "Furthermore", "Indeed", "This is", "It is", "What is", "There is", "There are" |
| No AI words | Never use: delve, nuanced, multifaceted, landscape, crucial, pivotal, foster, leverage, paradigm |
| No summaries | Never say "in conclusion", "to summarise", "key takeaways", "in other words" |
| No lists | Never use bullet points or numbered lists inside a piece |
| No "it's worth noting" | Or "interestingly" as a sentence opener |
| Cite URLs | Always cite sources as markdown hyperlinks in the body text |
| Sign off | Always end raw text with `- JB` |

---

## 5. HEADLINE RULES

- Generated automatically by the AI, prefixed with `HEADLINE:` on the first line of output
- Should be counterintuitive, specific, and carry the argument in itself
- Not clickbait. Not a question. A declarative claim that makes the reader want to argue with it or agree violently
- Examples of good Contrarian headlines:
  - *"Why Your Loyalty Program Is Making Customers Like You Less"*
  - *"The Safest Prediction Is Usually the One Nobody Will Make"*
  - *"Confidence and Correctness Are Not the Same Thing"*

---

## 6. APP WORKFLOW — HOW IT WORKS

The Contrarian app has five main input pathways to generate a piece:

### Pathway 1 — Compose Brief (main workflow)
1. Enter **Topic** and optional **Context** in the Compose panel
2. Go to **Topic Intelligence** to find sources — three modes:
   - **Trending:** Live news from NewsAPI/NewsData, filterable by region and period
   - **Search:** Search for specific topics
   - **Synthesis:** Select 2+ stories to find the hidden pattern connecting them
3. Select sources to include (tick boxes)
4. Choose word count (400 / 600 / 800 / 1000)
5. Choose tone chip (optional: Dry, Provocative, Melancholic, Hopeful, Furious)
6. Hit **Write** → generates full piece
7. Alternatively hit **Research & Write** to skip manual source selection and let AI search

### Pathway 2 — Drop a Link
- Paste 1–5 URLs, fetch content, generate from the fetched articles
- Single URL → piece based on that article
- Multiple URLs → **Synthesise** finds the one argument across all of them

### Pathway 3 — Paste Text
- Paste raw article text directly
- **Brief mode:** Use text as context, write piece from a brief
- **Direct mode:** Write directly from the pasted text

### Pathway 4 — Research & Write
- Enter topic only, AI searches the web for sources and writes in one step
- Faster but less editorial control

### Pathway 5 — Load from Articles (edit existing)
- Load a previously saved article from GitHub
- Edit in Raw Text tab
- Hit **↻ Update Preview** to re-render (always re-renders from raw text, not saved HTML)
- Save to overwrite the existing article on GitHub

---

## 7. OUTPUT PANEL

After generation, the output panel has three tabs:

| Tab | Contents |
|-----|----------|
| **Preview** | Fully rendered branded HTML article |
| **Raw Text** | Editable markdown/prose — edit here, hit ↻ Update Preview to re-render |
| **HTML** | Full HTML source for copy/paste |

### Food for Thought block
- The last paragraph of every piece is automatically extracted and displayed in a dark navy block labelled "Food for Thought"
- Below it: tone regeneration controls (Humorous / Grumpy old man / Compassionate / Provocative / Deadpan + custom)
- Hit **Rewrite** to regenerate only that closing paragraph in a different tone
- Rest of the article is untouched

### Rewrite panel
- Rewrite the whole piece with adjusted tone, angle, or additional context
- Preserves sources and topic

---

## 8. SOCIAL COMMENT PANEL

Generates branded LinkedIn comments/replies based on a post or article. Separate from article generation.

**Inputs:**
- Paste the post or article you're responding to (required)
- Your angle or POV (optional)
- Your context — role, audience, background (optional)
- Style chips: Julian Blok / The Contrarian / Provocateur / Empathetic / Devil's Advocate
- Custom style field
- Length: 1 sentence / 2 sentences / ~140 words
- Tone chips: Dry / Humorous / Grumpy old man / Compassionate / Provocative
- Custom tone field

**Output:** Word-count-badged comment text, copyable

---

## 9. ARTICLE STORAGE

- Articles save to GitHub repo: `FoodGameMedia/The-Contrarian/articles/`
- Hosted at: `foodgamemedia.github.io/The-Contrarian/articles/[filename]`
- Filename format: `DD.MM.YY-headline-slug-source-slug.html`
- Save goes through **Cloudflare Worker proxy** — GitHub token lives in Cloudflare secrets, never in the HTML file
- Worker URL: `https://young-fog-3045fgww-proxy.julian-68d.workers.dev`
- Auth header: `X-FGWW-Auth: foodgame2026`

---

## 10. DESIGN & BRAND

### Colours
| Role | Value |
|------|-------|
| Navy (primary dark) | `#0f1f38` |
| Deep navy (backgrounds) | `#050d1a` |
| Hot pink (accent) | `#e91e8c` |
| Soft pink (secondary accent) | `#f4a7b9` |
| Article body background | `#cdc8d9` (Soft Slate) |
| Light blush (alternate assets) | `#fce4ec` |

### Typography
- **Headlines:** Playfair Display, serif — italic, heavy weight
- **Body:** DM Sans, sans-serif
- **Labels/caps:** DM Sans, letter-spacing 3–4px, uppercase, 9–12px

### LinkedIn Assets (two colourways each)
- Profile Banner 1584×396
- Post Share Card 1200×627
- Square Post 1080×1080
- Article/Newsletter Hero 1920×1080
- Pull Quote Card 1200×627
- Comment/Reply Card 1200×400
- Newsletter Announcement Card 1200×627

---

## 11. TECHNICAL REFERENCE

### Key constants (in `index.html`)
```javascript
const PROXY_URL = 'https://young-fog-3045fgww-proxy.julian-68d.workers.dev';
const PROXY_SECRET = 'foodgame2026';
const GITHUB_OWNER = 'foodgamemedia';
const GITHUB_REPO = 'The-Contrarian';
const GITHUB_BRANCH = 'main';
```

### Cloudflare Worker routes
| Route | Method | Purpose |
|-------|--------|---------|
| `/` | POST | Anthropic API proxy |
| `/?fetch=URL` | GET | Article content fetcher |
| `/newsapi` | POST | NewsAPI proxy |
| `/newsdata` | POST | NewsData.io proxy |
| `/github` | POST | GitHub save/delete (token in env) |
| `/github?path=` | GET | GitHub file SHA check |

### Cloudflare Worker secrets
| Name | Purpose |
|------|---------|
| `ANTHROPIC_API_KEY` | Claude API |
| `FGWW_SECRET` | Auth (`foodgame2026`) |
| `GITHUB_TOKEN` | GitHub PAT (classic, repo scope, no expiry) |

### currentPiece state object
```javascript
currentPiece = {
  topic: '',        // Original topic/brief
  context: '',      // Additional context
  raw: '',          // Raw markdown body text
  body: '',         // Same as raw (used by save)
  html: '',         // Rendered HTML (what gets saved to GitHub)
  headline: '',     // Article headline
  sources: [],      // Array of {title, url, snippet}
  isLoadedHTML: false, // true when loaded from GitHub history
  date: '',         // ISO date string
  words: 0          // Target word count
}
```

### Important functions
| Function | Purpose |
|----------|---------|
| `renderPieceHTML(markdown, headline, sources)` | Renders raw text to branded HTML. Extracts last paragraph as Food for Thought block |
| `updatePreviewFromRaw()` | Re-renders preview from Raw Text tab. Always clears `isLoadedHTML` flag |
| `saveToHistory()` | Saves `currentPiece.html` to GitHub via Worker |
| `rewriteCloser(tone)` | Rewrites only the Food for Thought closing paragraph |
| `runSocialComment()` | Generates LinkedIn comment from pasted post |
| `extractHeadline(text)` | Strips `HEADLINE:` prefix, returns `{headline, body}` |

---

## 12. KNOWN BEHAVIOURS & GOTCHAS

- **Edit flow:** After loading an article from history and editing raw text, always hit **↻ Update Preview** before saving. The save uses `currentPiece.html` — Update Preview is what commits edits into it.
- **GitHub token:** Never put the GitHub PAT in the HTML file. It goes in Cloudflare Worker secrets as `GITHUB_TOKEN`. GitHub's secret scanner will revoke any token committed to the repo.
- **isLoadedHTML flag:** Articles loaded from GitHub set this to `true`. Update Preview now always clears it and re-renders from raw text regardless.
- **Food for Thought:** Only extracted if the piece has more than one `<p>` paragraph. Single-paragraph pieces won't show the block.
- **Social Comment word count:** The 140-word option generates a full mini opinion piece with setup, argument, and closer — not just a long comment.

---

## 13. HOW TO USE THIS SKILL FILE

### Loading it in a new chat
This file lives at `FoodGameMedia/The-Contrarian/SKILL.md` on GitHub. At the start of any new session working on The Contrarian, fetch it via:
```
https://raw.githubusercontent.com/FoodGameMedia/The-Contrarian/main/SKILL.md
```
Or upload it directly alongside `index.html`. Tell Claude: *"Read the SKILL.md first."*

### How Claude should behave when using this skill
- Read this file completely before writing any code or making any changes to the app
- Cross-reference any proposed changes against the voice rules, hard rules, and technical reference sections
- If a user request would violate a hard rule (e.g. adding bullet points to article output, using a banned word), flag it before proceeding
- Apply the correct voice and structural rules to any generated Contrarian content — headlines, article bodies, Food for Thought closers, social comments

### Self-improvement instructions for Claude
Claude must actively maintain and improve this skill file. Specifically:

**Flag and suggest updates when:**
- A new feature is added to the app (new panel, new workflow, new output format)
- A technical detail changes (new Worker route, new secret, new constant, new function)
- A new voice rule or hard rule is established during a session
- A gotcha or edge case is discovered that isn't documented here
- A design decision is made that affects brand colours, typography, or asset specs
- The app's workflow changes in any meaningful way

**How to flag:** At the end of any session where the above occurs, Claude should say:
> *"SKILL.md needs updating — [brief description of what changed]. Want me to push the update to GitHub now?"*

**When prompted to update:** Rewrite only the affected sections, increment the "Last updated" date at the top, and push to GitHub via the Worker proxy using the same save mechanism as articles (path: `SKILL.md`, branch: `main`).

**What Claude should never do:**
- Assume the SKILL.md is current if it hasn't been read this session
- Make changes to the app that contradict documented rules without flagging the contradiction
- Let a session end where significant undocumented changes were made without prompting an update
