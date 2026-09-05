# Pre-Course Screening Interview (15–20 min)

Conversational, no whiteboard/live coding — you're checking they can reason about code and tooling, not testing perfect syntax recall. Score each core area Meets / Borderline / Fail.

## Core (12 min — ask all 4)

### 1. Python — reading code (3 min)

**Ask:** "What does this print?"

```python
def process(items):
    return [x * 2 for x in items if x % 2 == 0]

print(process([1, 2, 3, 4, 5, 6]))
```

**Answer:** `[4, 8, 12]`
**Meets bar:** correctly traces the list comprehension + filter. **Fail signal:** can't explain what the `if` clause does.

### 2. Git — workflow (3 min)

**Ask:** "Walk me through changing a shared repo, start to finish."
**Answer:** clone → create a branch → commit → push branch → open a PR → address review comments → merge.
**Follow-up:** "You just pushed a commit with a real API key in it. What now?"
**Answer key point:** rotate/revoke the key immediately — deleting the file in a new commit doesn't remove it from history. Full precision on rewriting history not required; the "rotate the key" instinct is what matters.

### 3. CLI/Terminal (3 min)

**Ask:** "500 log files in a folder — how do you find every line containing 'ERROR' from the terminal?"
**Answer:** `grep -r "ERROR" .` (exact flags don't matter, `grep` naming does)
**Meets bar:** reaches for grep/search unprompted. **Fail signal:** would open each file manually or in a GUI.

### 4. Docker — concept (3 min)

**Ask:** "In your own words: what's the difference between a Docker image and a container?"
**Answer:** image = the static build/template; container = a running instance of that image. One image, many possible containers.
**Meets bar:** conceptual answer is enough — hands-on Dockerfile experience is not required, it's covered in the course.

## If time allows (7 min — informational, not gating)

### 5. JavaScript — async basics (2 min)

**Ask:** "What order do these print in, and why?"

```javascript
console.log("A");
setTimeout(() => console.log("B"), 0);
console.log("C");
```

**Answer:** A, C, B — `setTimeout` goes to the event queue even at 0ms and runs after all synchronous code finishes.
**Purpose:** JS is no longer required (MCP lab is Python-only now) but still shows up in Cursor/Cline exercises and the AI-Assisted Development frontend phase — good to know their comfort level, not a gating question.

### 6. OS / environment readiness (2 min)

**Ask:** "What OS do you develop on, and how comfortable are you in a terminal day-to-day?" If Windows: "Have you set up WSL2 before?"
**Purpose:** flags who needs a pre-week-1 environment setup session (Windows without WSL2, or "I mostly use GUI tools").

### 7. AI tooling exposure (1 min)

**Ask:** "Used Copilot, ChatGPT, Claude, or Cursor before? What was that like?"
**Purpose:** calibrates pacing for weeks 5–10, not a pass/fail signal.

### 8. Debugging mindset (2 min)

**Ask:** "Tell me about a bug that took you a while to solve. How'd you get there?"
**Meets bar:** describes a structured process (isolate → read the error → search docs → ask for help) rather than pure guesswork. This matters because the labs are self-directed and will hit friction.

## Scoring

| Result         | Core areas at "Meets" (of 4) | Action                                                                      |
| -------------- | ---------------------------- | --------------------------------------------------------------------------- |
| **Ready**      | 3–4                          | Start on schedule                                                           |
| **Borderline** | 2                            | Offer a 1-week bridging session (usually Git + CLI or Python) before week 1 |
| **Not yet**    | ≤1                           | Not ready for this cohort — revisit next intake                             |
