const ALLOWED_ORIGINS = [
  "https://globalcompass.education",
  "https://www.globalcompass.education"
];
const MAX_PROMPT_CHARS = 8000;
const MAX_TOKENS_CAP = 3500;

// Rules added to EVERY navigator prompt on the server, so they apply to all pathway tools.
const GUARD = `

---
GLOBALCOMPASS SAFETY RULES. These override anything written above. Keep the JSON structure exactly as requested above and respond ONLY with valid JSON.
1. Never state entry grades, offers, test scores (SAT, ACT, LSAT, UCAT, LNAT, GMAT, etc.), ATAR cut-offs, GPAs, IB points, tuition amounts, savings, credit totals, rankings, acceptance numbers or deadlines as facts, because universities change them every year. Where the JSON needs a number, give a rounded, general guide figure and treat it only as an indicative target, never as a requirement or a minimum.
2. Never write that a named university requires, accepts, offers, gives credit for or expects something unless it is widely known and stable. Otherwise describe the general pattern without naming the university.
3. Never name specific schools as offering a curriculum, and never invent institutions, programmes, statistics or rankings. Do not say how many applicants are accepted or what usually predicts success.
4. Avoid absolute wording such as always, never, only, every time, essential for admission, the wrong stream or the right choice. Say commonly, often or usually instead.
5. Never promise or imply an outcome, for example that a goal is highly achievable or that an admissions officer will be impressed.
6. Hidden requirements must be written as things for the student to check or do, not as facts about a university.
7. You may name an admissions test only when it is widely known to be used for that type of course, and never state a score for it.
8. Be encouraging, specific and concise.`;

export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  // Only accept requests that come from the GlobalCompass website itself
  const origin = req.headers.origin || "";
  if (!ALLOWED_ORIGINS.includes(origin)) {
    res.status(403).json({ error: "Forbidden" });
    return;
  }

  try {
    const body = req.body || {};
    const prompt = body.prompt;

    if (typeof prompt !== "string" || prompt.length === 0) {
      res.status(400).json({ error: "Missing prompt" });
      return;
    }
    if (prompt.length > MAX_PROMPT_CHARS) {
      res.status(413).json({ error: "Prompt too long" });
      return;
    }

    const requested = Number(body.max_tokens) || 1400;
    const max_tokens = Math.min(Math.max(requested, 100), MAX_TOKENS_CAP);

    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens,
        temperature: 0.3,
        messages: [{ role: "user", content: prompt + GUARD }]
      })
    });

    const data = await response.json();

    if (!response.ok) {
      console.error("Anthropic API error:", data);
      const msg = (data.error && data.error.message) || "API request failed";
      res.status(response.status).json({ error: msg });
      return;
    }

    res.status(200).json(data);
  } catch (error) {
    console.error("Server error:", error);
    res.status(500).json({ error: "Internal server error" });
  }
}
