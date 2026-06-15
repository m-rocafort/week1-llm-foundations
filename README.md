# Week 1 — LLM Foundations & Your First API Calls

**Goal:** Talk to an LLM programmatically. By the end you can call the Claude API, shape behavior with system prompts, and reason about cost/model choice.

This is **Project 0** of your roadmap — the warm-up before the 5 portfolio projects. Commit it to GitHub to start your green-squares streak.

---

## 1. One-time setup (~10 min)

```bash
# From this folder:
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# (Git Bash: source .venv/Scripts/activate)

pip install -r requirements.txt
```

### Get an API key
- **Anthropic (Claude):** https://console.anthropic.com → API Keys → Create Key. Add ~$5 of credits (plenty for Week 1).
- **OpenAI (optional, for comparison later):** https://platform.openai.com/api-keys

### Configure secrets
```bash
copy .env.example .env      # Windows
# then open .env and paste your real key(s)
```
> ⚠️ `.env` is gitignored. **Never commit real keys.** Only `.env.example` (with placeholders) is tracked.

---

## 2. Run the exercises (in order)

```bash
python src/01_first_call.py          # your first LLM response
python src/02_prompt_experiments.py  # system prompts + streaming
python src/03_model_comparison.py    # cost & model-choice intuition
```

Each file is heavily commented — read top to bottom, then **change things and re-run.** Curiosity here is the whole point.

---

## 3. Learning checklist

- [ ] I made a successful API call and printed the response
- [ ] I changed the **system prompt** and saw behavior change
- [ ] I streamed a response token-by-token
- [ ] I can explain what `max_tokens` does and why it matters
- [ ] I understand the rough cost difference between Opus and Haiku
- [ ] I committed this folder to GitHub
- [ ] I wrote 1 LinkedIn "build-in-public" post (see roadmap §5)

---

## 4. Concepts you just learned

| Concept | What it is |
|---------|-----------|
| **Message** | One request = your `messages` (conversation) + optional `system` prompt |
| **System prompt** | Sets the model's role/rules; the #1 lever for reliable behavior |
| **Tokens** | How text is chunked & billed (~4 chars ≈ 1 token in English) |
| **`max_tokens`** | Hard cap on the *response* length; too low truncates mid-thought |
| **Model choice** | Opus = smartest/pricier; Haiku = fast/cheap. Pick per task. |
| **Streaming** | Get tokens as they're generated (better UX, avoids timeouts) |

---

## 5. Next week (Week 2)
Prompt engineering + **structured outputs** (JSON) + tool calling → your first portfolio project, the **Intelligent Document Extractor**. See `../AI-Automation-Engineer-Roadmap.md`.

---

### Optional: turn this into a Git repo
```bash
git init
git add .
git commit -m "Week 1: LLM foundations"
# then create an empty repo on GitHub and push
```
